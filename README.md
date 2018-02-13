# SNOTEL_conditions
Scripts to get and analyze CSV reports from the National Water and Climate Center's SNOTEL web tool. All scripts are written a bit rigidly for specific applications and sites, but can easily be customized for other purposes and locations.

save_report.py is a simple tool for fetching a CSV report from SNOTEL and saving it to a local hard drive. May be customized to include different data fields or report resolution.

first_experiments.py offers rudimentary data processing for locally saved CSV reports, with functions to create new CSVs with temperature and snow depth averages and deviations from average over the span of the report. Needs cleanup work.

SNOTEL_best_conditions.py implements a crude algorithm to judge the 'best' snow conditions among the sites listed in the site dictionary. Best is defined as the site with the largest 7-day increase in snow, and in the case of a tie, the site with the fewest number of days above freezing.
