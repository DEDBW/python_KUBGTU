import sqlite3

def create_database():
    conn = sqlite3.connect('fitness_club.db')
    cursor = conn.cursor()

    # Создание таблицы Clients
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Clients (
            client_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone_number TEXT UNIQUE,
            email TEXT UNIQUE,
            membership_type TEXT,
            registration_date DATE
        )
    ''')

    # Создание таблицы Trainers
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Trainers (
            trainer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            specialization TEXT,
            hire_date DATE
        )
    ''')

    # Создание таблицы Services
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Services (
            service_id INTEGER PRIMARY KEY AUTOINCREMENT,
            service_name TEXT NOT NULL,
            description TEXT,
            duration_minutes INTEGER,
            trainer_id INTEGER,
            FOREIGN KEY (trainer_id) REFERENCES Trainers(trainer_id)
        )
    ''')

    conn.commit()
    conn.close()
    print("База данных и таблицы успешно созданы.")

if __name__ == '__main__':
    create_database()