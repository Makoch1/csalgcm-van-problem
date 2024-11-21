from helpers import get_distance, get_points

def main():
    n_drops = int(input("Enter amount of drop off points: "))
    drops = get_points(n_drops)

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

if __name__ == "__main__":
    main()
