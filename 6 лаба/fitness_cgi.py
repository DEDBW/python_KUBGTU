#!/usr/bin/env python3
import cgi
import sqlite3
import html

def get_table_data(table_name):
    conn = sqlite3.connect('fitness_club.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    conn.close()
    return column_names, rows

def display_table(table_name):
    column_names, rows = get_table_data(table_name)
    print(f"<h2>Таблица: {table_name}</h2>")
    print("<table border='1'>")
    print("<tr>")
    for col_name in column_names:
        print(f"<th>{html.escape(col_name)}</th>")
    print("</tr>")
    for row in rows:
        print("<tr>")
        for cell in row:
            print(f"<td>{html.escape(str(cell))}</td>")
        print("</tr>")
    print("</table>")

form = cgi.FieldStorage()
table_to_display = form.getvalue('table', 'Clients')

print("Content-type: text/html\n")
print("<html><head><title>Фитнес-клуб - Данные</title></head><body>")
print("<h1>Данные Фитнес-клуба</h1>")

print("<form method='get' action='fitness_cgi.py'>")
print("<label for='table'>Выберите таблицу для отображения:</label>")
print("<select name='table' id='table'>")
print(f"<option value='Clients' {'selected' if table_to_display == 'Clients' else ''}>Клиенты</option>")
print(f"<option value='Trainers' {'selected' if table_to_display == 'Trainers' else ''}>Тренеры</option>")
print(f"<option value='Services' {'selected' if table_to_display == 'Services' else ''}>Услуги</option>")
print("</select>")
print("<input type='submit' value='Показать таблицу'>")
print("</form><br>")

display_table(table_to_display)

print("</body></html>")