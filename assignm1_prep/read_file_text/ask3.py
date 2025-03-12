with open("words.txt", "r") as file:
    contents = file.read().strip()
    print(len(contents.split()))
