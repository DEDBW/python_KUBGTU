import sqlite3

def fill_database():
    conn = sqlite3.connect('fitness_club.db')
    cursor = conn.cursor()

    # Заполнение таблицы Trainers
    trainers = [
        ('Иван', 'Иванов', 'Силовые тренировки', '2023-01-15'),
        ('Елена', 'Петрова', 'Йога', '2022-11-20'),
        ('Сергей', 'Сидоров', 'Кардио', '2023-03-10')
    ]
    cursor.executemany('''
        INSERT INTO Trainers (first_name, last_name, specialization, hire_date)
        VALUES (?, ?, ?, ?)
    ''', trainers)

    # Заполнение таблицы Clients
    clients = [
        ('Анна', 'Смирнова', '+79123456789', 'anna.smirnova@email.com', 'Премиум', '2023-04-01'),
        ('Петр', 'Кузнецов', '+79234567890', 'petr.kuznetsov@email.com', 'Базовый', '2023-05-15'),
        ('Мария', 'Соколова', '+79345678901', 'maria.sokolova@email.com', 'Премиум', '2023-06-20')
    ]
    cursor.executemany('''
        INSERT INTO Clients (first_name, last_name, phone_number, email, membership_type, registration_date)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', clients)

    # Заполнение таблицы Services
    services = [
        ('Персональная тренировка', 'Индивидуальная тренировка с тренером', 60, 1), # Trainer_id 1 (Иван Иванов)
        ('Групповая йога', 'Занятие йогой в группе', 90, 2), # Trainer_id 2 (Елена Петрова)
        ('Кардио тренировка', 'Интенсивная кардио тренировка', 45, 3) # Trainer_id 3 (Сергей Сидоров)
    ]
    cursor.executemany('''
        INSERT INTO Services (service_name, description, duration_minutes, trainer_id)
        VALUES (?, ?, ?, ?)
    ''', services)

    conn.commit()
    conn.close()
    print("Таблицы успешно заполнены данными.")

if __name__ == '__main__':
    fill_database()