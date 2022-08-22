import pymysql

'''
description: mysql表结构与hive元数据对比
Created by yqq
2022-08-19
'''
connection = pymysql.connect(host="192.168.1.210"
                             , port=3307
                             , user="zsy"
                             , password="lc12345"
                             , db="zsy_school_5201"
                             , charset='utf8'
                             , cursorclass=pymysql.cursors.DictCursor)


conn_sink = pymysql.connect(host="192.168.1.210"
                            , port=3307
                            , user="zsy"
                            , password="lc12345"
                            , db="data_mining"
                            , charset='utf8'
                            , cursorclass=pymysql.cursors.DictCursor)

tables = []
schemes = []

try:
    with connection.cursor() as cursor:
        sql_tables = "SHOW TABLES"
        cursor.execute(sql_tables)
        result = cursor.fetchall()
        for i in range(len(result)):
            tables.append(result[i]['Tables_in_zsy_school_5201'])

        for i in range(len(tables)):
            sql_desc = " desc "+tables[i]
            cursor.execute(sql_desc)
            res_desc = cursor.fetchall()
            tuple2 = (tables[i], len(res_desc))
            schemes.append(tuple2)
finally:
    connection.close()

sql_insert = "INSERT INTO tbl_monitor_mysql(id,table_name,field_num) VALUES(%s,%s,%s)"
sql_truncate = "truncate tbl_monitor_mysql"

try:
    with conn_sink.cursor() as cursor_sink:
        cursor_sink.execute(sql_truncate)
        conn_sink.commit()
        for i in range(len(schemes)):
            cursor_sink.execute(sql_insert, (i, schemes[i][0], schemes[i][1]))
        conn_sink.commit()
finally:
    conn_sink.close()


print(schemes)


