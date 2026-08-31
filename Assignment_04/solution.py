def calculate_average(numbers):
    """Calculates and returns the average of a list of numbers."""
    return sum(numbers) / len(numbers)


def main():
    numbers = []

    print("Please enter five numbers:")
    for i in range(1, 6):
        num = float(input(f"Enter number {i}: "))
        numbers.append(num)

    avg = calculate_average(numbers)

    print(f"\nThe average of the five numbers is: {avg}")


if __name__ == "__main__":
    main()
