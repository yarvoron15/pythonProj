import sqlite3
import random

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
)''')

cursor.execute("INSERT INTO countries (title) VALUES ('Киргизия')")
cursor.execute("INSERT INTO countries (title) VALUES ('Германия')")
cursor.execute("INSERT INTO countries (title) VALUES ('Китай')")

cursor.execute('''CREATE TABLE IF NOT EXISTS cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    area REAL DEFAULT 0,
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES countries(id)
)''')

cities_data = [
    ('Бишкек', 1),
    ('Ош', 1),
    ('Берлин', 2),
    ('Пекин', 3),
    # Добавьте еще городов по аналогии
]

for city_data in cities_data:
    area = random.uniform(50, 500)  # Генерация случайной площади от 50 до 500
    cursor.execute("INSERT INTO cities (title, country_id, area) VALUES (?, ?, ?)", (city_data[0], city_data[1], area))

cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    city_id INTEGER,
    FOREIGN KEY (city_id) REFERENCES cities(id)
)''')

students_data = [
    ('Иван', 'Иванов', 1),
    ('Петр', 'Петров', 2),
    ('Мария', 'Сидорова', 3),
    # Добавьте еще учеников по аналогии
]

for student_data in students_data:
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)", student_data)

conn.commit()
conn.close()

def display_cities():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()

    print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
    for city in cities:
        print(f"{city[0]}. {city[1]}")

    city_id = int(input("Введите id города: "))

    if city_id == 0:
        print("Программа завершена.")
    else:
        cursor.execute("SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area "
                       "FROM students "
                       "JOIN cities ON students.city_id = cities.id "
                       "JOIN countries ON cities.country_id = countries.id "
                       "WHERE cities.id = ?", (city_id,))
        students_info = cursor.fetchall()

        print("\nИнформация о студентах в выбранном городе:")
        for student_info in students_info:
            print(f"Имя: {student_info[0]}, Фамилия: {student_info[1]}, Страна: {student_info[2]}, Город: {student_info[3]}, Площадь города: {student_info[4]}")

    conn.close()

display_cities()
