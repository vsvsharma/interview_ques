"""
Program to sort the dictionary in an ascending order.
"""
def insertion_sort_dict_by_values(input_dict):
    items = list(input_dict.items())

    for i in range(1, len(items)):
        key, value = items[i]
        j = i - 1
        while j >= 0 and value < items[j][1]:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = (key, value)

    sorted_dict = dict(items)

    return sorted_dict

original_dict = {'a': 5, 'b': 2, 'c': 8, 'd': 1}
ascending_result = insertion_sort_dict_by_values(original_dict)

print("Original Dictionary:", original_dict)
print("Sorted Dictionary (Ascending):", ascending_result)
