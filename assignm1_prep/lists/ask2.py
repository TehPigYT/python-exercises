def check_numbers(input):
    numbers = [int(x) for x in input.split(" ")]
    if len(numbers) != 7:
        return print(
            "You have entered the wrong amount of numbers or the format is invalid."
        )

    print(max(numbers), min(numbers))
    print(sum(numbers))


info = input("Enter 7 numbers seperated by space: ")
check_numbers(info)
