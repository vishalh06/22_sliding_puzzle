import time
from puzzle import Puzzle


class SlidingPuzzle:
    def __init__(self, size=4):
        if size not in (3, 4, 5):
            raise ValueError("Board size must be 3, 4, or 5.")

        self.size = size
        self.puzzle = Puzzle(self.size)
        self.moves = 0
        self.started = time.monotonic()
        self.completed = False
        self.finished = None

    def recreate_board(self):
        if self.completed:
            return False
        self.puzzle = Puzzle(self.size)
        return True

    def elapsed(self):
        end = self.finished if self.finished is not None else time.monotonic()
        return end - self.started

    def display(self):
        print()
        for row in self.puzzle.board:
            print(" ".join(f"{x or ' ':>2}" for x in row))
        print("Moves:", self.moves, " Time:", int(self.elapsed()), "s")

    def finish_if_solved(self):
        if not self.completed and self.puzzle.solved():
            self.completed = True
            self.finished = time.monotonic()
        return self.completed

    def run(self):
        if self.completed:
            print("This puzzle is already completed.")
            return

        print(f"Sliding Puzzle — {self.size}x{self.size}")
        print("W/A/S/D moves the blank. Q quits.")
        print("R recreates the board; session moves and time continue.")

        while True:
            self.finish_if_solved()
            self.display()

            if self.completed:
                print("Solved!")
                return

            key = input("> ").strip().lower()
            if key == "q":
                return
            if key == "r":
                self.recreate_board()
                print("Board recreated. Session moves and time retained.")
                continue
            if key not in "wasd":
                print("Use W/A/S/D, R, or Q.")
                continue
            if self.puzzle.move(key):
                self.moves += 1
            else:
                print("That move is not possible.")