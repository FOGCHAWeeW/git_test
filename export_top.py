import psycopg2
import csv 

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="shop",
    user="postgres",
    password="2019"
)
cur = conn.cursor()
query = """
SELECT 
    customers.name,
    SUM(orders.quantity * products.price) AS total
FROM orders
JOIN customers ON orders.customer_id = customers.id
JOIN products ON orders.product_id = products.id
GROUP BY customers.name
ORDER BY total DESC
LIMIT 5;
"""
cur.execute(query)
rows = cur.fetchall()
with open("top_customers.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Имя","Сумма"])
    writer.writerows(rows)


cur.close()
conn.close()
print("go")