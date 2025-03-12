with open("sample_in.txt", "r") as file:
    contents = file.read().strip()

    filtered = [i.upper() for i in contents.split() if len(i) > 5]
    print(filtered)
