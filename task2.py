my_list = [5, 22, 33, 8, 9, 2, 4, 12]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список: {my_list}')
print(f'Новый список: {my_new_list}')