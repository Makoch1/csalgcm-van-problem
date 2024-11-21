from helpers import get_distance, get_points, get_start_point

def main():
    start_point = get_start_point()
    n_points = int(input("Enter amount of points / drop-offs"))
    points = get_points(n_points)

    # both visited and sequence are initialized with the start_point alr in
    visited = {start_point} # set of visited nodes. implemented as set bc O(1) lookup

    total_distance = 0.0 # total distance of the sequence
    sequence = [start_point] # sequence, list of tuples

    # while there are points to be visited still
    while len(visited) < n_points + 1: # number of points + the start point
        nearest_distance = -1 # distance can never be -1 bc of square
        nearest_point = (-1, -1) # default value to shut the warnings up

        curr_point = sequence[-1] # get last elemen of sequence
        # find the nearest point to the current point
        for point in points:
            if point in visited: # if alr visited, skip
                continue

            distance = get_distance(curr_point, point)

            # if no nearest distance yet, or distance is shorter than nearest distance
            if nearest_distance == -1 or nearest_distance > distance:
                nearest_distance = distance
                nearest_point = point

        # add the distance and point to the running total
        total_distance += nearest_distance
        sequence.append(nearest_point)

        # visit
        visited.add(nearest_point)

    # calculate from last point back to the start point
    total_distance += get_distance(sequence[-1], start_point)
    sequence.append(start_point)

    # print off the calculated sequence and distance
    print(sequence)
    print(total_distance)

if __name__ == "__main__":
    main()

