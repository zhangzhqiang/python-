# #! /usr/bin/env python
# # -*- coding: utf-8 -*-
# # __author__ = "Q1mi"
# # Email: master@liwenzhou.com
# # Date: 2022-01-02
#
# """
# [ ] 实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败!
# [ ] 实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
# [ ] 实现用户输入用户名和密码,当用户名为 seven 或 alex 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
# """
#
# count = 1
#
# while True:
#     username = input("用户名：").strip()
#     password = input("密码:").strip()
#
#     if count < 3:
#         if password == "123":
#             if username.lower() == "seven" or username.lower() == "alex":
#                 print("登录成功")
#                 break
#             else:
#                 print("登录失败,剩余{}次机会".format(3 - count))
#         else:
#             print("登录失败,剩余{}次机会".format(3-count))
#     else:
#         break
#     count += 1
#
# """
# 使用 while 循环实现输出 1,2,3,4,5, 7,8,9, 11,12
#
# 使用while 循环输出100-50，从大到小，如100，99，98…，到50时再从0循环输出到50，然后结束
#
# 使用 while 循环实现输出 1-100 内的所有奇数
#
# 使用 while 循环实现输出 1-100 内的所有偶数count = 0
#
# 使用while循环实现输出2-3+4-5+6…+100 的和
# """
#
# # # 1.
# # count = 0
# # while count < 12:
# #     count += 1
# #     if count == 6 or count == 10:
# #         pass
# #     else:
# #         print(count)
# #
# # # 2.
# # count = 100
# # num = 0
# # while True:
# #     if count > 50:
# #         print(count)
# #         count -= 1
# #     else:
# #         print(num)
# #         num += 1
# #         if num > 50:
# #             break
# #
# # # 3.
# # count = 100
# # while count > 0:
# #     if count % 2 == 1:
# #         print(count)
# #     count -= 1
# #
# # count = 100
# # while True:
# #     count -= 1
# #     if count % 2 == 1:
# #         print(count)
# #     if count == 0:
# #         break
# #
# # count = 0
# # while count < 100:
# #     if count % 2 == 0:
# #         print(count)
# #     count += 1
# #
# # count = 2
# # total = 0
# #
# # while count <= 100:
# #     if count % 2 == 0:
# #         total += count
# #     elif count % 2 == 1:
# #         total -= count
# #     count += 1
# # print(total)
#
# # n1 = 123456
# # n2 = n1
# # n1 = 333
# # print(n1, n2)
# # print(id(n1))
# # print(id(n2))
#
#
# """
# 需求：等待用户输入名字、地点、爱好，根据用户的名字和爱好进行任意显示
#
# 如：敬爱可爱的xxx，最喜欢在xxx地方干xxx
# """
# username = input("姓名：")
# addr = input("地点：")
# hobbit = input("爱好：")
# print("敬爱的 %s,最新欢在 %s地方干%s" % (username, addr, hobbit))
#
# """
# 输入一年份，判断该年份是否是闰年并输出结果。（编程题）
#
# 注：凡符合下面两个条件之一的年份是闰年。 （1） 能被4整除但不能被100整除。 （2） 能被400整除。
# """
# while True:
#     year = input("输入年份：")
#     if year.isdigit():
#         pass
#     if int(year) % 4 == 0 and int(year) % 100 != 0:
#         print("%s是闰年" % year)
#     elif int(year) % 400 == 0:
#         print("%s是闰年" % year)
#     else:
#         print("%s是平年" % year)
#
# year = 0
# salary = 10000
# rate = 0.0325
#
# while salary < 20000:
#     year += 1
#     instance = year * rate
#     salary += instance
#     print("过了 %s年，%s的利息能翻到 %s" % (year, rate, salary))
#
# count = 0
# while count < 10:
#     count += 1
#     if count <= 5:
#         print(count * "*")
#     else:
#         print((10 - count) * "*")
#
# """一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？"""
# height = 100
# times = 0
# total = 0
#
# while times < 10:
#     times += 1
#     new_height = height / 2
#     total += 2 * new_height
#     height += new_height
# print("经过了%s次,共经过了%s米反弹%s米" % (times, new_height, total+100))
#
# height = 100
# times = 0
# total = 0
#
# while times < 10:
#     times += 1
#     new_height = height / 2
#     height = new_height
#     total += 2 * new_height
# print("第%s次落地是 %s米，共经过 %s米" % (times, new_height, total + 100))
#
# """双色球彩票 选购程序
#
# 1 双色球（假设一共八个球，6个红球，球号1-32、2个蓝球，球号1-16）
# 2 确保用户不能重复选择，不能超出范围
# 3 用户输入有误时有相应的错误提示
# 4 最后展示用户选择的双色球的号码"""
#
# red_list = []
# count = 0
# while count < 6:
#     choice = input("请选择红号球：").strip()
#     if choice.isdigit():
#         if choice in red_list:
#             print("%s已经存在，请重新选择" % choice)
#             continue
#         elif int(choice) > 32 or int(choice) < 0:
#             print("球号超出范围")
#             continue
#         red_list.append(choice)
#         count += 1
#     else:
#         print("输入错误")
#
# blue_list = []
# num = 0
# while num < 2:
#     choice = input("请选择蓝号球：").strip()
#     if choice.isdigit():
#         if choice in blue_list:
#             print("%s已选择" % choice)
#             continue
#         elif 16 > int(choice) > 0:
#             blue_list.append(choice)
#             num += 1
#         print("球号超出范围")
#         continue
#     else:
#         print("输入错误")
# print(blue_list)
# print(red_list)

# continue打印1-10，不打印7
# count = 1
# while count < 11:
#     print(count)
#     if count == 7:
#         count += 1
#         continue

count = 1
total = 0
while count < 101:
    if count % 2 == 1:
        total += count
    elif count % 2 == 0:
        total -= count
    count += 1
print(total)




