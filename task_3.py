def delete(list_, index=-1):
    if index < 0:
        index = len(list_)+index
    if index >= len(list_) or index < 0:
        return list_
    half_1 = list_[0:index]
    half_2 = list_[(index+1):]
    new_list = half_1
    for i in range(len(half_2)):
        new_list.append(half_2[i])
    return new_list


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
