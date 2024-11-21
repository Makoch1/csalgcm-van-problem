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

def get_points(n: int) -> List[tuple[int, int]]:
    points = []

    for i in range(n):
        print(f"\nDrop off point #{i + 1}")

        # absolutely no error checking
        x = int(input("Enter x coordinate: "))
        y = int(input("Enter y coordinate: "))

        points.append((x, y))

    return points

def get_start_point() -> tuple[int, int]:
    print("Enter starting point")

    x = int(input("Enter x coordinate: "))
    y = int(input("Enter y coordinate: "))

    return (x, y)
