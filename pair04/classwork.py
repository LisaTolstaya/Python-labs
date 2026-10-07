#list-#spysok vporyadkovana zminna kolektsia
# grades = [12, 4, 6, 9]
# numbers=[]
# # numbers2=list()
# # print(grades[2])
# # grades[2]=12
# numbers.append(5)
# numbers.append(6)
# numbers.insert(1,2)
# numbers.extend([3,7,5,4])
# numbers.remove(5)
# numbers.pop(-1)
# print(numbers)
# # numbers.clear()
# print(numbers.count(5))
# print(numbers.index(6))
# print(5 in numbers)
# if len(numbers)>0:
#     average= sum(numbers)/len(numbers)
# print(average)
# numbers.sort()
# print(numbers.sort())
# numbers.reverse()
# print(numbers.reverse())
# print(numbers[1:3])
# print(numbers[::-1])
#
# for number in numbers:
#     print(number)

# digits=[-1, 0, 4, -5,3,-6]
# dodatni=list()
# parni=list()
# for digit in digits:
#     if digit>0:
#         dodatni.append(digit)
#     if digit%2==0:
#         parni.append(digit)
# print(dodatni)
# print(parni)




#tuple-kortezh
# rgb=(255, 0, 0)
# r,g,b=rgb
# print(r, g, b)
# data= ()
# a=(1,)
# a = (30,40)
# b=(50,60)
# c = a+b
# c= a[:1]+ b[::]

# point = (4, -6, )
# point = point +(4,)



# #set-mnozhyna
# subjects={"python","html","CSS","html"}
# print(subjects)
# data= {}
# print(type(data))
# data2 = set()
# data2.add("JS")
# data2.update(["C++","Java"])
# deleted = data2.pop()
#
# print(data2)

#1
# names={"Ivan","Olha","Vadym", "Ivan", "Irina"}
# new_names=set(names)
# print(new_names)
#2
# names1={"Ivan","Ivan","Irina"}
# names2={"Olha","Vadym","Irina"}
# names3=names1|names2
# print(names3)
# names4=names1&names2
# print(names4)
# names5=names1-names2
# names6=names2-names1
# print(names5)
# print(names6)

# #dict-slovnyk
# products=["bread", "milk", "apple", "banana"]
# prices= [30,50,50,80]
# prices = {
#     'apple':50,
#     'banana':70,
#     'milk':30
# }
# # students = {}
# print(prices['apple'])
# prices['tea']=75
# prices.update(
#     {
#         'juice':50,
#         'coffe':70
#
#     }
# )
#
# print(prices)

#2.1
# grades = [10, 8, 12, 9]
# print(grades[0])
# grades.append(11)
# grades[1]=9
# print(grades)

#2.2
# numbers = [12, 3, 4, 14, -12, 5, 10, 16, -4]
# positive = []
# for number in numbers:
#     if number > 0:
#         positive.append(number)
# print("Додатні:", positive)
# print("Min:", min(numbers))
# print("Max:", max(numbers))
# print("Сума:", sum(numbers))

#2.3
# point = (10, 25)
# x, y = point
# print("x =", x)
# print("y =", y)

#2.4
# group1 = {"Anna", "Ivan", "Olha"}
# group2 = {"Ivan", "Maksym", "Olha"}
# print("Спільні:", group1 & group2)
# print("Тільки перша:", group1 - group2)
# print("Усі:", group1 | group2)

#2.5
# prices = {
#     "bread": 35,
#     "milk": 48,
#     "cheese": 120
# }
# print(prices["milk"])
# print(prices.get("coffee", "Товар не знайдено"))
# prices["bread"] = 38
# prices["tea"] = 75

#2.6
# prices = {"bread": 35, "milk": 48, "cheese": 120}
# for product, price in prices.items():
#     print(f"{product}: {price} грн")

# 2.7
# students = {
#     "Anna": [10, 11, 12, 9, 10],
#     "Ivan": [8, 9, 10, 11, 9]
# }
# for name, grades in students.items():
#     average = sum(grades) / len(grades)
#     print(name, round(average, 2))

#1
# grades = [10, 8, 12, 9, 11]
# print("Min:", min(grades))
# print("Max:", max(grades))
# print("Сума:", sum(grades))
# print("Середнє:", sum(grades) / len(grades))

#2
# numbers = [5, 2, 9, 1]
# numbers.append(7)
# numbers.remove(2)
# numbers.sort()
# print(numbers)

#3
# numbers = [12, -3, 4, -7, 10, 5]
# positive = []
# for number in numbers:
#     if number > 0:
#         positive.append(number)
# print(positive)

#5
# names = ["Ivan", "Anna", "Ivan", "Olha", "Anna"]
# unique_names = set(names)
# print(unique_names)

#6
# math = {"Ivan", "Anna", "Olha"}
# python = {"Anna", "Maksym", "Ivan"}
# print("Спільні:", math & python)
# print("Тільки math:", math - python)
# print("Усі:", math | python)

#7
# prices = {"bread": 35, "milk": 48}
# prices["cheese"] = 120
# prices["bread"] = 38
# print(prices)

#8
# prices = {"bread": 38, "milk": 48, "cheese": 120}
# for product, price in prices.items():
# print(product, "-", price, "грн")

#9
# students = {
#     "Anna": [10, 11, 12],
#     "Ivan": [8, 9, 10]
# }
# print(students["Anna"])

#10
# students = {
#     "Anna": [10, 11, 12],
#     "Ivan": [8, 9, 10]
# }
# for name, grades in students.items():
#     average = sum(grades) / len(grades)
#     print(name, round(average, 2))

#11
# students = {
#     "Anna": [10, 11, 12],
#     "Ivan": [8, 9, 10],
#     "Olha": [11, 12, 12]
# }
# best_name = ""
# best_average = 0
# for name, grades in students.items():
#     average = sum(grades) / len(grades)
#     if average > best_average:
#         best_average = average
#         best_name = name
# print("Найкращий:", best_name, round(best_average, 2))






