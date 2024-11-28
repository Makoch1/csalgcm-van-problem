from helpers import get_distance, get_points, get_start_point
from itertools import permutations
from typing import List

def solve_by_bruteforce(points: List[tuple[float, float]]) -> List[int]:
    # get list of all permutations
    order_permutations = [list(x) for x in permutations(range(len(points)))]

    # for all permutations, calculate the distance, and keep track of the shortest distance
    shortest_distance = None
    shortest_order = []
    for order in order_permutations:
        curr_distance = 0

        # calculate distance from start node / point / terminal to the first point in the permutation
        curr_distance += get_distance(points[0], points[order[0]])

        # calculates from i to i + 1 to i + 2, so on so forth
        for i in range(len(order) - 1): # not a for each cuz i need the index to access next element
            curr_point = points[order[i]]
            next_point = points[order[i + 1]]

            curr_distance += get_distance(curr_point, next_point)

        # calculate distance from last node to start node
        curr_distance += get_distance(points[order[-1]], points[0])

        # if current is shorter than current shortest, swap em
        if (shortest_distance == None or shortest_distance > curr_distance):
            shortest_distance = curr_distance
            shortest_order = order

    return shortest_order + [0] # add the start point back

