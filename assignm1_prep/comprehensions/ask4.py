numbers = {"a": 10, "b": 25, "c": 33, "d": 47, "e": 50}
new_num = {key: value for key, value in numbers.items() if value > 30}
print(new_num)
