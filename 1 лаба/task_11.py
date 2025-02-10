def average_ascii_value(string):
    ascii_values = [ord(char) for char in string]
    return sum(ascii_values) / len(ascii_values) if string else 0

def sort_strings_by_average_ascii(strings):
    return sorted(strings, key=average_ascii_value)

strings_list_1 = ["zebra", "apple", "Banana", "kiwi"]
sorted_strings_1 = sort_strings_by_average_ascii(strings_list_1)
print("Отсортировано по среднему значению ASCII:")
for s in sorted_strings_1:
    print(f"'{s}': Среднее ASCII = {average_ascii_value(s):.2f}")