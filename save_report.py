# TODO: V_2.0: get different types of reports (maybe based on input).
# TODO: Fetch many reports at once. See 'SNOTEL_best_conditions' for example code.
# TODO: add out-of-state capability (e.g., Cooke City)

import requests, csv
from datetime import date

stations = {
    'casper_mtn': '389',
    'togwotee_pass': '822',
    'grand_targhee': '1082',
    'med_bow': '1196',
    'powder_river_pass': '703',
    'old_battle': '673',
    'wolverine': '875',
    'townsend_creek': '826'
    }
get_station = input('Choose station for monthly report: {} '.format([x for x in stations]))
r_length = int(input('Report depth in years: '))


def get_month():
    month = date.today().month
    return month


def get_end_month():
    end_month = str(get_month())  # End in Dec. of the last complete calendar year (becomes negative in URL request).
    return end_month


def get_start_month(years):
    start_month = str(12 * years + get_month() - 1)  # start in January 20 years prior to current date.
    return start_month


station = stations[get_station]
state = 'WY'
code = 'SNTL'
base_url = 'https://wcc.sc.egov.usda.gov/reportGenerator/view_csv/customSingleStationReport/monthly/start_of_period/'
values = 'WTEQ::value,SNWD::value,PREC::value,TMAX::value,TMIN::value,TAVG::value'
st = get_start_month(r_length)
en = get_end_month()

r = requests.get(base_url + '{}:{}:{}|id=%22%22|name/-{},-{}/'.format(station, state, code, st, en) + values)
data = r.text

fo = open('C:/Users/ccrud/PycharmProjects/snotel/Data/CSVs/{}_{}year.csv'.format(get_station, r_length), 'w')
fo.write(data)
fo.close()

