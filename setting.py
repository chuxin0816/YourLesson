# -*- coding: utf-8 -*-
# 程序设置

'''
这是一个用户配置文档，您只需要在这里进行配置。
需要配置的属性有:
1. user_id: 学号
2. cookie,electiveBatchCode,token这三个字段需要在浏览器登录后，打开开发者工具，选择在network选项卡中选择recommendedCourse.do
   然后再找出相应字段
3. 你要选择的课程，类比相关格式，填写courses
4. 然后设置抢课延迟和选课提交次数
'''

user_id = "2022150091"

# cookie = ""
cookie = "_WEU=qggsnUO1E7TZLQE4IGPyofwDF7aAx9XKcCtNm35LMCBqyAFzzc_Q6HYMmB78hrjx; JSESSIONID=266BC0ABBF5B3A161870DFFE521FFC2D; route=2e7b4a35a31c5a6d82a1048539c55f40; insert_cookie=22322123"
electiveBatchCode = "3e05cb5370a2428f991fa902fe078b66"

token = "63824583-6d06-4528-8c16-4cf3bda64226"

# 本班课程： 'TJKC'
# 方案内课程: 'FANKC'
# 方案外课程： 'FAWKC'
# 校公选课： 'XGXK'
# 慕课: "ＭOOC"，
# 辅修课程: "FXKC"，
# 体育课程:"TYKC"
# 你要抢的课程，按照如下格式提前先填写好
courses = [
    # {'id': '202420251150291000101', 'type': 'TJKC', 'name': "计算机安全导论"},
    # {'id': '202420251150289000101', 'type': 'TJKC', 'name': "微处理器与机器人"},
    # {'id': '202420251150280000101', 'type': 'TJKC', 'name': "自动机与形式语言"},
    # {'id': '202420251150280000101', 'type': 'FANKC', 'name': "自动机与形式语言"},
    {'id': '202420251150329000101', 'type': 'FANKC', 'name': "智能识别系统设计"},
    {'id': '202420251150465000101', 'type': 'FANKC', 'name': "计算机视觉"},
]

# 抢课的间隔，单位是毫秒
delay:int = 60*1000

# 抢课的次数
count:int = 10*60*60*1000//delay




########## 以上需要用户自行配置 ############

########## 请不要修改下面的配置  ############

url:str = "http://bkxk.szu.edu.cn/"

headers:map =  {
    "Cookie": cookie.strip(),
    "token": token.strip(),
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "bkxk.szu.edu.cn",
    "Pragma": "no-cache"
}


