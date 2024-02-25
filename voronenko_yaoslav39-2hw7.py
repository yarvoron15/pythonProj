import sqlite3

conn = sqlite3.connect('hw.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS products (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               product_title TEXT NOT NULL,
               price REAL NOT NULL DEFAULT 0.0,
               quantity INTEGER NOT NULL DEFAULT 0
               )''')

def add_products():
    products = [
        ("Шариковая ручка синяя", 10.50, 100),
        ("Тетрадь в клетку 96 листов", 15.75, 50),
        ("Фломастеры 12 цветов", 25.99, 30),
        ("Карандаши HB 12 штук", 8.99, 80),
        ("Ластик", 2.50, 200),
        ("Набор пластилина 6 цветов", 12.25, 40),
        ("Клей ПВА 100 мл", 5.75, 60),
        ("Кисти для рисования набор 5 штук", 18.50, 25),
        ("Акварельные краски 12 цветов", 30.99, 20),
        ("Папка-регистратор на кнопке", 7.99, 75),
        ("Калькулятор на солнечной батарее", 35.00, 15),
        ("Линейка 30 см", 3.25, 150),
        ("Ножницы для бумаги", 6.50, 100),
        ("Конверты почтовые 20 штук", 4.99, 50),
        ("Блокнот A5", 12.99, 35)
    ]

    cur.executemany("INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)", products)
    conn.commit()

def update_quantity(product_id, new_quantity):
    cur.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))
    conn.commit()

def update_price(product_id, new_price):
    cur.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
    conn.commit()

def delete_product(product_id):
    cur.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()

def select_all_products():
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    for product in products:
        print(product)

def select_products_below_limit():
    cur.execute("SELECT * FROM products WHERE price < 100 AND quantity > 5")
    products = cur.fetchall()
    for product in products:
        print(product)

def search_products_by_title(title):
    cur.execute("SELECT * FROM products WHERE product_title LIKE ?", ('%' + title + '%',))
    products = cur.fetchall()
    for product in products:
        print(product)

add_products()

update_quantity(1, 120)
update_price(3, 22.50)

delete_product(15)

select_all_products()

select_products_below_limit()

search_products_by_title('мыло')

conn.close()


