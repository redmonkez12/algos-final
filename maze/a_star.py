from __future__ import annotations

from heapq import heappush, heappop
from typing import TypeVar, Callable, Optional, Generic, Dict

from maze.maze_generator import Maze, MazeLocation

T = TypeVar("T")


class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self._container: list[T] = []

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: T) -> None:
        heappush(self._container, item)

    def pop(self) -> T:
        return heappop(self._container)

    def __repr__(self) -> str:
        return repr(self._container)


class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional[Node], cost: float = 0.0, heuristic: float = 0.0) -> None:
        self.state: T = state
        self.parent: Optional[Node] = parent
        self.cost: float = cost
        self.heuristic: float = heuristic

    def __lt__(self, other: Node) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def astar(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], list[T]], heuristic: Callable[[T], float]) -> Optional[Node[T]]:
    frontier: PriorityQueue[Node[T]] = PriorityQueue()
    frontier.push(Node(initial, None, 0.0, heuristic(initial)))
    explored: Dict[T, float] = {initial: 0.0}

    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            new_cost: float = current_node.cost + 1

            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(child)))
    return None


def manhattan_distance(goal: MazeLocation) -> Callable[[MazeLocation], float]:
    def distance(ml: MazeLocation) -> float:
        xdist: int = abs(ml.column - goal.column)
        ydist: int = abs(ml.row - goal.row)

        return (xdist + ydist)
    return distance


def node_to_path(node: Node[T]) -> list[T]:
    path: list[T] = [node.state]
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path


if __name__ == "__main__":
    m = Maze(rows=30, columns=30, goal=MazeLocation(29, 29))
    distance: Callable[[MazeLocation], float] = manhattan_distance(m.goal)
    solution: Optional[Node[MazeLocation]] = astar(m.start, m.goal_test, m.successors, distance)

    if solution is None:
        print("No solution found using A*!")
    else:
        path3: list[MazeLocation] = node_to_path(solution)
        m.mark(path3)
        print(m)
