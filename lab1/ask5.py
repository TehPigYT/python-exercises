def input_text():
    while True:
        text = input("Enter a text: ")
        formatted_text = text.replace(" ", "")

        final_text = formatted_text[::-1]

        print(final_text)
        break


input_text()