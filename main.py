import math

def main():
    drops = []
    n_drops = int(input("Enter amount of drop off points: "))

    for i in range(n_drops):
        print(f"\nDrop off point #{i + 1}")

        # absolutely no error checking
        x = int(input("Enter x coordinate: "))
        y = int(input("Enter y coordinate: "))

        drops.append((x, y))

    # actually calculating the path
    # ASSUME: that the first given "drop off" is the home-base of the van

    sequence = [0]
    curr = 0
    # when alg is done, sequence would be filled with all the drop off points
    while len(sequence) != n_drops:
        shortest_drop = curr
        shortest_distance = None

        # check every other node, find the one with the shortest distance
        for i, drop in enumerate(drops):
            # make sure we're not comparing same drop OR going somewhere we've been already
            if drop == drops[curr] or i in sequence:
                continue

            dist = get_distance(drops[curr], drop)

            if shortest_distance == None or dist < shortest_distance:
                shortest_distance = dist
                shortest_drop = i

        # visit the drop off
        curr = shortest_drop
        sequence.append(curr)

    print(sequence)

def get_distance(point_x: tuple, point_y: tuple) -> float:
    x_diff = point_x[0] - point_y[0]
    y_diff = point_x[1] - point_y[1]

    return math.sqrt( x_diff**2 + y_diff**2 )

if __name__ == "__main__":
    main()
