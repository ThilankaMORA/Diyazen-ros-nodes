 #!/usr/bin/env python3

import mysql.connector

mydb=mysql.connector.connect(
   host = "localhost",
   user = "root",
   passwd = "diyazen123",
   database = "rosdb" ,
)

my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE rosdb")

# my_cursor.execute("SHOW DATABASES")

# for db in my_cursor:
#     print(db)

# my_cursor.execute("CREATE TABLE places(id INTEGER AUTO_INCREMENT PRIMARY KEY, place VARCHAR(255), pose JSON)")
# my_cursor.execute("SHOW TABLES")

# sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
# record1 = ("John", "john@codemy.com",40)

# my_cursor.execute(sqlStuff,record1)
# mydb.commit()

# sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"

# records = [
#     ("Tim","tim@tim.com", 32),
#     ("Marry", "Mary@mary.com", 21),
#     ("Steve", "steve@steveEmail.com", 57),
#     ("Tina", "tina@somethingesle.com", 29),
# ]

# my_cursor.executemany(sqlStuff,records)
# mydb.commit()

# my_cursor.execute("SELECT * FROM users")
# result = my_cursor.fetchall()
# for row in result:
#     print(row)

# my_cursor.execute("SELECT * FROM users WHERE age = 57")
# result = my_cursor.fetchall()
# for row in result:
#     print(row)

# my_sql = "UPDATE users SET age = 50 WHERE user_id = 4"
# my_cursor.execute(my_sql)
# mydb.commit()

# my_sql = "DELETE FROM users WHERE user_id = 5"
# my_cursor.execute(my_sql)
# mydb.commit()

# my_sql = "DROP TABLE IF EXISTS users"
# my_cursor.execute(my_sql)
