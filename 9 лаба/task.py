import csv
import re
from datetime import timedelta

CSV_FILENAME = '11 - 1.csv'
ENCODING = 'utf-8'

def parse_time_to_seconds(time_str):
    days, hours, minutes, seconds = 0, 0, 0, 0
    time_str = time_str.lower().strip()
    pattern = r"(?:(\d+)\s*дн\.?)?\s*(?:(\d+)\s*час\.?)?\s*(?:(\d+)\s*мин\.?)?\s*(?:(\d+)\s*сек\.?)?"
    match = re.search(pattern, time_str)
    if match:
        d, h, m, s = match.groups()
        days = int(d) if d else 0
        hours = int(h) if h else 0
        minutes = int(m) if m else 0
        seconds = int(s) if s else 0
    total_seconds = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds).total_seconds()
    return int(total_seconds)

if __name__ == "__main__":
    try:
        target_time_str = input("Введите пороговое время (например, '1 час 30 мин'): ")
        target_score_str = input("Введите искомый балл (например, 8.2): ").replace(',', '.')

        target_time_seconds = parse_time_to_seconds(target_time_str)
        target_score = float(target_score_str)

        matching_people = []

        lastname_header = "Фамилия"
        firstname_header = "Имя"
        time_header = "Затраченное время"
        score_header = "Оценка/10,00"

        with open(CSV_FILENAME, mode='r', encoding=ENCODING, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            if not all(h in reader.fieldnames for h in [lastname_header, firstname_header, time_header, score_header]):
                 print(f"Ошибка: Отсутствуют необходимые заголовки в файле {CSV_FILENAME}")
                 exit()

            for row in reader:
                if "среднее" in row[lastname_header].lower():
                    continue

                try:
                    time_spent_str = row[time_header]
                    score_str = row[score_header].replace(',', '.')

                    if not time_spent_str or not score_str:
                         continue

                    time_spent_seconds = parse_time_to_seconds(time_spent_str)
                    score = float(score_str)

                    if time_spent_seconds > target_time_seconds and score == target_score:
                         last_name = row[lastname_header].strip()
                         first_name = row[firstname_header].strip()
                         matching_people.append((last_name, first_name))
                except (ValueError, TypeError):
                    continue

        matching_people.sort()

        print(f"\nНайдено людей ({len(matching_people)}):")
        if matching_people:
            for person in matching_people:
                print(f"- {person[0]} {person[1]}")
        else:
            print("Соответствующие критериям не найдены.")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{CSV_FILENAME}' не найден.")
    except ValueError:
         print(f"Ошибка: Неверный формат балла '{target_score_str}'.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")