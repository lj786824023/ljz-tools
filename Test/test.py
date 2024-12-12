import dmapi

# 连接数据库
conn = dmapi.connect(host='localhost', port='5236', user='username', password='password', dbname='dbname')

# 创建游标对象
cursor = conn.cursor()

# 执行SQL语句
cursor.execute("SELECT * FROM table_name")

# 获取结果
result = cursor.fetchall()

# 打印结果
for row in result:
    print(row)

# 关闭游标和连接
cursor.close()
conn.close()
