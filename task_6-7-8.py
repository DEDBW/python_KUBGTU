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


def solve_task_7():
    s = input("Введите строку для задачи 7: ")
    min_number = None
    num_str = ""

    for c in s:
        if c.isdigit():
            num_str += c
        else:
            if num_str:
                num = int(num_str)
                if num > 0:
                    if min_number is None or num < min_number:
                        min_number = num
                num_str = ""

    if num_str:
        num = int(num_str)
        if num > 0:
            if min_number is None or num < min_number:
                min_number = num

    if min_number is not None:
        print("Минимальное натуральное число в строке:", min_number)
    else:
        print("В строке не найдено натуральных чисел.")

def solve_task_8():
    s = input("Введите строку для задачи 8: ")
    max_count = 0
    current_count = 0
    for c in s:
        if c.isdigit():
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0
    print("Наибольшее количество подряд идущих цифр:", max_count)

def solve_task_6_7_8():
    while True:
        print("\nВыберите задачу для решения:")
        print("6 - Найти наибольшее количество подряд идущих символов кириллицы")
        print("7 - Найти минимальное натуральное число в строке")
        print("8 - Найти наибольшее количество подряд идущих цифр")
        print("0 - Выход")
        choice = input("Ваш выбор: ")

        if choice == "6":
            solve_task_6()
        elif choice == "7":
            solve_task_7()
        elif choice == "8":
            solve_task_8()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 6, 7, 8 или 0 для выхода.")

solve_task_6_7_8()