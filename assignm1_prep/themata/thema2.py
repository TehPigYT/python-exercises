def avg_no_extremes(numbers):
    if len(numbers) < 3:
        return None

    numbers.pop(numbers.index(min(numbers)))
    numbers.pop(numbers.index(max(numbers)))

    return sum(numbers) / len(numbers)


numbers = [2, 4, 8, 145, 283, 27, 193, 1784]
print(avg_no_extremes(numbers))
