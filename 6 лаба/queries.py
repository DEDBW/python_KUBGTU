import sqlite3

def execute_queries():
    conn = sqlite3.connect('fitness_club.db')
    cursor = conn.cursor()

    # 1. Количество клиентов по типам абонементов
    cursor.execute('''
        SELECT membership_type, COUNT(*)
        FROM Clients
        GROUP BY membership_type
    ''')
    print("1. Количество клиентов по типам абонементов:")
    for row in cursor.fetchall():
        print(f"Тип абонемента: {row[0]}, Количество: {row[1]}")
    print("-" * 30)

    # 2. Список тренеров и количество услуг, которые они проводят
    cursor.execute('''
        SELECT t.first_name, t.last_name, COUNT(s.service_id) AS service_count
        FROM Trainers t
        LEFT JOIN Services s ON t.trainer_id = s.trainer_id
        GROUP BY t.trainer_id
        ORDER BY service_count DESC
    ''')
    print("2. Список тренеров и количество услуг:")
    for row in cursor.fetchall():
        print(f"Тренер: {row[0]} {row[1]}, Услуг: {row[2]}")
    print("-" * 30)

    # 3. Средняя продолжительность услуг
    cursor.execute('''
        SELECT AVG(duration_minutes)
        FROM Services
    ''')
    average_duration = cursor.fetchone()[0]
    print(f"3. Средняя продолжительность услуг: {average_duration:.2f} минут")
    print("-" * 30)

    # 4. Клиенты, зарегистрированные в определенном месяце (например, в июне)
    cursor.execute('''
        SELECT first_name, last_name, registration_date
        FROM Clients
        WHERE strftime('%m', registration_date) = '06' -- Июнь
    ''')
    print("4. Клиенты, зарегистрированные в июне:")
    for row in cursor.fetchall():
        print(f"Клиент: {row[0]} {row[1]}, Дата регистрации: {row[2]}")
    print("-" * 30)

    conn.close()

if __name__ == '__main__':
    execute_queries()