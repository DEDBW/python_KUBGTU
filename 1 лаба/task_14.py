from collections import Counter

def quadratic_deviation_frequency(strings, string):
    if not strings or not string:
        return 0

    total_counts = Counter()
    for s in strings:
        total_counts.update(s)

    most_common_char = total_counts.most_common(1)[0][0]

    string_counts = Counter(string)
    string_char_frequency = string_counts.get(most_common_char, 0) / len(string) if string else 0

    total_char_frequency = total_counts.get(most_common_char, 0) / sum(total_counts.values()) if sum(total_counts.values()) else 0


    return (total_char_frequency - string_char_frequency) ** 2

def sort_strings_by_quadratic_deviation_frequency(strings):
    return sorted(strings, key=lambda s: quadratic_deviation_frequency(strings, s))

strings_list_4 = ["apple", "banana", "apricot", "grape"]
sorted_strings_4 = sort_strings_by_quadratic_deviation_frequency(strings_list_4)

print("\nОтсортировано по квадратичному отклонению (частота символов):")
for s in sorted_strings_4:
    dev = quadratic_deviation_frequency(strings_list_4, s)
    print(f"'{s}': Квадратичное отклонение (частота) = {dev:.5f}")