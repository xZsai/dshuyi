
# 连接数据库
import pymysql
from pyecharts.charts import Bar
from pyecharts import options
db = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "crawlerdemo",
    charset = "utf8"
)
cursor = db.cursor()
sql = "select avg(job_sal),job_place from job group by job_place order by avg(job_sal) limit 5"

sal = []
city = []

try:
    cursor.execute(sql)
    res = cursor.fetchall()
    for i in res:
        sal.append(i[0])
        city.append(i[1])
except:
    print("查询出问题了")

# 创建柱状图对象
bar = Bar()
# 添加x轴的数据
bar.add_xaxis(city)
# 添加y轴的数据"月薪水/元" 是y轴数据的单位
bar.add_yaxis("月薪水/元",sal)
# 添加图标的 标题
bar.set_global_opts(title_opts=options.TitleOpts(title="平均工资最低的五个城市",subtitle="单位/元"))
bar.render("baravg.html")