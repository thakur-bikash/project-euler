def solve(target=4_000_000):
    """Sum of even-valued Fibonacci terms not exceeding target."""
    prev, current = 1, 2
    count_sum = 0

    while current <= target:
        if current % 2 == 0:
            count_sum += current
        next_term = prev + current
        prev = current
        current = next_term

    return count_sum


if __name__ == "__main__":
    print(solve())
