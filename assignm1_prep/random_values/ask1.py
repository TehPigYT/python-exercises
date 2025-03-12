import random


def gen_num_list_avg():
    my_list = []
    for x in range(5):
        my_list.append(random.randint(1, 50))

    return sum(my_list) / 5


print(gen_num_list_avg())
