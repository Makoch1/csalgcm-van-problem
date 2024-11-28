from som import solve_by_som
from greedy import solve_by_greedy
from brute import solve_by_bruteforce
from helpers import get_points_from_user, generate_path_plot
import matplotlib.pyplot as plt

def main():
    x_list, y_list = get_points_from_user()
    points = [(x, y) for x, y in zip(x_list, y_list)]

    som_order = solve_by_som(x_list, y_list, visualize=False)
    print("Done with som!")

    greedy_order = solve_by_greedy(points)
    print("Done with greedy!")

    bruteforce_order = solve_by_bruteforce(points)
    print("Done with brute force!")

    fig, (sp1, sp2, sp3) = plt.subplots(1, 3)
    generate_path_plot(x_list, y_list, som_order, "som", sp1)
    generate_path_plot(x_list, y_list, greedy_order, "greedy", sp2)
    generate_path_plot(x_list, y_list, bruteforce_order, "brute force", sp3)

    fig.set_size_inches(15, 5)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

