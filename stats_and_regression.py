import matplotlib.pyplot as plt


def get_data_mean(biv_coors):
    return sum(biv_coors) / len(biv_coors)


def get_var(biv_coors):
    mean = get_data_mean(biv_coors)
    # print('Data mean: {}'.format(mean))
    dif_sqd = 0
    for each in biv_coors:
        dif_sqd += (each - mean) ** 2
    return dif_sqd / (len(biv_coors) - 1)


def get_std_dev(coors_var):
    return coors_var ** .5


def get_corr_coef(biv_coors_x, biv_coors_y):
    cx = biv_coors_x
    cy = biv_coors_y
    d_sum = 0
    for point in range(len(biv_coors_x)):
        d_sum += (((cx[point] - get_data_mean(cx)) / get_std_dev(get_var(cx)))
                    * ((cy[point] - get_data_mean(cy)) / get_std_dev(get_var(cy))))
    r = (1 / (len(cx) - 1)) * d_sum
    return r


def least_sqs_line_points(biv_coors_x, biv_coors_y):
    r = get_corr_coef(biv_coors_x, biv_coors_y)
    sx = get_std_dev(get_var(biv_coors_x))
    sy = get_std_dev(get_var(biv_coors_y))
    m = r * (sy / sx)
    xmean = get_data_mean(biv_coors_x)
    ymean = get_data_mean(biv_coors_y)
    return [[xmean - xmean, round(ymean - xmean * m, 3)], [xmean, round(ymean, 3)],
            [xmean + xmean, round(ymean + xmean * m, 3)]]


def print_statitics(biv_coors_x, biv_coors_y):
    x = biv_coors_x
    y = biv_coors_y
    print('Data mean:          x: {}   y: {}'.format(round(get_data_mean(x), 3),
                                                     round(get_data_mean(y), 3)))
    print('Variance:           x: {}   y: {}'.format(round(get_var(x), 3), round(get_var(y), 3)))
    print('Standard deviation: x: {}   y: {}'.format(round(get_std_dev(get_var(x)), 3),
                                                     round(get_std_dev(get_var(y)), 3)))
    print('Correlation coef.: r = {}'.format(round(get_corr_coef(x, y), 3)))
    lsl_points = least_sqs_line_points(x, y)
    print('Least sqs. points: {}'.format(lsl_points))
    return lsl_points


def plot_least_squares_reg(lsl_points):
    """Argument should be 'print_statistics' output."""
    plt.plot([lsl_points[0][0], lsl_points[1][0], lsl_points[2][0]],
             [lsl_points[0][1], lsl_points[1][1], lsl_points[2][1]], 'r--')


if __name__ == "__main__":
    # For debugging and demonstration; insert data for x and y.
    x = [1, 2, 2, 3]
    y = [1, 2, 3, 6]

    plt.plot(x, y, 'o')
    plt.axis([0, 10, 0, 10])
    plt.show()