import matplotlib.pyplot as plt
from math import sqrt
from typing import List

def get_distance(point_x: tuple, point_y: tuple) -> float:
    """
    Takes two tuples that represent a coordinate (x, y), 
    and calculates the euclidian distance between them.

    Args:
        point_x: First tuple / point / coordinate
        point_y: Second tuple / point / coordinate

    Returns:
        Euclidian distance float
    """
    x_diff = point_x[0] - point_y[0]
    y_diff = point_x[1] - point_y[1]

    return sqrt( x_diff**2 + y_diff**2 )

def get_points_from_user(n=10) -> tuple[List[float], List[float]]:
    x_points = []
    y_points = []

    # set the limit of the graph
    plt.xlim(0, 50)
    plt.ylim(0, 50)

    # ask the user for the rest of the points
    for i in range(n):
        title = 'Enter the starting point (Shuttle terminal)' if i == 0 else f'Enter the {n - i} remaining points'

        plt.title(title, fontweight="bold")
        plt.scatter(x_points, y_points)
        input_point = plt.ginput(1)[0]

        x_points.append(input_point[0])
        y_points.append(input_point[1])

    return (x_points, y_points)

def generate_path_plot(x: List[float], y: List[float], order: List[int], alg_name: str, subplot):
    """
    Displays the points, and the path suggested by the algorithm. Also calculates the
    total distance of the path. x and y are split into two, instead of being one list
    of points (like (x, y)) because matplotlib takes them separately.

    Args:
        x: list of x coordinates of the points
        y: list of y coordinates of the points
        order: list of indexes that signify the order / path
        alg_name: name of the algorithm (for the graph title)
        subplot: subplot to place the generated plot in
    """
    path_x = [x[i] for i in order]
    path_y = [y[i] for i in order]

    # calculates the total distance of the path
    distance = 0
    for i in range(len(order) - 1):
        curr_i = order[i]
        next_i = order[i + 1]

        curr_point = (x[curr_i], y[curr_i])
        next_point = (x[next_i], y[next_i])

        distance += get_distance(curr_point, next_point)

    # generate graph
    subplot.set_title(f'Best path ({alg_name}), total distance = {distance:.2f}')
    subplot.scatter(x, y, label='point to visit')
    subplot.plot(path_x, path_y, 'C3', linewidth=2, label='path')

    # label, and color the start point
    subplot.scatter(x[0], y[0], color='deeppink', s=5)
    subplot.annotate(
        "START POINT", 
        (x[0], y[0]),
        xytext=(-20, 5),
        textcoords='offset points',
    )

