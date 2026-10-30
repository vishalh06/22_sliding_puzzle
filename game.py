import time
from puzzle import Puzzle


class SlidingPuzzle:
    def __init__(self):
        self.size = 4
        self.puzzle = Puzzle(self.size)
        self.moves = 0
        self.started = time.monotonic()
        self.completed = False
        self.finished = None

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

        print("Sliding Puzzle — W/A/S/D moves the blank. Q quits.")
        while True:
            self.finish_if_solved()
            self.display()

            if self.completed:
                print("Solved!")
                return

            key = input("> ").strip().lower()
            if key == "q":
                return
            if key not in "wasd":
                print("Use W/A/S/D.")
                continue
            if self.puzzle.move(key):
                self.moves += 1
            else:
                print("That move is not possible.")