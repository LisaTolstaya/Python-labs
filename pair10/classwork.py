# class Person:
#     def __init__(self, name):
#         self.name = name
#     def info(self):
#         return f"Name: {self.name}"
# class Student(Person):
#     def __init__(self, name, group):# дає доступ до батківського класу
#         super().__init__(name)
#         self.group = group
#     def info(self):
#         return f"Name: {self.name}, Group: {self.group}"
# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
#     def info(self):
#         return f"Name: {self.name}, Subject: {self.subject}"

# person1=Person('Vadym')
# student=Student('Lisa',"10IT")
# teacher=Teacher('',"")
# print(person1.info())
# print(student.info())

# people=[Person('Vadym'),Student('Lisa','10-It'), Teacher("Ivan","IT")]
# for person in people:
#     print(person.info())
# person2=Person('Vadym')
# print(isinstance(person2,Person))

#1
# class Person:
#     def __init__(self, name):
#         self.name = name
# person = Person("Ivan")
# print(person.name)

#2
# class Person:
#     def __init__(self, name):
#         self.name = name
# class Student(Person):
#     pass
# class Teacher(Person):
#     pass
# student = Student("Anna")
# teacher = Teacher("Olena")

#3
# class Person:
#     def __init__(self, name):
#         self.name = name
# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group
# student = Student("Anna", "IT-10")
# print(student.name, student.group)
#4
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def info(self):
#         return f"Ім'я: {self.name}"
#
# person = Person("Ivan")
# print(person.info())

#5
#  class Person:
#     def __init__(self, name):
#          self.name = name
# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group
#     def info(self):
#         return f"Учень: {self.name}, група: {self.group}"
# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
#     def info(self):
#         return f"Викладач: {self.name}, предмет: {self.subject}"

#6
# people = [
#     Person("Ivan"),
#     Student("Anna", "IT-10"),
#     Teacher("Olena", "Python")
# ]
# for person in people:
#     print(person.info())

#7
# class Person:
#     def __init__(self, name):
#          self.name = name
# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
# class Course:
#     def __init__(self, title, teacher):
#         self.title = title
#         self.teacher = teacher
#         self.students = []
# teacher = Teacher("Olena", "Python")
# course = Course("Основи Python", teacher)
#

#8
# class Person:
#     def __init__(self, name):
#          self.name = name
# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
# class Student(Person):
#     def __init__(self, name, group):
#          super().__init__(name)
#          self.group = group
#     def info(self):
#          return f"Учень: {self.name}, група: {self.group}"
# class Course:
#     def __init__(self, title, teacher):
#         self.title = title
#         self.teacher = teacher
#         self.students = []
#     def add_student(self, student):
#         self.students.append(student)
#course=Course('it','Alex')
# course.add_student(Student("Anna", "IT-10"))
# course.add_student(Student("Ivan", "IT-10"))

#9
# class Person:
#     def __init__(self, name):
#          self.name = name
# class Student(Person):
#     def __init__(self, name, group):
#          super().__init__(name)
#          self.group = group
#
#     def info(self):
#         return f"Учень: {self.name}, група: {self.group}"
# class Course:
#     def __init__(self, title, teacher):
#         self.title = title
#         self.teacher = teacher
#         self.students = []
#     def add_student(self, student):
#         self.students.append(student)
#     def remove_student(self, name):
#         for student in self.students:
#             if student.name.lower() == name.lower():
#                 self.students.remove(student)
#             return True
#         return False
# course=Course('it','Alex')
# course.add_student(Student("Anna", "IT-10"))
# course.add_student(Student("Ivan", "IT-10"))

#10
# class Person:
#     def __init__(self, name):
#          self.name = name
# class Student(Person):
#     def __init__(self, name, group):
#          super().__init__(name)
#          self.group = group
#
#     def info(self):
#         return f"Учень: {self.name}, група: {self.group}"
#
# class Cours:
#     def __init__(self, studets,title,teacher):
#         self.students=[]
#         self.title = title
#         self.teacher = teacher
#     def find_student(self, name):
#         for student in self.students:
#             if student.name.lower() == name.lower():
#                 return student
#         return None
#
# course=Cours(12,'it','Alex')
# student = course.find_student("Anna")
# if student:
#     print(student.info())
# else:
#     print("Учня не знайдено.")

#11
# class Cours:
#     def __init__(self, studets,title,teacher):
#         self.students=[]
#         self.title = title
#         self.teacher = teacher
#
#     def average_rating(self):
#         if len(self.students) == 0:
#             return 0
#         total = 0
#         for student in self.students:
#             total += student.average()
#         return total / len(self.students)

#12
class Cours:
    def __init__(self, studets,title,teacher):
        self.students=[]
        self.title = title
        self.teacher = teacher
while True:
    print("\n1 - Додати студента")
    print("2 - Показати студентів")
    print("3 - Знайти студента")
    print("0 - Вихід")
    choice = input("Ваш вибір: ")
    if choice == "1":
        name = input("ПІБ: ")
        group = input("Група: ")
    elif choice == "2":
        course.show_students()
    elif choice == "3":
        name = input("ПІБ для пошуку: ")
        student = course.find_student(name)
        if student:
            print(student.info())
        else:
            print("Учня не знайдено.")
    elif choice == "0":
        break
    else:
        print("Невідомий пункт меню.")












