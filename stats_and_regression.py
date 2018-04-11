import matplotlib.pyplot as plt


def get_data_mean(biv_coors):
    """Simply returns the mean of a set of data. Input a list of x coords. or y coords."""
    return sum(biv_coors) / len(biv_coors)


def get_var(biv_coors):
    """Returns the variance for a dataset, usually a list of x- or y-coordinates."""
    mean = get_data_mean(biv_coors)
    dif_sqd = 0
    for each in biv_coors:
        dif_sqd += (each - mean) ** 2
    return dif_sqd / (len(biv_coors) - 1)  # 'n - 1' returns SAMPLE variance.
    # Sample variance (not population variance) is needed to calculate
    # correlation coefficient and the least squares regression line.


def get_std_dev(biv_coors):
    """Returns standard deviation for a dataset, usually a list of x- or y-coordinates."""
    coors_var = get_var(biv_coors)
    return coors_var ** .5


def get_corr_coef(biv_coors_x, biv_coors_y):
    """Returns 'r', the correlation coefficient for a set of x- and y-coordinates."""
    cx = biv_coors_x
    cy = biv_coors_y
    d_sum = 0
    for point in range(len(biv_coors_x)):
        # Sums the 'z-scores' for each data point in the lists.
        d_sum += (((cx[point] - get_data_mean(cx)) / get_std_dev(cx))
                    * ((cy[point] - get_data_mean(cy)) / get_std_dev(cy)))
    r = (1 / (len(cx) - 1)) * d_sum  # Formula for correlation coefficient.
    return r


def least_sqs_line_points(biv_coors_x, biv_coors_y):
    """Returns a list of 3 points: (x, y) where x == 0, where x == mean(x), and where x == 2x."""
    r = get_corr_coef(biv_coors_x, biv_coors_y)
    sx = get_std_dev(biv_coors_x)  # Just to shorten formulas for readability.
    sy = get_std_dev(biv_coors_y)
    m = r * (sy / sx)  # Slope; 'm' as in y = mx + b.
    xmean = get_data_mean(biv_coors_x)
    ymean = get_data_mean(biv_coors_y)
    x_spread = (max(biv_coors_x) - min(biv_coors_x)) / 2
    return [[xmean - x_spread, round(ymean - x_spread * m, 3)], [xmean, round(ymean, 3)],
            [xmean + x_spread, round(ymean + x_spread * m, 3)]]
    # ^^^ Returns 3 points that span most of the dataset in most cases.


def print_statitics(biv_coors_x, biv_coors_y):  # TODO: add option not to print? 'if np:'
    """Prints basic statistics for x, y dataset, including mean, variance,
    standard deviation, correlation coefficient, and a list of the 3 least
    squares line points. RETURNS a list of the least squares line points."""
    x = biv_coors_x
    y = biv_coors_y
    print('Data mean:          x: {}   y: {}'.format(round(get_data_mean(x), 3),
                                                     round(get_data_mean(y), 3)))
    print('Variance:           x: {}   y: {}'.format(round(get_var(x), 3), round(get_var(y), 3)))
    print('Standard deviation: x: {}   y: {}'.format(round(get_std_dev(x), 3),
                                                     round(get_std_dev(y), 3)))
    print('Correlation coef.: r = {}'.format(round(get_corr_coef(x, y), 3)))
    lsl_points = least_sqs_line_points(x, y)
    print('Least sqs. points: {}'.format(lsl_points))
    return lsl_points


def plot_least_squares_reg(lsl_points):
    """Plots least squares regression line. Argument should be 'print_statistics' output."""
    plt.plot([lsl_points[0][0], lsl_points[1][0], lsl_points[2][0]],
             [lsl_points[0][1], lsl_points[1][1], lsl_points[2][1]], 'r--')
    # Reorganizes lsl_points output into [x, x, x], [y, y, y], 'style' for plotting.


if __name__ == "__main__":
    # For debugging and demonstration; insert data for x and y.
    x = [1, 2, 2, 3]
    y = [1, 2, 3, 6]

    plt.plot(x, y, 'o')
    plt.axis([0, 10, 0, 10])
    plt.show()