list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max = 0

for a in range(len(list_numbers)):
    max_num = list_numbers[max]
    current = list_numbers[a]
    if current > max_num:
        max = a

list_numbers[max], list_numbers[-1] = list_numbers[-1], list_numbers[max]

print(list_numbers)
