#!/usr/bin/env python3
import cgi
import sqlite3
import html

form = cgi.FieldStorage()
client_id = form.getvalue('id')

print("Content-type: text/html; charset=utf-8\n")
print("<html><head><title>Удаление клиента</title></head><body>")

if client_id:
    conn = sqlite3.connect('fitness_club.db')
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Clients WHERE client_id = ?", (client_id,))
        conn.commit()
        print("<h2>Клиент успешно удален!</h2>")
    except sqlite3.Error as e:
        print(f"<h2>Ошибка удаления клиента: {html.escape(str(e))}</h2>")
    finally:
        conn.close()
else:
    print("<h2>Ошибка: ID клиента не передан для удаления.</h2>")

print("<p><a href='../index.html'>Вернуться к просмотру данных</a></p>")
print("<p><a href='../fitness_cgi.py?table=Clients'>Посмотреть таблицу Клиенты</a></p>")
print("</body></html>")