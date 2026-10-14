#1
# import math
# r=float(input("Введіть радіус :"))
# surplace=math.pow(r,2)*math.pi
# print(round(surplace,2))
#
# a,b= map(int,input("Введіть значення двох катетів:").split())
# gipotenusa=math.pow(a,2)+math.pow(b,2)
# gipotenusa1=math.sqrt(gipotenusa)
# print(round(gipotenusa1,2))
#
# items=int(input("Введіть кількість:"))
# boxes=int(input("ВВедіть кількість боксів: "))
# kilkist= math.ceil(items/boxes)
# print(round(kilkist,2))

#2
# import statistics as stat
# import random
# n = int(input("Введіть кількість оцінок:"))
# grades =[]
# count=0
# for i in range(1,n+1):
#     grade= random.randint(1,12)
#     grades.append(grade)
#     if grade >=10:
#         count+=1
# print(grades)
# print("Мінімальне значення :",min(grades))
# print("Максимальне значення:",max(grades))
# print("Середнє арифметичне:",stat.mean(grades))
# print("Медіана:", stat.median(grades))
# print("к-сть оцінок 10-12:",count)

#3
# import datetime
# today = datetime.date.today()
# event=datetime.date(2026,12,31)
# diff= event-today
# if diff.days>0:
#     print("Ця дата наступить")
# elif diff.days<0:
#     print("Ця дата вже наступила")
# else:
#     print("сьогодні")

#4
import student_utils
import tkinter as tk
students=["Anna", "Ivan", "Olha"]
count=int(input("Введіть к-сть оцінок: "))
for student in students:
    grades=student_utils.generate_grades(count)
    average=student_utils.average_grades(grades)
    level=student_utils.get_level(average)
    print(f'Студенти {students},їз оцінки {grades},середнє {average},їх рівень знань { level}')





