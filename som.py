import numpy as np
import matplotlib.pyplot as plt
from minisom import MiniSom
from typing import List

def solve_by_som(x: List[float], y: List[float], visualize=True) -> List[int]:
    """
    TSP using SOM. Instead of taking a list of points, takes in a list of x coordinates, 
    and a list of y coords, where a point is (x[0], y[0]). This is bc its easier to plot using matplotlib.
    This returns a list of indices that represents the path / order. (e.g., [0, 2, 4, 3, 1, 0])

    Args:
        visualize (bool): determines whether to visualize the iterations of som. Defaults to True 
        x: list of x coords
        y: list of y coords

    Returns: List of indices representing the order / path
    """
    N_neurons = len(x) * 2 # n neurons is number of points * 2
    points = np.array([x,y]).T

    som = MiniSom(1, N_neurons*2, 2, sigma=10,
                  neighborhood_function='gaussian', random_seed=50)
    max_iter = 1000
    som.pca_weights_init(points)

    last_order = [] # previous order / path
    for i in np.arange(max_iter):
        i_point = i % len(points)
        som.update(points[i_point], som.winner(points[i_point]), i, max_iter)
        visit_order = np.argsort([som.winner(p)[1] for p in points])
        visit_order = np.concatenate((visit_order, [visit_order[0]]))

        # this is so it doesnt display if there are no changes to the path
        if visualize and len(last_order) != 0 and not np.array_equiv(visit_order, last_order):
            path_x = [points[i][0] for i in visit_order]
            path_y = [points[i][1] for i in visit_order]

            plt.clf() # clears the graph
            plt.scatter(x, y) # plots the points / drop-offs
            plt.plot(path_x, path_y, 'C3', linewidth=2, label='path') # plots the line path
            plt.title(f'Iteration #{i}')
            plt.pause(0.1)

        # update last order
        last_order = visit_order

    plt.close()
    return last_order

