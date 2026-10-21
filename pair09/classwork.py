# book_dict={
#     'title':'Кобзар',
#     'author':'Тарас Шевченко',
#     'copies':15
# }
#
# print(book_dict['title'])

# class Book:
#     def __init__(self,title,price, copies):
#         self.title=title
#         self.price=price
#         self.copies=copies
#     def available(self):
#         return self.copies>0
#
# book1=Book('Кобзар',450,15)
# book2=Book('Лісова пісня',500,0)
# # print(book1.title, book1.price)
# # print(book2.title, book2.price)
#
# print(f' Кобзар доступний {book1.available()}')
# print(f' Лісова пісня доступна {book2.available()}')

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def perimetr(self):
#         return 2*(self.width+self.height)
#     def area(self):
#         return self.width * self.height
#     def info(self):
#         print(f'Розміри прямокутника : {self.width} x {self.height} ')
#         print(f'S={self.area()}')
#         print(f'P={self.perimetr()}')
# a=int(input('Ііедіть ширину'))
# b=int(input('Введть висоту'))
# rectangle=Rectangle(a, b)
# rectangle.info()

#1
# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
# student = Student("Anna", [10, 11, 12])
# print(student.name)
# print(student.grades)

#2
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
# student1=Student("Anna")
# student2=Student("Ivan")
# print(student1.name)
# print(student2.name)

#3
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
#     def add_grade(self,grade):
#         if 1<= grade <= 12:
#             self.grades.append(grade)
#         else:
#             print("Оцінка повинна бути від 1 до 12")
#
# student=Student("Anna")
# student.add_grade(11)
# student.add_grade(15)
# print(student.grades)

#4
# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#     def average(self):
#         if len(self.grades) == 0:
#             return 0
#         return sum(self.grades) / len(self.grades)
# student = Student("Anna", [10, 11, 12])
# print(student.average())

#5
# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#     def average(self):
#         if not self.grades:
#             return 0
#         return sum(self.grades) / len(self.grades)
#     def info(self):
#         print("ПІБ:", self.name)
#         print("Оцінки:", self.grades)
#         print("Середній:", round(self.average(), 2))
# student = Student("Ivan Petrenko", [8, 10, 11])
# student.info()

#6
# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#     def __str__(self):
#         return f"{self.name}: {self.grades}"
# student = Student("Olha", [12, 11, 12])
# print(student)

#7
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# students = [
#     Student("Anna", [10, 11, 12]),
#     Student("Ivan", [8, 9, 10]),
#     Student("Olha", [12, 12, 11])
# ]
# print("Кількість учнів:", len(students))

#8
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# students = [
#     Student("Anna", [10, 11, 12]),
#     Student("Ivan", [8, 9, 10]),
#     Student("Olha", [12, 12, 11])
# ]
# for student in students:
#     print(student.name)
#     print(student.grades)

#9
# class Student:
#     def __init__(self, name,grades ):
#         self.name = name
#         self.grades = []
#     def average(self):
#         if not self.grades:
#             return 0
#         return sum(self.grades)/len(self.grades)
# students = [
#     Student("Anna", [10, 11, 12]),
#     Student("Ivan", [8, 9, 10]),
#     Student("Olha", [12, 12, 11])
# ]
# best_student = students[0]
# for student in students:
#     if student.average() > best_student.average():
#         best_student = student
# print("Найкращий учень:", best_student.name)
# print("Середній:", round(best_student.average(), 2))

#10
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
# product = Product("Keyboard", 1200, 3)
# print(product.name)
# print(product.price)
# print(product.quantity)

#11
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def total_cost(self):
#         return self.price * self.quantity
# product = Product("Mouse", 650, 4)
# print("Загальна вартість:", product.total_cost())


# #12
# # Через словник
# product_dict = {
#     "name": "Monitor",
#     "price": 7000,
#     "quantity": 2
# }
# dict_total = product_dict["price"] * product_dict["quantity"]
# # Через клас
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def total_cost(self):
#         return self.price * self.quantity
# product = Product("Monitor", 7000, 2)
# print("Словник:", dict_total)
# print("Об'єкт:", product.total_cost())
















