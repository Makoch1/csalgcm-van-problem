from helpers import get_distance, get_points, get_start_point
from itertools import permutations

def main():
    start_point = get_start_point()
    n_points = int(input("Enter amount of points / drop-offs: "))
    points = get_points(n_points)

    # get list of all permutations
    sequence_permutations = [list(x) for x in permutations(points)]

    # for all permutations, calculate the distance, and keep track of the shortest distance
    shortest_distance = None
    shortest_distance_index = 0

    for index, sequence in enumerate(sequence_permutations):
        curr_distance = 0

        # calculate distance from start node / point / terminal to the first point in the permutation
        curr_distance += get_distance(start_point, sequence[0])

        # calculates from i to i + 1 to i + 2, so on so forth
        for i in range(len(sequence) - 1): # not a for each cuz i need the index to access next element
            point = sequence[i]
            next_point = sequence[i + 1]

            curr_distance += get_distance(point, next_point)

        # calculate distance from last node to start node
        curr_distance += get_distance(sequence[len(sequence) - 1], start_point)

        # if current is shorter than current shortest, swap em
        if (shortest_distance == None or shortest_distance > curr_distance):
            shortest_distance = curr_distance
            shortest_distance_index = index

    print(sequence_permutations[shortest_distance_index])
    print(shortest_distance)

if __name__ == "__main__":
    main()
