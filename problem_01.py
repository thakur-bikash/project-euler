def solve(target=999):
    """Sum of all multiples of 3 and 5 below target."""

    def sum_of_multiples(mult, num):
        return num * (mult * (mult + 1)) / 2

    mult3  = int(target / 3)
    mult5  = int(target / 5)
    mult15 = int(target / 15)

    return sum_of_multiples(mult3, 3) + sum_of_multiples(mult5, 5) - sum_of_multiples(mult15, 15)


if __name__ == "__main__":
    print(int(solve()))
