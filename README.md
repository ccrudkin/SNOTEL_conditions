# SNOTEL_conditions
Scripts to fetch and analyze CSV reports from the National Water and Climate Center's SNOTEL web tool. All scripts are written a bit rigidly for specific applications and sites, but can easily be customized for other purposes and locations.

save_report_1_1.py is a simple tool for fetching a CSV report from SNOTEL and saving it to a local directory. May be customized to include different data fields or report resolution.

data_processing.py offers limited data processing for locally saved CSV reports, with functions to create new CSVs with temperature and snow depth averages, plus deviations from average over the span of the report. Needs cleanup work.

SNOTEL_best_conditions_1_1.py implements an algorithm to judge the 'best' snow conditions among the sites listed in the site dictionary. Best is defined as the site with the largest 7-day increase in snow, and in the case of a tie, the site with the fewest number of days above freezing.

SNOTEL_plots.py and SNOTEL_plots_sd.py offer basic charting via matplotlib, and thus are matplotlib-dependent.
