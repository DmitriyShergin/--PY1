list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_num = 0
index_max = 0


for i in range(len(list_numbers)):
    if list_numbers[i] > max_num:
        max_num = list_numbers[i]
        index_max = i

list_numbers[index_max], list_numbers[-1] = list_numbers[-1], max_num

print(list_numbers)
