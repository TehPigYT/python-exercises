import random

def gen_dice_results():
    my_list = []
    frequency = [0, 0, 0, 0, 0, 0]
    for x in range(10):
        num = random.randint(1, 6)
        my_list.append(num)
        frequency[num - 1] = frequency[num - 1] + 1

    print(my_list)

    for num in range(6):
        print(f"Times {num + 1} appeared: {frequency[num]}")

gen_dice_results()