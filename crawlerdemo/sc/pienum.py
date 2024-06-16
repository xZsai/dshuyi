
import pymysql
from pyecharts.charts import Pie
from pyecharts import options
db = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "crawlerdemo",
    charset = "utf8"
)
cursor = db.cursor()
# 用来查找岗位数量最多的五个城市
sql = ("select job_place,count(job_id) from job group by job_place order by count(job_id) desc limit 5")
try:
    cursor.execute(sql)
    res = cursor.fetchall()
    pie = Pie()
    # [("类型1"，30),(“类型2”,40),......]
    pie.add("单位/个",res)
    pie.set_global_opts(title_opts=options.TitleOpts(title="岗位数最多的五个城市"))
    pie.render("pienum.html")
except:
    print("查询出错啦")
