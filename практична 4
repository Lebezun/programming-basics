def remove_duplicates(input_list):
    return list(set(input_list))

def sort_list(input_list):
    numbers = [item for item in input_list if isinstance(item, (int, float))]
    strings = [item for item in input_list if isinstance(item, str)]
    numbers.sort()
    strings.sort()
    return numbers + strings

original_list = [3, 1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']
unique_list = remove_duplicates(original_list)
sorted_list = sort_list(unique_list)

print("Унікальний і відсортований список:", sorted_list)
