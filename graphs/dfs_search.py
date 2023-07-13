import random

import networkx as nx

from deps import plt_error
from graphs.intro import Stack
from graphs.maze import Maze, to_networkx, solution_graph, node_from_field


def dfs_search(G, src):
    marked = {}
    node_from = {}

    stack = Stack()

    marked[src] = True
    stack.push(src)

    while not stack.is_empty():
        v = stack.pop()

        for w in G[v]:
            if w not in marked:
                node_from[w] = v
                marked[w] = True
                stack.push(w)

    return node_from


def path_to(node_from, src, target):
    if target not in node_from:
        raise ValueError("Unreachable")

    path = []
    v = target
    while v != src:
        path.append(v)
        v = node_from[v]

    path.append(src)
    path.reverse()

    return path


def draw_solution(G, field, src, target, figsize=(12, 6)):
    """
    Use matplotlib to draw the original graph containing the solution to
    a designated target vertex; in the second graph the node_from dictionary
    is visualized.
    """
    if plt_error:
        return
    import matplotlib.pyplot as plt

    H = solution_graph(G, path_to(field, src, target))
    F = node_from_field(G, field)

    _, axes = plt.subplots(nrows=1, ncols=2, figsize=figsize)
    ax = axes.flatten()

    # get original positional location from original graph
    pos_h = nx.get_node_attributes(H, 'pos')
    nx.draw(H, pos_h, with_labels=True, node_color='w', font_size=8, ax=ax[0])
    pos_f = nx.get_node_attributes(F, 'pos')
    nx.draw(F, pos_f, with_labels=True, node_color='w', font_size=8, ax=ax[1])


if __name__ == "__main__":
    random.seed(15)
    m = Maze(3, 5)  # Anything bigger and these are too small to read
    graph = to_networkx(m)

    # Choose whether to use dfs_search, bfs_search, or guided_search
    draw_solution(graph, dfs_search(graph, m.start()), m.start(), m.end())

    import matplotlib.pyplot as plt
    plt.show()
