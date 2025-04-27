import sys


def main():
    if len(sys.argv) != 4:
        print("More or less values given, exiting...")
        return

    if (
        not str.isdigit(sys.argv[1])
        or not str.isdigit(sys.argv[2])
        or not str.isdigit(sys.argv[3])
    ):
        print("One or more values are not numbers, exiting...")
        return

    res = (int(sys.argv[1]) + int(sys.argv[2]) + int(sys.argv[3])) / 3
    print(f"Average: {res}")


if __name__ == "__main__":
    main()
