# -*- coding: utf-8 -*-
# 程序入口

import downloads
import setting
import time
import sys
import choose_course

if __name__ == "__main__":

    for i in range(setting.count):
        cnt = 0
        for course in setting.courses:
            try:
                response = choose_course.start_choose(course['id'], course['type'])
                if "添加选课志愿成功" in response:
                    print("抢课成功")
                    cnt += 1
                elif "非法请求" in response:
                    print(response)
                    sys.exit()
                elif "已经存在选课结果中" in response:
                    cnt += 1
                elif "该课程超过课容量" in response:
                    print(course['name'] + ": " + response)
                elif "选课系统正在初始化" in response:
                    print(response)
                    time.sleep(100)
                else:
                    print(response)
                    sys.exit()

            except KeyboardInterrupt:
                print("通过键盘中断退出程序")
                sys.exit()
            except:
                print("出现错误，请检查设置setting.py部分是否填写正确")
                print(i + 1)
                sys.exit()
        if cnt >= len(setting.courses):
            break

        time.sleep(setting.delay / 1000.0)

    print("抢课结束")

    print("======================")
    print("您现在选课的结果如下")
    choose_course.query_result()
