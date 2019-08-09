import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "GracE-1056",
    #Connecting to a specific database
    database="mydatabase"
)

mycursor = mydb.cursor()
#Create a database
#mycursor.execute("CREATE DATABASE mydatabase")
#Show list databases
'''
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
'''
'''
#Creating tables
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
'''
'''
#Altering a table in the database
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
#Inserting an element into the table
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
'''
'''
#Insert multiple rows
sql = "INSERT INTO customers(name, address) VALUES (%s, %s)"
val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)
#mydb.commit(). It is required to make the changes,
#otherwise no changes are made to the table.
mydb.commit()
print(mycursor.rowcount, "was inserted.")
'''
'''
sql = "INSERT INTO customers(name, address) VALUES (%s, %s)"
val = ("Eliezer", "Kronom 1497")
mycursor.execute(sql, val)
mydb.commit()
print("1 record inserted, ID:", mycursor.lastrowid)
'''
'''
#Selecting elements
#We use the fetchall() method,
#which fetches all rows from the last executed statement.
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
'''
'''
mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
'''
'''
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult)
'''
'''
sql = "SELECT * FROM customers WHERE address ='Ocean blvd 2'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
'''
'''
#Wildcards
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
'''
'''
#Escape query values by using the placholder %s method
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2",)
mycursor.execute(sql,adr)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
'''
'''
#Using ORDER BY
sql = "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
'''
'''
#Ordering the data in descending order
sql = "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
'''
'''
#Delete any record where the address is =:
#Important!: Notice the statement: mydb.commit().
#It is required to make the changes, otherwise no changes are made to the table.
#Notice the WHERE clause in the DELETE syntax:
#The WHERE clause specifies which record(s) that should be deleted.
#If you omit the WHERE clause, all records will be deleted!
sql = "DELETE FROM customers WHERE address='Kronom 1497'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")
'''
'''
#Prevent SQL Injection
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2",)
mycursor.execute(sql, adr)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")
'''
'''
#sql = "CREATE TABLE acid (first_name VARCHAR(255), last_name VARCHAR(255))"
#mycursor.execute(sql)
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
'''
'''
sql = "DROP TABLE acid"
mycursor.execute(sql)
'''
'''
sql = "DROP TABLE IF EXISTS rock "
mycursor.execute(sql)
'''
'''
#Notice the WHERE clause in the UPDATE syntax:
#The WHERE clause specifies which record or records that should be updated.
#If you omit the WHERE clause, all records will be updated!
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
'''
'''
#Prevent SQL injection
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
'''
'''
#Limit the number of result
mycursor.execute("SELECT * FROM customers LIMIT 5")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
'''
'''
#If you want to return five records,
#starting from the third record,
#you can use the "OFFSET" keyword:
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
'''
'''
#mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav INT)")
#mycursor.execute("CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")

sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
val = [
    ('John', 154),
    ('Peter', 154),
    ('Amy', 155),
    ('Hannah',156),
    ('Michael',157)
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

mycursor.execute("SELECT * FROM users")
for x in mycursor:
    print(x)
'''
'''
#mycursor.execute("DROP TABLE users")
sql = 'INSERT INTO products (id, name) VALUES (%s, %s)'
val = [
    (154, 'Chocolate Heaven'),
    (155, 'Tasty Lemons'),
    (156, 'Vanilla Dreams')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

mycursor.execute("SELECT * FROM products")
for x in mycursor:
    print(x)
'''
'''
#You can use JOIN instead of INNER JOIN.
#They will both give you the same result.
sql = "SELECT \
    users.name AS user, \
    products.name AS favorite \
    FROM users \
    INNER JOIN products ON users.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
'''
#Select all users and their favorite products
#Left Join
'''
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
'''
#Right Join
#Select all products, and the user(s) who have them as their favorite:
'''
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
'''
