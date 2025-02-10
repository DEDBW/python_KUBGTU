def task_10():
    print("Введите строки (пустая строка для завершения ввода):")
    lines = []

    while True:
        line = input("Введите строку: ")
        if line == "":
            break
        lines.append(line)

    sorted_lines = sorted(lines, key=lambda x: len(x.split()))

    print("\nСтроки, отсортированные по количеству слов:")
    for s in sorted_lines:
        print(s)

task_10()