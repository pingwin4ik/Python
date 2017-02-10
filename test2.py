def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def multiply(numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total


if __name__ == "__main__":
    print sum([4, 5, 3, 4])
    print multiply([5, 4, 3, 4])
