from collections import Counter

def create_squared_list_simple(numbers):
    counts = Counter(numbers)
    squared_list = []

    for number in numbers:
        if number >= 0 and number < 100 and counts[number] > 2:
            if number not in squared_list:
                squared_list.append(number**2)

    return squared_list

input_list = [1, 2, 3, 4, 4, 4, 5, 5, 5, 6, 6, -1, -2, 9, 9, 9, 99, 99, 99, 100, 100, 100]
result_list = create_squared_list_simple(input_list)
print(f"Исходный список: {input_list}")
print(f"Новый список квадратов: {result_list}")