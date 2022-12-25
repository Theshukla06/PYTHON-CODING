import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password = 'Shukla@06',
    database = 'db1'
    )

cur = mydb.cursor()
# s = "DROP DATABASE db1"                 #("DELETE DATABASE IN MYSQL DATABASE ")
# crtdata = "CREATE DATABASE db1"         #("CREATE DATABASE IN MYSQL DATABASE ")
# crtab = "CREATE TABLE Book(Bookid integer(5),BookName varchar(20),Price float(5,2))"
# cur.execute(crtab)

instdata = "INSERT INTO book(Bookid,BookName,Price) VALUES(%s,%s,%s)"
# b1 = (1,"Python",500)
# cur.execute(instdata,b1)
books = [(2,"Java",500),(3,"Php",90.90),(4,"JavaScript",222)]
cur.executemany(instdata,books)
mydb.commit()






# print(conn.connection_id)
# if conn.is_connected():
#     print("Connection Established")
