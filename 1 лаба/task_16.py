def find_two_smallest_elements_simple(arr):
    if len(arr) < 2:
        return None

    sorted_arr = sorted(arr)
    return sorted_arr[0], sorted_arr[1]

array1 = [5, 1, 9, 3, 7, -2, 8]
two_smallest1 = find_two_smallest_elements_simple(array1)
print(f"Для массива {array1} два наименьших элемента: {two_smallest1}")