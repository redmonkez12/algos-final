from enum import Enum


class Direction(Enum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"


class Snake:
    def __init__(self, width: int, height: int, food: list[list[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.snake = [[0, 0]]
        self.score = 0

    def move(self, direction: Direction) -> int:
        directions = {Direction.UP: (-1, 0), Direction.DOWN: (1, 0), Direction.LEFT: (0, -1), Direction.RIGHT: (0, 1)}
        curr_head = self.snake[0]
        row, col = directions[direction]
        new_head = [curr_head[0] + row, curr_head[1] + col]

        if new_head[0] < 0 or new_head[0] >= self.height or new_head[1] < 0 or new_head[1] >= self.width:
            return -1

        for i in range(1, len(self.snake)):
            if new_head == self.snake[i]:
                return -1

        if len(self.food) and new_head == self.food[0]:
            self.score += 1
            self.food.pop(0)
        else:
            self.snake.pop()

        self.snake.insert(0, new_head)

        return self.score

    def print_board(self) -> None:
        print("-" * (2 * self.width + 1))
        board = [[" " for _ in range(self.width)] for _ in range(self.height)]

        if food:
            board[food[0][0]][food[0][1]] = "F"

        for segment in self.snake:
            board[segment[0]][segment[1]] = "S"

        for row in board:
            print("|" + "|".join(row) + "|")

        print("-" * (2 * self.width + 1))


width = 10
height = 10
food = [[1, 2], [0, 1], [3, 3], [5, 6]]

snake = Snake(width, height, food)

snake.print_board()
print(snake.move(Direction.RIGHT))
snake.print_board()
print(snake.move(Direction.DOWN))
snake.print_board()
print(snake.move(Direction.RIGHT))
snake.print_board()
print(snake.move(Direction.UP))
snake.print_board()
print(snake.move(Direction.LEFT))
snake.print_board()
