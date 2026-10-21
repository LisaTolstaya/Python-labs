#1
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#     def info(self):
#         print(f'Розміри:{self.width} X {self.height}', end=",")
#         print(f'S={self.area()}', end=",")
#         print(f'P={self.perimeter()}')
#
# rectangle1=Rectangle(5,3)
# rectangle2=Rectangle(10,4)
#
# rectangle1.info()
# rectangle2.info()

#2
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
#     def add_grade(self, grade):
#         if 1<=grade<=12:
#             self.grades.append(grade)
#         else:
#             print("Оцінка не в діапазоні 1-12")
#     def average(self):
#         if not self.grades:
#             return 0
#         return sum(self.grades)/len(self.grades)
#     def __str__(self):
#         return f'ПІБ:{self.name},оцінки:{self.grades},середній бал:{self.average()}'
#
# student=Student("Ivan Petrenko")
# student.add_grade(10)
# student.add_grade(12)
# student.add_grade(15)
# student.add_grade(9)
# print(f'Імя:{student.name}')
# print(f'Оцінки:{student.grades}')
# print(f'Середній бал:{round(student.average(),2)}')

#3

# class Student:
#     def __init__(self, name,grades):
#         self.name = name
#         self.grades = grades
#     def average(self):
#         if not self.grades:
#             return 0
#         return sum(self.grades)/len(self.grades)
#     def info(self):
#         print(self.name)
#         print(round(self.average(),2))
# students=[
#     Student("Katya",[5,11,12]),
#     Student("Olha",[10,7,6]),
#     Student("Petro",[8,9,7]),
#     Student("Kolya",[12,10,9]),
#     Student("Anna",[12,12,8])
# ]
# best_student=students[0]
# for student in students:
#     student.info()
#     if student.average()>best_student.average():
#         best_student=student
# print(f'Імя найкращого цчня:{best_student.name},оцінка(середня):{round(best_student.average(),2)} ')

#4
# class Wallet:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance+=amount
#             print(f'Додали:{amount}, теперішій баланс:{self.balance}')
#         else:
#             print('Значення має бути додатнім')
#     def withdraw(self, amount):
#         if amount > 0 and amount < self.balance:
#             self.balance-=amount
#             print(f'Знято:{amount},теперішій баланс:{self.balance}')
#         elif amount >self.balance:
#             print('Списання не може бути меншим за баланс')
#         else:
#             print('Не можна списати нульову або відємну суму')
#
# wallet1=Wallet("Ivan",1000)
# wallet2=Wallet("Olha",700)
# wallet1.deposit(500)
# wallet1.withdraw(300)
# wallet1.withdraw(2000)
# wallet2.withdraw(200)
# wallet2.deposit(100)









