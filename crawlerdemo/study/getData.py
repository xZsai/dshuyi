
# 导入一整个类
import string
import urllib.request
# 只导入某一个方法
from urllib.parse import quote

import pymysql
from bs4 import BeautifulSoup


def nospace(world):
    return world.strip().replace(" ", "").replace("\n", "")

city = input("请输入城市：")
code = {
'北京': '530',
    '上海': '538',
    '广州': '763',
    '深圳': '765',
    '天津': '531',
    '武汉': '736',
    '西安': '854',
    '成都': '801',
    '沈阳': '599',
    '南京': '635',
    '杭州': '653',
    '苏州': '639',
    '重庆': '551',
    '长沙': '749',
    '厦门': '682',
    '南昌': '691'
}
# 将用户输入的城市替换成对应的城市代码
city = code[city]

type = input("请输入岗位：")
# 进行字符串拼接，完成最终爬取的地址
url = "https://sou.zhaopin.com/?jl=" + city + "&kw=" + type + "&p=1"
# 如果url中需要有空格，则需要手动转义，用  %20 来替代空格
# 如果url中需要中文，则需要通过quote 进行转义
# url中允许使用的字符有  数字、英文字母、一些特殊符号
# -_~! 键盘能够输入的符号，基本都支持
url = quote(url,safe=string.printable)
res = urllib.request.urlopen(url)
print(url)
# read()取出网页源代码(byte类型的数据)
# 可以通过decode()转换成utf-8
# 网页源代码不包括js处理后的数据
content = res.read().decode()
# print(content)

# 通过beautifulSoup对象来解析咱们得到的页面内容
# 同时需要安装解析器，推荐使用 lxml 这个解析器需要手动导入
soup = BeautifulSoup(content,"lxml")
# 通过select()方法通过类名来获取数据
jobitem = soup.select(".joblist-box__item")
print(jobitem)
# 用来存放所需数据的列表
job_list = []
for job in jobitem:
    # 用来存放单条招聘信息
    job_dic = {}
    # get_text() 用来获取所有文本内容，但是是以字符字符串列表的方式显示
    # getText() 用来获取所有文本内容，但是会拼接成一个字符串显示
    job_name = job.select(".jobinfo__name")[0].get_text()
    job_sal = job.select(".jobinfo__salary")[0].get_text()
    # 用来处理工资的左右两边空格，以及内容之间的空格，最后还有 换行
    # job_sal = job_sal.strip().replace(" ","").replace("\n","")
    job_sal = nospace(job_sal)
    print(job_sal)
    if '天' in job_sal:
        job_sal = int(job_sal.split("-")[0])*30
    elif('千' in job_sal):
        job_sal = int(job_sal.split("千")[0])*1000
    elif('万' in job_sal):
        job_sal = float(job_sal.split("万")[0]) * 10000
    else:
        job_sal = 5000
    # 拿到公司名称
    company_name = nospace(job.select(".companyinfo__name")[0].get_text())
    # 同时获取三个信息
    job_msg = job.select(".jobinfo__other-info-item")
    # 工作地点
    # "abcd"[0:2] 代表从下标为0开始取值 直到下标为 2 但是取不到下标为2的字符 ab
    job_place = nospace(job_msg[0].get_text())[0:2]
    # 工作经验
    job_exp = nospace(job_msg[1].get_text())
    # 学历要求
    job_education = nospace(job_msg[2].get_text())
    # 最后将获取到的数据全部放入字典
    job_dic["job_name"] = job_name
    job_dic["job_sal"] = job_sal
    job_dic["company_name"] = company_name
    job_dic["job_place"] = job_place
    job_dic["job_exp"] = job_exp
    job_dic["job_education"] = job_education
    print(job_dic)
    job_list.append(job_dic)

# 创建数据库连接
db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    database="crawlerdemo",
    charset="utf8"
)
# 获取操作游标
cursor = db.cursor()
for job in job_list:
    sql = "insert into job values(null,'%s','%s','%s','%s','%s','%s')" % (job["job_name"],job["job_sal"],job["company_name"],
                                                                          job["job_place"],job["job_exp"],job["job_education"])
    try:
        cursor.execute(sql)
    except Exception as e:
        print(e)
        print("插入数据失败")
        db.rollback()
db.commit()
# 关闭游标
cursor.close()
# 关闭数据库
db.close()


