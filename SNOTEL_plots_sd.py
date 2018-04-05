import os
import matplotlib.pyplot as plt
import csv

cwd = os.getcwd()

for filename in os.listdir(cwd + '/Data/long_term_reports/'):
    if filename.startswith('sd_dev_'):
        with open(cwd + '/Data/long_term_reports/' + filename) as f:
            data = list(csv.reader(f))
            l = []
            for set in data[1:]:
                l.append(float(set[1]))  # NUMBERS, not strings. Took long enough.
            print(l)
            plt.plot(l)

plt.title('March snow depth deviation from average, 1998-2017')
plt.xlabel('Years')
plt.ylabel('Deviation (inches)')
plt.show()
