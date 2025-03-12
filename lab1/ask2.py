def count_word_length():
    string = "How I want a drink alcoholic of course after the heavy lectures involving quantum mechanics"
    for word in string.split():
        print(word, len(word))


count_word_length()
