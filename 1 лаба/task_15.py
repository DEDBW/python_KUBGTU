def find_unique_element(arr):
    if arr[0] == arr[1]:
        different_element = arr[0]
        for element in arr:
            if element != different_element:
                return element
    else:
        if arr[0] == arr[2]:
            return arr[1]
        else:
            return arr[0]

array1 = [1, 1, 2, 1, 1]
unique_element1 = find_unique_element(array1)
print(f"Для массива {array1} уникальный элемент: {unique_element1}")

array2 = [5, 6, 5, 5, 5]
unique_element2 = find_unique_element(array2)
print(f"Для массива {array2} уникальный элемент: {unique_element2}")

array3 = [10, 10, 10, 9, 10]
unique_element3 = find_unique_element(array3)
print(f"Для массива {array3} уникальный элемент: {unique_element3}")

array4 = [2, 1, 1, 1, 1]
unique_element4 = find_unique_element(array4)
print(f"Для массива {array4} уникальный элемент: {unique_element4}")

array5 = [1, 2, 1, 1, 1]
unique_element5 = find_unique_element(array5)
print(f"Для массива {array5} уникальный элемент: {unique_element5}")