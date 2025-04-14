#!/usr/bin/env python3
import cgi
import sqlite3
import html

form = cgi.FieldStorage()

first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')
phone_number = form.getvalue('phone_number')
email = form.getvalue('email')
membership_type = form.getvalue('membership_type')
registration_date = form.getvalue('registration_date')

print("Content-type: text/html; charset=utf-8\n")
print("<html><head><title>Добавление клиента</title></head><body>")

if first_name and last_name:
    conn = sqlite3.connect('fitness_club.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO Clients (first_name, last_name, phone_number, email, membership_type, registration_date)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (first_name, last_name, phone_number, email, membership_type, registration_date))
        conn.commit()
        print("<h2>Клиент успешно добавлен!</h2>")
    except sqlite3.Error as e:
        print(f"<h2>Ошибка добавления клиента: {html.escape(str(e))}</h2>")
    finally:
        conn.close()
else:
    print("<h2>Ошибка: Имя и Фамилия обязательны для заполнения.</h2>")

print("<p><a href='../index.html'>Вернуться к просмотру данных</a></p>")
print("<p><a href='../add_client_form.html'>Добавить еще одного клиента</a></p>")
print("</body></html>")