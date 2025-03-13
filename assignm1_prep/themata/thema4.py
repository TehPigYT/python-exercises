def read_file():
    with open("sample_in.txt", "r") as file:
        contents = file.read().strip()

        filtered = [i.upper() for i in contents.split() if len(i) > 5]
        return filtered


def save_file(words):
    with open("sample_out.txt", "w") as file:
        file.write("\n".join(words))

words = read_file()
save_file(words)