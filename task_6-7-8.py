def solve_task_6():
    s = input("Введите строку для задачи 6: ")
    max_count = 0
    current_count = 0
    for c in s:
        if ('а' <= c <= 'я') or ('А' <= c <= 'Я') or c in "ёЁ":
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0
    print("Наибольшее количество подряд идущих символов кириллицы:", max_count)