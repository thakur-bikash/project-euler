from problem_01 import solve as p1
from problem_02 import solve as p2

# Register problems here as you add more.
# Key = problem number, value = the solve function.
PROBLEMS = {
    1: p1,
    2: p2,
}

# Notes:
# P1 - 1038027th to solve it
# P2 - 826036th to solve it


if __name__ == "__main__":
    for num, solver in PROBLEMS.items():
        print(f"Problem {num:>3}: {int(solver())}")
