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
            plt.plot(list(range(1998, 1998 + len(l))), l)  # Plot (year, temperature)
            combined_y.append(l)  # create one long list of y-values to feed into plot.
            combined_x.append(list(range(1998, 1998 + len(l))))  # repeat so every y has an x.

all_x = []
all_y = []

for lst in combined_x:
    for pt in lst:
        all_x.append(pt)
for lst in combined_y:
    for pt in lst:
        all_y.append(pt)

# print(all_x)
# print(all_y)

sts.plot_least_squares_reg(sts.print_statitics(all_x, all_y))

plt.title('March temp. deviation from average, 1998-2017', size=24)
plt.xlabel('Years', size=20)
plt.ylabel('Deviation (*F)', size=20)
plt.xticks(range(1998, 2018, 2), size=16)
plt.yticks(size=16)
plt.show()
