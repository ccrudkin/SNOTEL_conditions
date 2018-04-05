# TODO: Clean up.
# TODO: Increase versatility with user input for desired actions.

import csv
import os

f = {  # Snotel data field labels.
    'date': 0,
    'swe': 1,
    's_depth': 2,
    'prec_accum': 3,
    'temp_max': 4,
    'temp_min': 5,
    'temp_avg': 6
    }


def get_avg_temps(month_num):
    for y in range(0, 20):
        month = y * 12 + 58 + month_num
        print('Month: ' + data[month][f['date']], 'Temp.: ' + data[month][f['temp_avg']])


def get_deviation(month_num):
    temps = []
    for y in range(0, 20):
        month = y * 12 + 58 + month_num
        if month <= len(data):
            mt = data[month][f['temp_avg']]
            if mt != '':
                temps.append(int(mt))
    print(temps)
    t_avg = sum(temps) / len(temps)
    print(t_avg)
    dev_file = 'dev_' + local_file
    fo = open('C:/Users/ccrud/PycharmProjects/snotel/Data/long_term_reports/{}'.format(dev_file), 'w', newline='')
    o_w = csv.writer(fo)
    o_w.writerow(['Month', 'Deviation, 20 year temp. avg.'])
    for y in range(0, 20):
        month = y * 12 + 58 + month_num
        if data[month][f['temp_avg']] != '':
            dev = round(int(data[month][f['temp_avg']]) - t_avg, 1)
            print('Month: ' + data[month][f['date']], 'T. dev.: ' + str(dev))
            o_w.writerow([data[month][f['date']], str(dev)])
        else:
            print('Month: ' + data[month][f['date']], 'T. dev.: ' + 'No Data')
            o_w.writerow([data[month][f['date']], '0'])
    fo.close()


def get_snow_depth(month_num, y):
    month = y * 12 + 58 + month_num
    if month <= len(data):
        # print('Month: ' + data[month][f['date']], 'Snow depth: ' + data[month][f['s_depth']])
        return data[month][f['date']], data[month][f['s_depth']]


def get_snow_d_avg(month_num):
    d_list = []
    for y in range(0, 20):
        sd = get_snow_depth(month_num, y)[1]
        if sd != '':
            d_list.append(int(sd))
    sd_avg = sum(d_list) / len(d_list)
    return sd_avg


def get_snow_deviation(month_num):
    sd_avg = get_snow_d_avg(month_num)
    fn = 'sd_dev_''' + local_file
    fo = open('C:/Users/ccrud/PycharmProjects/snotel/Data/long_term_reports/{}'.format(fn), 'w', newline='')
    o_w = csv.writer(fo)
    o_w.writerow(['Date', 'Deviation, 20 year snow depth avg.'])
    for y in range(0, 20):
        m = get_snow_depth(month_num, y)[0]
        if get_snow_depth(month_num, y)[1] != '':
            dev = round(int(get_snow_depth(month_num, y)[1]) - round(sd_avg, 1), 1)
            print('Month: ' + str(m), 'Snow depth deviation: ' + str(dev))
            o_w.writerow([str(m), str(dev)])
        else:
            print('Month: ' + str(m), 'Snow depth deviation: ' + 'No data.')
            o_w.writerow([str(m), '0'])
    fo.close()


cwd = os.getcwd()

for filename in os.listdir(cwd + '/Data/long_term_reports'):
    local_file = filename
    with open(cwd + '/Data/long_term_reports/{}'.format(local_file)) as fo:
        data = csv.reader(fo)
        data = list(data)
        get_deviation(3)
        get_snow_deviation(3)