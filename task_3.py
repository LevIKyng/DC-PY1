def get_unique_list_numbers() -> list[int]:
    from random import randint
    list_ = []
    while len(list_) != 15:
        for i in range(15):
            i = randint(-10, 10)
        if i in list_:
            continue
        else:
            list_.append(i)
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
