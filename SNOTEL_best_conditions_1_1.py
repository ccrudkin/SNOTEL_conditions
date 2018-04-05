#! python3

# TODO: Orient and locate data from end of data instead of beginning.

import requests
import csv
from datetime import date
import os

stations = {
    'casper_mtn': ['389', 'WY', 'Casper Mountain'],
    'togwotee_pass': ['822', 'WY', 'Togwotee Pass'],
    'grand_targhee': ['1082', 'WY', 'Grand Targhee'],
    'med_bow': ['1196', 'WY', 'Medicine Bow'],
    'powder_river_pass': ['703', 'WY', 'Powder River Pass (Big Horns)'],
    'old_battle': ['673', 'WY', 'Old Battle (Sierra Madres)'],
    'wolverine': ['875', 'WY', 'Wolverine (Absarokas)'],
    'townsend_creek': ['826', 'WY', 'Townsend Creek (SE Wind Rivers)'],
    'blind_bull': ['353', 'WY', 'Blind Bull Summit (Wyoming Range)'],
    'fisher_creek': ['480', 'MT', 'Fisher Creek (Cooke City)']
    }

f = {  # Data field numbers as values, listed by short descriptors as keys for easier remembering.
    'date': 0,
    's_depth': 1,
    'temp_max': 2,
    'temp_min': 3,
    'temp_avg': 4
    }

code = 'SNTL'
base_url = 'https://wcc.sc.egov.usda.gov/reportGenerator/view_csv/customSingleStationReport/daily/'
values = 'SNWD::value,TMAX::value,TMIN::value,TAVG::value'
st = '-28'
en = '0'
cwd = os.getcwd()


def get_data(s):
    """Fetches data for a single station and saves CSV to local disk."""
    s_code = stations[s][0]
    state = stations[s][1]
    r = requests.get(base_url + '{}:{}:{}|id=%22%22|name/{},{}/'.format(s_code, state, code, st,
                                                                        en) + values)
    data = r.text

    fo = open(cwd + '/Data/CSVs/30_day_temps/{}_{}.csv'.format(s, '30_day'), 'w')
    fo.write(data)
    fo.close()

    with open(cwd + '/Data/CSVs/30_day_temps/{}_{}.csv'.format(s, '30_day'), 'r') as fo:
        cdata = csv.reader(fo)
        cdata = list(cdata)

    data_end = len(cdata) - 1
    # print(data_end)

    return cdata, data_end


def snow_acc(d, de):
    """Compare snow at most recent data point within 7 days to oldest
    data point within 7 days."""
    days = list(range(de - 6, de + 1))
    # print(days)
    for n in days[::-1]:
        if d[n][f['s_depth']] != '':
            for u in days:
                if d[u][f['s_depth']] != '':
                    return int(d[n][f['s_depth']]) - int(d[u][f['s_depth']]), d[u][f['date']], \
                           d[n][f['date']]


def above_freezing(d, de):
    """Get days above freezing for last 7 days."""
    above = []
    count = 0
    for n in range(de - 6, de + 1):
        if d[n][f['temp_max']] != '':
            if int(d[n][f['temp_max']]) > 32:
                entry = [d[n][f['date']], d[n][f['temp_max']]]
                above.append(entry)
                count += 1
    return count, above


def score_location(station_list):
    """Call functions to get data and parse it, returning highest snow
    gains and losses as 'best' and 'worst'."""
    best_acc = -100
    bast = 0  # Best accumulation start date.
    wast = 0  # Worst accumulation start date.
    baen = 0  # Best accumulation end date.
    waen = 0  # Worst accumulation end date.
    worst_acc = 100
    daf = 0
    daf_w = 0
    best_site = 0
    worst_site = 0
    for l in station_list:
        cdata = get_data(l)[0]
        data_end = get_data(l)[1]
        # print(l)  # for debugging date ranges
        # print(cdata[data_start])
        # print(cdata[data_start + 22])
        # print(cdata[data_start + 28])
        snacc = snow_acc(cdata, data_end)[0]
        abfre = above_freezing(cdata, data_end)[0]
        snacc_start = snow_acc(cdata, data_end)[1]
        snacc_end = snow_acc(cdata, data_end)[2]
        if snacc > best_acc:
            best_acc = snacc
            daf = abfre
            best_site = l
            bast = snacc_start
            baen = snacc_end
        if snacc < worst_acc:
            worst_acc = snacc
            daf_w = abfre
            worst_site = l
            wast = snacc_start
            waen = snacc_end
        if snacc == best_acc:
            if abfre < daf:
                daf = abfre
                best_site = l
                bast = snacc_start
                baen = snacc_end
        if snacc == worst_acc:
            if abfre > daf_w:
                daf_w = abfre
                worst_site = l
                wast = snacc_start
                waen = snacc_end
    print('\nBest snow conditions for past week: {}'.format(stations[best_site][2]))
    print('Snow change: {} from {} to {}'.format(best_acc, bast, baen))
    print('Days above freezing: {}'.format(daf))
    print()
    print('Worst snow conditions for past week: {}'.format(stations[worst_site][2]))
    print('Snow change: {} from {} to {}'.format(worst_acc, wast, waen))
    print('Days above freezing: {}'.format(daf_w))


score_location(stations)

