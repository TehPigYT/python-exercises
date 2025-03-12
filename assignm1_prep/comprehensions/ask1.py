def return_filtered_num():
    list = [i * i for i in range(1, 21)]
    print(list)

    new_list = [i for i in list if i % 2 == 1]
    return new_list


print(return_filtered_num())
