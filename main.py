from game import SlidingPuzzle


def main():
    while True:
        choice = input(
            "Choose board size: 3, 4, or 5 (Enter for 4; Q quits): "
        ).strip().lower()

        if choice == "q":
            return
        if choice == "":
            choice = "4"
        if choice in ("3", "4", "5"):
            SlidingPuzzle(int(choice)).run()
            return

        print("Please enter 3, 4, or 5.")


if __name__ == "__main__":
    main()