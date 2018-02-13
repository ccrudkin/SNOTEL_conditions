#! python3

# TODO: add out-of-state capability (e.g., Cooke City) and prettier names for humans. DONE!
# TODO: Clean up score_location() function with variables instead of operations. DONE!
# TODO: dynamically find first cell of data instead of counting by hand. DONE!
# TODO: for ^ : data_start = [data.index(row) for row in data if row[0] == 'Date'][0] + 1 DONE!

import requests, csv
from datetime import date

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

f = {
    'date': 0,
    's_depth': 1,
    'temp_max': 2,
    'temp_min': 3,
    'temp_avg': 4
    }

# get_station = input('Choose station for report: {} '.format([x for x in stations]))

# station = stations[get_station]
# state = 'WY'
code = 'SNTL'
base_url = 'https://wcc.sc.egov.usda.gov/reportGenerator/view_csv/customSingleStationReport/daily/'
values = 'SNWD::value,TMAX::value,TMIN::value,TAVG::value'
st = '-29'
en = '-1'


def get_data(s):
    s_code = stations[s][0]
    state = stations[s][1]
    r = requests.get(base_url + '{}:{}:{}|id=%22%22|name/{},{}/'.format(s_code, state, code, st, en) + values)
    data = r.text

    fo = open('C:/Users/ccrud/PycharmProjects/snotel/Data/CSVs/30_day_temps/{}_{}.csv'.format(s, '30_day'), 'w')
    fo.write(data)
    fo.close()

    with open('C:/Users/ccrud/PycharmProjects/snotel/Data/CSVs/30_day_temps/{}_{}.csv'.format(s, '30_day'), 'r') as fo:
        cdata = csv.reader(fo)
        cdata = list(cdata)

    data_start = [cdata.index(row) for row in cdata if row[0] == 'Date'][0] + 1

    return cdata, data_start


def snow_acc(d, ds):  # compare snow at most recent data point within 7 days to oldest data point within 7 days.
    days = list(range(ds + 22, ds + 29))
    for n in days[::-1]:
        if d[n][f['s_depth']] != '':
            for u in days:
                if d[u][f['s_depth']] != '':
                    return int(d[n][f['s_depth']]) - int(d[u][f['s_depth']])


def above_freezing(d, ds):  # Get days above freezing for last 7 days.
    above = []
    count = 0
    for n in range(ds + 22, ds + 29):
        if d[n][f['temp_max']] != '':
            if int(d[n][f['temp_max']]) > 32:
                entry = [d[n][f['date']], d[n][f['temp_max']]]
                above.append(entry)
                count += 1
    return count, above


def score_location(station_list):
    best_acc = -100
    worst_acc = 100
    daf = 0
    daf_w = 0
    best_site = 0
    worst_site = 0
    for l in station_list:
        cdata = get_data(l)[0]
        data_start = get_data(l)[1]
        # print(l)  # for debugging date ranges
        # print(cdata[data_start])
        # print(cdata[data_start + 22])
        # print(cdata[data_start + 28])
        snacc = snow_acc(cdata, data_start)
        abfre = above_freezing(cdata, data_start)[0]
        if snacc > best_acc:
            best_acc = snacc
            daf = abfre
            best_site = l
        if snacc < worst_acc:
            worst_acc = snacc
            daf_w = abfre
            worst_site = l
        if snacc == best_acc:
            if abfre < daf:
                daf = abfre
                best_site = l
        if snacc == worst_acc:
            if abfre > daf_w:
                daf_w = abfre
                worst_site = l
    print('\nBest snow conditions for past week: {}'.format(stations[best_site][2]))
    print('Snow change: {}'.format(best_acc))
    print('Days above freezing: {}'.format(daf))
    print()
    print('Worst snow conditions for past week: {}'.format(stations[worst_site][2]))
    print('Snow change: {}'.format(worst_acc))
    print('Days above freezing: {}'.format(daf_w))

score_location(stations)



