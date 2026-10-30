import random


class Puzzle:
    def __init__(self, size=4):
        self.size = size
        self.board = self.make_board()

    def make_board(self):
        tiles = list(range(1, self.size * self.size)) + [0]
        board = [
            tiles[r * self.size:(r + 1) * self.size]
            for r in range(self.size)
        ]

        blank_r = self.size - 1
        blank_c = self.size - 1
        previous_blank = None

        for _ in range(self.size * self.size * 40):
            neighbours = [
                (r, c)
                for r, c in (
                    (blank_r - 1, blank_c),
                    (blank_r + 1, blank_c),
                    (blank_r, blank_c - 1),
                    (blank_r, blank_c + 1),
                )
                if 0 <= r < self.size and 0 <= c < self.size
                and (r, c) != previous_blank
            ]

            next_r, next_c = random.choice(neighbours)
            board[blank_r][blank_c], board[next_r][next_c] = (
                board[next_r][next_c], board[blank_r][blank_c]
            )
            previous_blank = (blank_r, blank_c)
            blank_r, blank_c = next_r, next_c

        if sum(board, []) == tiles:
            board[blank_r][blank_c], board[blank_r - 1][blank_c] = (
                board[blank_r - 1][blank_c], board[blank_r][blank_c]
            )

        return board

    def blank_pos(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == 0:
                    return r, c

    def move(self, direction):
        directions = {
            "w": (-1, 0),
            "s": (1, 0),
            "a": (0, -1),
            "d": (0, 1),
        }

        if direction not in directions:
            return False

        r, c = self.blank_pos()
        dr, dc = directions[direction]
        nr, nc = r + dr, c + dc

        if not (0 <= nr < self.size and 0 <= nc < self.size):
            return False

        self.board[r][c], self.board[nr][nc] = (
            self.board[nr][nc], self.board[r][c]
        )
        return True

    def solved(self):
        return sum(self.board, []) == list(range(1, self.size * self.size)) + [0]
