def task_9():
    print("Введите строки (пустая строка для завершения ввода):")
    lines = []
    while True:
        line = input("Введите строку: ")
        if line == "":
            break
        lines.append(line)

    sorted_lines = sorted(lines, key=len)

    print("\nСтроки, отсортированные по длине:")
    for s in sorted_lines:
        print(s)

task_9()