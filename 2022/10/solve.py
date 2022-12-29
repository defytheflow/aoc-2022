from pathlib import Path


class CustomStopError(Exception):
    pass


def solve_one(data: str) -> int:
    CYCLES = (20, 60, 100, 140, 180, 220)

    x = 1
    cycle = 0
    total = 0

    def next_cycle(count: int | None = None) -> None:
        nonlocal x, cycle, total
        cycle += 1

        if cycle in CYCLES:
            total += x * cycle

        if count is not None:
            x += count

        if cycle == CYCLES[-1]:
            raise CustomStopError

    for command in data.split("\n"):
        command = command.rstrip("\n")
        try:
            if command == "noop":
                next_cycle()
            else:
                count = int(command.split(" ")[-1])
                next_cycle()
                next_cycle(count)
        except CustomStopError:
            return total

    raise AssertionError("This should never happen")


def solve_two(data: str) -> None:
    x = 1
    cycle = 0
    pixel = 0

    def next_cycle(count: int | None = None) -> None:
        nonlocal x, cycle, pixel
        cycle += 1

        if x - 1 <= pixel <= x + 1:
            print("#", end="")
        else:
            print(".", end="")

        pixel += 1

        if count is not None:
            x += count

        if cycle > 0 and cycle % 40 == 0:
            print()
            pixel = 0

        if cycle == 240:
            raise CustomStopError

    for command in data.split("\n"):
        command = command.rstrip("\n")
        try:
            if command == "noop":
                next_cycle()
            else:
                count = int(command.split(" ")[1])
                next_cycle()
                next_cycle(count)
        except CustomStopError:
            pass


if __name__ == "__main__":
    data = (Path(__file__).parent / "input.txt").read_text().strip()

    solution_one = solve_one(data)
    print(solution_one)
    assert solution_one == 15140

    solution_two = solve_two(data)
    # print(solution_two)
    # assert solution_two == ...
