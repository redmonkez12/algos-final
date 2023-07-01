maze = [
    "xxxxxxxxxx x",  # 0
    "x        x x",  # 1
    "x        x x",  # 2
    "x xxxxxxxx x",  # 3
    "x          x",  # 4
    "x xxxxxxxxxx",  # 5
]  # 01234567891011


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x} {self.y}"


direction = [
    [-1, 0],
    [0, -1],
    [1, 0],
    [0, 1],
]


# end bude point
# curr je point

def walk(maze, wall, curr, end, seen, path):
    # Jdu do zdi
    if maze[curr.y][curr.x] == wall:
        return False

    # Jdu mimo mapu
    if curr.x < 0 or curr.x >= len(maze[0]) or curr.y < 0 or curr.y >= len(maze):
        return False

    # jsem v cili
    if curr.x == end.x and curr.y == end.y:
        path.append(end)
        return True

    # uz jsem tam byl
    if seen[curr.y][curr.x]:
        return False

    seen[curr.y][curr.x] = True
    path.append(curr)

    for dir in direction:
        x, y = dir

        if walk(maze,wall, Point(curr.x + x, y + curr.y), end, seen, path):
            return True

    path.pop()

    return False


def solve(maze, wall, start, end):
    seen = []
    path = []

    for _ in maze:
        seen.append([False] * len(maze[0]))

    print(seen)
    walk(maze, wall, start, end, seen, path)

    return path


result = solve(maze, "x", Point(10, 0), Point(1, 5))
print(result)


def draw_path(maze, path):
    data = list(map(lambda row: list(row), maze))

    for point in path:
        if data[point.y][point.x]:
            data[point.y][point.x] = "O"

    return list(map(lambda row: "".join(row), data))


maze_with_path = draw_path(maze, result)
for row in maze_with_path:
    print(row)