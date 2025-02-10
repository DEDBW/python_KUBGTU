def get_unique_positive_divisors_easy(numbers):
    unique_divisors = set()
    for number in numbers:
        if isinstance(number, (int, float)) and number > 0:
            divisors = {i for i in range(1, number + 1) if number % i == 0}
            unique_divisors.update(divisors)

    return sorted(list(unique_divisors))

positive_numbers = [12, 25, 12, 30, 8]
divisors_list = get_unique_positive_divisors_easy(positive_numbers)
print(f"Для списка чисел {positive_numbers} уникальные положительные делители: {divisors_list}")
