import mysql.connector
connection = mysql.connector.connect(user = ‘root’, database = ‘example’, password = ‘password’)
cursor = connection.cursor()
addData = (“INSERT INTO table_name (column1, column2, column3...) VALUES (value1,value2,value3)”)
cursor.execute(addData)
connection.commit()
cursor.close()
connection.close()
print("hello")