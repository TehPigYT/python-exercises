import random


def gen_list():
    num_list = []
    for x in range(10):
        num_list.append(random.randint(1, 100))

    return num_list


def keep_even(my_list):
    new_list = []
    for x in my_list:
        if x % 2 == 1:
            new_list.append(x)

    return new_list


my_list = gen_list()
new_list = keep_even(my_list)
print(my_list, new_list)
