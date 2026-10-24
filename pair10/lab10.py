#1
# class Person:
#     def __init__(self,name):
#         self.name = name
#     def info(self):
#         return f'Імя: {self.name}'
# class Student(Person):
#     def __init__(self,name,group):
#         super().__init__(name)
#         self.group = group
#     def info(self):
#         return f'Учень:{self.name},Група: {self.group}'
#
# student1=Student("Anna Ivanenko", "IT-10")
# student2=Student("Tanya Shevchenko", "IT-20")
# print(student1.info())
# print(student2.info())

#2
# class Person:
#     def __init__(self,name):
#         self.name = name
#     def info(self):
#         return f'Імя: {self.name}'
# class Student(Person):
#     def __init__(self,name,group):
#         super().__init__(name)
#         self.group = group
#     def info(self):
#         return f'Учень:{self.name},Група: {self.group}'
# class Teacher(Person):
#     def __init__(self,name,subject):
#         super().__init__(name)
#         self.subject = subject
#     def info(self):
#         return f'ПІБ:{self.name},Предмет:{self.subject}'
# people=[
#     Student("Anna Ivanenko", "IT-10"),
#     Student("Tanya Shevchenko", "IT-20"),
#     Person('Danya'),
#     Teacher("Olha Olexandrivna","math")
# ]
#
# for person in people:
#     print(person.info())

#3
class Person:
    def __init__(self,name):
        self.name = name

class Student:
    def __init__(self,name):
        self.name=name

class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject
class Course:
    def __init__(self,title,teacher,students):
        self.title=title
        self.teacher=teacher
        self.students=students
    def add_student(self,student):
        for s in self.students:
            if s.name == student.name:
                return f'Такий студент є вже у списку'
        self.students.append(student)
    def remove_student(self,name):
        for student in self.students:
            if student.name.lower() == name.lower():
                self.students.remove(student)
                return True
        return False
    def show_students(self, name):
        for student in self.students:
            print(student.name)
    def info(self):
        print(f'Курс:{self.title}')
        print(f'Викладач :{self.teacher}')
        print(f'Студенти:')
        for student in self.students:
            print(student.name)

teacher=Teacher('Olena Mykolaivna','Python')
course=Course('Python','Olena Mykolaivna',[Student('Oleg'),Student('Tanya')])
s1=Student('Anna')
s2=Student('Olha')
s3=Student('Petro')
s4=Student('Andriy')
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
course.add_student(s4)
course.remove_student(s1.name)
course.info()





















