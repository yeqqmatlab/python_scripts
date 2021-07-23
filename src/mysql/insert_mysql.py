import pymysql
import time

conn = pymysql.connect(host="192.168.1.210", port=3307, user="zsy", password="lc12345", db="data_mining")

print(conn)

#使用cursor()方法创建一个游标对象

cursor = conn.cursor()

# cursor.execute("SELECT * FROM test_ch")

# data = cursor.fetchall()

# print(data)

sql = "INSERT INTO test_ch(id,name,age) VALUES(%s,%s,%s)"

for i in range(100):
    time.sleep(1)
    cursor.execute(sql,(i,"bob","123"))
    conn.commit()



cursor.close()
conn.close()