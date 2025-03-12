def fun(a_list, threshold):
    new_list = []
    for x in a_list:
        if x > threshold:
            new_list.append(x)

    return new_list


a_list = [4, 7, 12, 1, 154, 54, 27, 6954]
print(fun(a_list, 50))
