#!/usr/bin/env python3
import cgi
import sqlite3
import html

form = cgi.FieldStorage()

client_id = form.getvalue('client_id')
first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')
phone_number = form.getvalue('phone_number')
email = form.getvalue('email')
membership_type = form.getvalue('membership_type')
registration_date = form.getvalue('registration_date')


print("Content-type: text/html; charset=utf-8\n")
print("<html><head><title>Редактирование клиента</title></head><body>")

if client_id and first_name and last_name:
    conn = sqlite3.connect('fitness_club.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            UPDATE Clients
            SET first_name = ?, last_name = ?, phone_number = ?, email = ?,
                membership_type = ?, registration_date = ?
            WHERE client_id = ?
        ''', (first_name, last_name, phone_number, email, membership_type, registration_date, client_id))
        conn.commit()
        print("<h2>Данные клиента успешно обновлены!</h2>")
    except sqlite3.Error as e:
        print(f"<h2>Ошибка обновления данных клиента: {html.escape(str(e))}</h2>")
    finally:
        conn.close()
else:
    print("<h2>Ошибка: Недостаточно данных для обновления.</h2>")

print("<p><a href='../index.html'>Вернуться к просмотру данных</a></p>")
print("<p><a href='../fitness_cgi.py?table=Clients'>Посмотреть таблицу Клиенты</a></p>")
print("</body></html>")