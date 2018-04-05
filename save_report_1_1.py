# TODO: V_2.0: get different types of reports (maybe based on input).
# TODO: Fetch many reports at once. See 'SNOTEL_best_conditions' for example code.
# TODO: add out-of-state capability (e.g., Cooke City)

import requests, csv
from datetime import date
import os

stations = {
    'casper_mtn': ['389', 'WY', 'Casper Mountain'],
    'togwotee_pass': ['822', 'WY', 'Togwotee Pass'],
    'med_bow': ['1196', 'WY', 'Medicine Bow'],
    'powder_river_pass': ['703', 'WY', 'Powder River Pass - Big Horns'],
    'old_battle': ['673', 'WY', 'Old Battle - Sierra Madres'],
    'wolverine': ['875', 'WY', 'Wolverine - Absarokas'],
    'townsend_creek': ['826', 'WY', 'Townsend Creek - SE Wind Rivers'],
    'blind_bull': ['353', 'WY', 'Blind Bull Summit - Wyoming Range'],
    'fisher_creek': ['480', 'MT', 'Fisher Creek - Cooke City'],
    'willow_park': ['870', 'CO', 'Willow Park - Estes ']
    }

r_length = int(input('Report depth in years: '))


def get_month():
    month = date.today().month
    return month


def get_end_month():
    end_month = str(get_month())
    # End in Dec. of the last complete calendar year (becomes negative in URL request).
    return end_month


def get_start_month(years):
    start_month = str(12 * years + get_month() - 1)
    # start in January 20 years prior to current date.
    return start_month


for get_station in stations:
    station = stations[get_station][0]
    state = stations[get_station][1]
    st_name = stations[get_station][2]
    code = 'SNTL'
    base_url = 'https://wcc.sc.egov.usda.gov/reportGenerator/view_csv/' \
               + 'customSingleStationReport/monthly/start_of_period/'
    values = 'WTEQ::value,SNWD::value,PREC::value,TMAX::value,TMIN::value,TAVG::value'
    st = get_start_month(r_length)
    en = get_end_month()

    r = requests.get(base_url + '{}:{}:{}|id=%22%22|name/-{},-{}/'.format(station, state, code,
                                                                          st, en) + values)
    data = r.text

    cwd = os.getcwd()
    fo = open(cwd + '/Data/long_term_reports/{}_{}year.csv'.format(get_station, r_length), 'w')
    fo.write(data)
    fo.close()

