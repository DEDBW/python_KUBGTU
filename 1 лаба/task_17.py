def find_closest_element_easiest(R, arr):
    if not arr:
        return None

    return min(arr, key=lambda element: abs(element - R))

R = 7.5
array_numbers = [1.2, 4.5, 9.8, 7.9, 6.1]
closest_number = find_closest_element_easiest(R, array_numbers)
print(f"Для числа {R} и массива {array_numbers} самый близкий элемент: {closest_number}")
