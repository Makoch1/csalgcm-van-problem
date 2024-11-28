from helpers import get_distance, get_points, get_start_point
from typing import List

def solve_by_greedy(points: List[tuple[float, float]]) -> List[int]:
    n_points = len(points)

    # both visited and sequence are initialized with the start index alr in
    visited = {0} # set of visited nodes. implemented as set bc O(1) lookup
    order = [0] # order

    while len(visited) < n_points:
        nearest_distance = -1 # distance can never be -1 bc of square
        nearest_index = -1

        # find the nearest point to the current point
        curr_index = points[order[-1]] # get last elemen of order
        for i in range(n_points):
            if i in visited: # if alr visited, skip
                continue

            distance = get_distance(curr_index, points[i])

            # if no nearest distance yet, or distance is shorter than nearest distance
            if nearest_distance == -1 or nearest_distance > distance:
                nearest_distance = distance
                nearest_index = i

        order.append(nearest_index)

        # visit
        visited.add(nearest_index)

    return order + [0] # add the start index to the end of the order

