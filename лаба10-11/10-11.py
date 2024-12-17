from flask import Flask, request, render_template_string, jsonify
import sqlite3
import json

app = Flask(__name__)

# Создание базы данных и таблиц
def setup_database():
    connection = sqlite3.connect("medicine.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Patients (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Doctors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        specialty TEXT
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Appointments (
        id INTEGER PRIMARY KEY,
        patient_id INTEGER,
        doctor_id INTEGER,
        appointment_date TEXT,
        FOREIGN KEY (patient_id) REFERENCES Patients (id),
        FOREIGN KEY (doctor_id) REFERENCES Doctors (id)
    );
    """)

    # Заполнение таблиц
    cursor.execute("INSERT OR IGNORE INTO Patients (id, name, age, gender) VALUES (1, 'Саша', 30, 'Female');")
    cursor.execute("INSERT OR IGNORE INTO Patients (id, name, age, gender) VALUES (2, 'Максим', 45, 'Male');")
    cursor.execute("INSERT OR IGNORE INTO Doctors (id, name, specialty) VALUES (1, 'Иванов', 'Cardiology');")
    cursor.execute("INSERT OR IGNORE INTO Doctors (id, name, specialty) VALUES (2, 'Смирнов', 'Neurology');")
    cursor.execute("INSERT OR IGNORE INTO Appointments (id, patient_id, doctor_id, appointment_date) VALUES (1, 1, 1, '2024-12-10');")
    cursor.execute("INSERT OR IGNORE INTO Appointments (id, patient_id, doctor_id, appointment_date) VALUES (2, 2, 2, '2024-12-11');")

    connection.commit()
    connection.close()

# HTML-шаблон для отображения таблиц
table_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h1>{{ title }}</h1>
    <table>
        <thead>
            <tr>
                {% for header in headers %}
                <th>{{ header }}</th>
                {% endfor %}
            </tr>
        </thead>
        <tbody>
            {% for row in rows %}
            <tr>
                {% for cell in row %}
                <td>{{ cell }}</td>
                {% endfor %}
            </tr>
            {% endfor %}
        </tbody>
    </table>
    <a href="/">Назад на главную</a>
</body>
</html>
"""

# Маршрут для отображения таблиц
@app.route("/view/<table>")
def view_table(table):
    connection = sqlite3.connect("medicine.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    headers = [description[0] for description in cursor.description]
    connection.close()

    return render_template_string(table_template, title=f"Таблица: {table}", headers=headers, rows=rows)

# HTML-шаблон для формы
form_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Добавить пациента</title>
</head>
<body>
    <h1>Добавить пациента</h1>
    <form method="post" action="/add_patient">
        <label for="name">Имя:</label>
        <input type="text" id="name" name="name" required><br>
        <label for="age">Возраст:</label>
        <input type="number" id="age" name="age" required><br>
        <label for="gender">Пол:</label>
        <select id="gender" name="gender">
            <option value="Male">Мужской</option>
            <option value="Female">Женский</option>
        </select><br>
        <input type="submit" value="Добавить">
    </form>
    <a href="/">Назад на главную</a>
</body>
</html>
"""

# Маршрут для добавления пациента
@app.route("/add_patient", methods=["GET", "POST"])
def add_patient():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]

        connection = sqlite3.connect("medicine.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Patients (name, age, gender) VALUES (?, ?, ?);", (name, age, gender))
        connection.commit()
        connection.close()
        return f"<h1>Пациент {name} добавлен!</h1><a href='/add_patient'>Назад</a>"
    return render_template_string(form_template)

# Экспорт таблицы в JSON
@app.route("/export")
def export_to_json():
    connection = sqlite3.connect("medicine.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Patients;")
    patients = cursor.fetchall()

    data = {"Patients": [dict(zip([column[0] for column in cursor.description], row)) for row in patients]}
    with open("patients.json", "w") as file:
        json.dump(data, file, indent=4)

    connection.close()
    return jsonify({"message": "Данные экспортированы в patients.json"})

# Импорт из JSON в таблицу
@app.route("/import")
def import_from_json():
    connection = sqlite3.connect("medicine.db")
    cursor = connection.cursor()

    with open("patients.json", "r") as file:
        data = json.load(file)

    for patient in data["Patients"]:
        cursor.execute("INSERT OR IGNORE INTO Patients (id, name, age, gender) VALUES (?, ?, ?, ?);",
                       (patient["id"], patient["name"], patient["age"], patient["gender"]))

    connection.commit()
    connection.close()
    return jsonify({"message": "Данные импортированы из patients.json"})

# Главная страница
@app.route("/")
def home():
    return """
    <h1>Добро пожаловать в медицинскую систему</h1>
    <ul>
        <li><a href="/add_patient">Добавить пациента</a></li>
        <li><a href="/view/Patients">Просмотреть пациентов</a></li>
        <li><a href="/view/Doctors">Просмотреть врачей</a></li>
        <li><a href="/view/Appointments">Просмотреть записи на прием</a></li>
        <li><a href="/export">Экспортировать пациентов в JSON</a></li>
        <li><a href="/import">Импортировать пациентов из JSON</a></li>
    </ul>
    """

if __name__ == "__main__":
    setup_database()
    app.run(debug=True)