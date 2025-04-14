#!/usr/bin/env python3
import cgi
import sqlite3
import html

form = cgi.FieldStorage()

print("Content-type: text/html; charset=utf-8\n")
print("<html><head><title>Редактирование клиента</title></head><body>")

# Если пришли данные из формы (например, если передано поле first_name),
# значит, это запрос на обновление данных.
if form.getvalue('first_name'):
    client_id = form.getvalue('id')
    first_name = form.getvalue('first_name')
    last_name = form.getvalue('last_name')
    phone_number = form.getvalue('phone_number')
    email = form.getvalue('email')
    membership_type = form.getvalue('membership_type')
    registration_date = form.getvalue('registration_date')

    # Обновляем данные в базе
    conn = sqlite3.connect('fitness_club.db')
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Clients
        SET first_name = ?,
            last_name = ?,
            phone_number = ?,
            email = ?,
            membership_type = ?,
            registration_date = ?
        WHERE client_id = ?
    """, (first_name, last_name, phone_number, email, membership_type, registration_date, client_id))
    conn.commit()
    conn.close()

    print("<h2>Данные клиента обновлены.</h2>")
    print('<p><a href="../index.html">Вернуться к просмотру данных</a></p>')

# Если данных для обновления нет, значит, нужно показать форму с текущими данными.
else:
    client_id = form.getvalue('id')
    if client_id:
        conn = sqlite3.connect('fitness_club.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Clients WHERE client_id = ?", (client_id,))
        client_data = cursor.fetchone()
        conn.close()

        if client_data:
            print(f"""
                <script>
                    document.addEventListener('DOMContentLoaded', function() {{
                        document.getElementById('client_id').value = '{html.escape(str(client_data[0]))}';
                        document.getElementById('first_name').value = '{html.escape(str(client_data[1]))}';
                        document.getElementById('last_name').value = '{html.escape(str(client_data[2]))}';
                        document.getElementById('phone_number').value = '{html.escape(str(client_data[3] or ''))}';
                        document.getElementById('email').value = '{html.escape(str(client_data[4] or ''))}';
                        document.getElementById('membership_type').value = '{html.escape(str(client_data[5] or ''))}';
                        document.getElementById('registration_date').value = '{html.escape(str(client_data[6] or '')).split(' ')[0]}';
                    }});
                </script>
            """)

            with open("edit_client_form.html", "r", encoding="utf-8") as f:
                print(f.read())
        else:
            print("<h2>Клиент не найден.</h2>")
    else:
        print("<h2>Ошибка: ID клиента не передан.</h2>")

print("</body></html>")
