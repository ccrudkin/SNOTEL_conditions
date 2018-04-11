import os
import matplotlib.pyplot as plt
import csv
import stats_and_regression as sts

cwd = os.getcwd()
combined_x = []
combined_y = []

for filename in os.listdir(cwd + '/Data/long_term_reports/'):
    if filename.startswith('dev_'):
        with open(cwd + '/Data/long_term_reports/' + filename) as f:
            data = list(csv.reader(f))
            l = []
            for set in data[1:]:
                l.append(float(set[1]))  # NUMBERS, not strings. Took long enough.
            # print(l)
            plt.plot(list(range(0, len(l))), l)
            combined_y.append(l)
            combined_x.append(list(range(0, len(l))))

all_x = []
all_y = []

for lst in combined_x:
    for pt in lst:
        all_x.append(pt)
for lst in combined_y:
    for pt in lst:
        all_y.append(pt)

sts.plot_least_squares_reg(sts.print_statitics(all_x, all_y))

plt.title('March temp. deviation from average, 1998-2017')
plt.xlabel('Years')
plt.ylabel('Deviation (*F)')
plt.show()
