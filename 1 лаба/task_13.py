import numpy as np

def quadratic_deviation_mirrored(string):
    if not string:
        return 0

    max_ascii = max(ord(char) for char in string)
    deviations = []
    n = len(string)
    for i in range(n // 2):
        diff = abs(ord(string[i]) - ord(string[n - 1 - i]))
        deviations.append((max_ascii - diff) ** 2)

    return sum(deviations)

def sort_strings_by_quadratic_deviation_mirrored(strings):
    return sorted(strings, key=quadratic_deviation_mirrored)

strings_list_3 = ["level", "rotor", "stats", "window"]
sorted_strings_3 = sort_strings_by_quadratic_deviation_mirrored(strings_list_3)
print("\nОтсортировано по квадратичному отклонению (зеркальные символы):")
for s in sorted_strings_3:
    print(f"'{s}': Квадратичное отклонение (зеркальные) = {quadratic_deviation_mirrored(s)}")