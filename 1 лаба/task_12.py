import statistics

def median_ascii_value(string):
    ascii_values = [ord(char) for char in string]
    return statistics.median(ascii_values) if string else 0

def sort_strings_by_median_ascii(strings):
    return sorted(strings, key=median_ascii_value)

strings_list_2 = ["zebra", "apple", "Banana", "kiwi"]
sorted_strings_2 = sort_strings_by_median_ascii(strings_list_2)
print("\nОтсортировано по медианному значению ASCII:")
for s in sorted_strings_2:
    print(f"'{s}': Медиана ASCII = {median_ascii_value(s)}")