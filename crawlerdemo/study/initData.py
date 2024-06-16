
import pymysql

db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    charset="utf8"
)
# 获取操作游标
cursor = db.cursor()
# 用来指定操作哪一个数据库
cursor.execute("use crawlerdemo")
# ”“” 内容 “”“用于书写多行sql语句
sql = """
    create table if not exists job(
        `job_id` int primary key auto_increment,
        `job_name` varchar(40),
        `job_sal` int,
        `company_name` varchar(30),
        `job_place` varchar(10),
        `job_exp` varchar(10),
        `job_education` varchar(10)
    ) 
"""
cursor.execute(sql)
# 查看当前数据库的所有表
cursor.execute("show tables")
res = cursor.fetchall()
print(res)

job_list = [
    {'job_name': 'Java开发', 'job_sal': 7000, 'company_name': '深圳肆专科技有限公司', 'job_place': '南昌',
     'job_exp': '1-3年', 'job_education': '本科'},
    {'job_name': 'JAVA开发工程师', 'job_sal': 10000.0, 'company_name': '江西太平洋宇洪建设有限公司南昌一分公司',
     'job_place': '南昌', 'job_exp': '3-5年', 'job_education': '本科'},
    {'job_name': '初级java开发工程师', 'job_sal': 6000, 'company_name': '和壹科技', 'job_place': '南昌',
     'job_exp': '1-3年', 'job_education': '本科'},
    {'job_name': 'Java开发工程师', 'job_sal': 6000, 'company_name': '江西圣东智能科技有限公司',
     'job_place': '南昌', 'job_exp': '3-5年', 'job_education': '本科'},
    {'job_name': 'java开发实习生', 'job_sal': 2700, 'company_name': '浪潮集团', 'job_place': '南昌',
     'job_exp': '无经验', 'job_education': '本科'},
    {'job_name': 'Java开发工程师', 'job_sal': 6000, 'company_name': '中科软科技股份有限公司',
     'job_place': '南昌', 'job_exp': '3-5年', 'job_education': '本科'},
    {'job_name': 'JAVA工程师', 'job_sal': 10000.0, 'company_name': '思特奇', 'job_place': '南昌',
     'job_exp': '1-3年', 'job_education': '本科'},
    {'job_name': 'Java（学信网-江西数能）', 'job_sal': 7000, 'company_name': '北京腾信软创科技股份有限公司',
     'job_place': '南昌', 'job_exp': '3-5年', 'job_education': '大专'},
    {'job_name': '金融高级java开发', 'job_sal': 10000.0, 'company_name': '北京神州数字科技有限公司',
     'job_place': '南昌', 'job_exp': '3-5年', 'job_education': '本科'},
    {'job_name': 'JAVA开发工程师+食宿+五险一金', 'job_sal': 10000.0, 'company_name': '江西太平洋宇洪建设有限公司',
     'job_place': '南昌', 'job_exp': '3-5年', 'job_education': '本科'},
    {'job_name': 'Java开发工程师', 'job_sal': 10000.0, 'company_name': '赣江新区创新产业投资有限公司',
     'job_place': '南昌', 'job_exp': '5-10年', 'job_education': '大专'},
    {'job_name': '中高级Java开发工程师', 'job_sal': 7000, 'company_name': '南昌中展数智科技有限公司',
     'job_place': '南昌', 'job_exp': '5-10年', 'job_education': '本科'},
    {'job_name': '中级java工程师', 'job_sal': 8000, 'company_name': '江西普赛科技有限公司',
     'job_place': '南昌', 'job_exp': '3-5年', 'job_education': '本科'},
    {'job_name': 'java开发工程师', 'job_sal': 5000, 'company_name': '江西东为高新技术有限公司',
     'job_place': '南昌', 'job_exp': '1-3年', 'job_education': '大专'},
    {'job_name': 'c/c++，java，js，python软件开发', 'job_sal': 18000.0, 'company_name': '外企德科',
     'job_place': '南昌', 'job_exp': '1-3年', 'job_education': '本科'},
    {'job_name': '银行Java（济南岗 线上初试）', 'job_sal': 9000, 'company_name': '易诚互动',
     'job_place': '南昌', 'job_exp': '3-5年', 'job_education': '本科'},
    {'job_name': 'java软件开发工程师', 'job_sal': 10000.0, 'company_name': '江西太平洋宇洪建设有限公司南昌一分公司',
     'job_place': '南昌', 'job_exp': '3-5年', 'job_education': '本科'},
    {'job_name': 'java开发工程师中级', 'job_sal': 11000.0, 'company_name': '诚迈科技', 'job_place': '南昌',
     'job_exp': '经验不限', 'job_education': '本科'},
    {'job_name': '资深java开发工程师', 'job_sal': 11000.0, 'company_name': '思特奇', 'job_place': '南昌',
     'job_exp': '1-3年', 'job_education': '本科'},
    {'job_name': '中高级java工程师+十六薪+包吃住+红谷滩', 'job_sal': 10000.0,
     'company_name': '江西太平洋宇洪建设有限公司南昌一分公司', 'job_place': '南昌', 'job_exp': '3-5年',
     'job_education': '本科'}
]
for job in job_list:
    sql = ("insert into job (job_name,job_sal,company_name,job_place,job_exp,job_education)""values('%s','%s','%s','%s','%s','%s')")%\
          (job["job_name"],job["job_sal"],job["company_name"],job["job_place"],job["job_exp"],job["job_education"])
    # sql = "insert into job values(null,'%s','%s','%s','%s','%s','%s')" % (job["job_name"],job["job_sal"],
    #                             job["company_name"],job["job_place"],job["job_exp"],job["job_education"])

    try:
        cursor.execute(sql)
 #       db.commit()
    except Exception as e:
        print(e)
        print("插入数据失败")
        # 当插入出现问题时，回滚事务，即本次插入失败
        db.rollback()
# 提交事务，只有提交事务之后，数据才是真正插入到表中
db.commit()
cursor.execute("select * from job")
data = cursor.fetchall()
for i in data:
    print(i)
# 关闭游标
cursor.close()
# 关闭数据库
db.close()