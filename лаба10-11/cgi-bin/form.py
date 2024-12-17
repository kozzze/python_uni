#!/usr/bin/env python3
import cgi
import sqlite3

print("Content-type: text/html\n")
form = cgi.FieldStorage()

name = form.getvalue("name")
age = form.getvalue("age")
gender = form.getvalue("gender")

if name and age and gender:
    connection = sqlite3.connect("../medicine.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Patients (name, age, gender) VALUES (?, ?, ?);", (name, age, gender))
    connection.commit()
    connection.close()
    print("<h1>Пациент добавлен!</h1>")

print('''
<form method="post" action="form.py">
    <label for="name">Имя:</label>
    <input type="text" id="name" name="name"><br>
    <label for="age">Возраст:</label>
    <input type="number" id="age" name="age"><br>
    <label for="gender">Пол:</label>
    <select id="gender" name="gender">
        <option value="Male">Мужской</option>
        <option value="Female">Женский</option>
    </select><br>
    <input type="submit" value="Добавить">
</form>
''')
