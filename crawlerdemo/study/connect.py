
import pymysql as pymysql

# 创建数据库连接
# localhost 127.0.0.1 都是本机
#port可以不写，默认是3306
db = pymysql.connect(
    host="localhost",
    port =3306,
    user = "root",
    database = "crawlerdemo",
    password= "123456",
    charset= "utf8"
)
#获取操作游标，即操作数据库的一个对象
cursor = db.cursor()
# 使用execute方法执行sql语句
cursor.execute("select * from m_stu")
print(cursor)
# fetchone() 方法用来获取一条数据，字符串
# data = cursor.fetchone()
# fetchall() 方法用来获取所有数据，获取出来的数据用元组（tuple）来保存
data = cursor.fetchall()
#print("当前数据库版本：%s" % data)
print(data)
#关闭游标
cursor.close()
# 关掉数据库连接
db.close()