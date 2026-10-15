import os
if not os.path.exists('text.txt'):
    with open('text.txt', 'w', encoding="utf-8") as file:
        file.write("Python - популярна мова програмування.\n")
        file.write("Python використовується для роботи з даними.\n")
        file.write("Файли дозволяють зберігати інформацію\n")
        file.write("Python вимагає практики.\n")
        file.write("Сьогодні ми працюємо з текстовими файлами.\n")

if not os.path.exists('numbers.txt'):
    with open('numbers.txt', 'w', encoding="utf-8") as file:
        file.write("12\n8\n25\n4\n16\n")

if not os.path.exists('students.txt'):
    with open('students.txt', 'w', encoding="utf-8") as file:
        file.write("Ivanenko Anna;91\n")
        file.write("Leshchenko Ivan;76\n")
        file.write("Komarova Sophie;97\n")
        file.write("Bondarenko Illya;84\n")

if not os.path.exists('grades.csv'):
    with open('grades.csv', 'w', encoding="utf-8") as file:
        file.write("Anna;Python;11\n")
        file.write("Anna;Math;10\n")
        file.write("Ivan;Python;6\n")
        file.write("Ivan;Math;5\n")
        file.write("Sophie;Python;11\n")
        file.write("Sophie;Math;12\n")
        file.write("Illya;Python;9\n")
        file.write("Illya;Math;8\n")


# with open('hello.txt','w',encoding="utf-8" ) as file:
#     file.write("Hello world!\n")

# with open ("text.txt","r", encoding="utf-8") as file:
#     text=file.read()
# print(f'read()=>{text}, len()=>{len(text)}')

# with open ("text.txt","r", encoding="utf-8") as file:
#     line1=file.readline()
#     other_line = file.readlines()
#     line2=file.readline()
#
# print(line1)
# print(other_line)
# print(line2)
#
# with open ("text.txt","r",encoding="utf-8") as file:
#     other_lines=file.readlines()
# for line in other_lines:
#     print(line)

# with open ("text.txt","r",encoding="utf-8") as file:
#     for number, line in enumerate(file, start=1):
#         clean_line=line.strip()
#         print(number, line)
#         print(f'{number}. {clean_line}')

# line= "Tolstaya Lisa;10\n"
# clean_line=line.strip()
# name, grade=line.split(';')
# print(name, grade)

# student =[]
# botanics=[]
# with open ('students.txt', 'r', encoding="utf-8") as file:
#     for line in file:
#         name,grade=line.strip().split(';')
#         student.append([name,grade])
#         if int(grade)>=90:
#             botanics.append([name, grade])
# print(student)
# print(botanics)
# with open ('botanics.txt', 'w', encoding="utf-8") as file:
#      for name, grade in botanics:
#         file.write(name + ';' + grade + '\n')

# grades=[]
# with open("grades.csv", "r", encoding="utf-8") as file:
# for line in file:
#     name,subject,grade=line.strip().split(';')
#     grades.append(grade)
#     print(f'{name} {subject} {grade}')
# average= sum(grades)/len(grades)

# with open("hello.txt", "w", encoding="utf-8") as file:
#     file.write("Привіт, Python!\n")

# with open("log.txt", "w", encoding="utf-8") as file:
#     file.write("Перший запуск\n")
# with open("log.txt", "a", encoding="utf-8") as file:
#     file.write("Новий запис\n")
# 3
# with open("hello.txt", "r", encoding="utf-8") as file:
#     text = file.read()
# print(text)

# 4
# with open("text.txt", "r", encoding="utf-8") as file:
#     text = file.read()
# print(text)
# print("Символів:", len(text))

# 5
# with open("text.txt", "r", encoding="utf-8") as file:
#     for number, line in enumerate(file, start=1):
#         print(f"{number}: {line.strip()}")

# 6
# with open("text.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         clean_line = line.strip()
#         print(clean_line)

# 7
# numbers = []
# with open("numbers.txt", "r", encoding="utf-8") as file:
#     for line in file:
#          numbers.append(int(line.strip()))
# print("Min:", min(numbers))
# print("Max:", max(numbers))
# print("Sum:", sum(numbers))
# print("Average:", sum(numbers) / len(numbers))

# 8
# with open("students.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         name, score = line.strip().split(";")
#         print(name, int(score))

# 9
# line = "Anna;Python;11"
# name, subject, grade = line.split(";")
# print("Учень:", name)
# print("Предмет:", subject)
# print("Оцінка:", int(grade))

# 10
# selected = []
# with open("students.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         name, score = line.strip().split(";")
#         score = int(score)
#         if score > 80:
#             selected.append([name, score])
# print(selected)

# 11
# students = [
# ["Anna", 91],
# ["Ivan", 84],
# ["Olha", 97]
# ]
# students.sort(key=lambda student: student[1], reverse=True)
# for student in students:
#     print(student[0], student[1])

# 12
# students = [
# ["Olha", 97],
# ["Anna", 91],
# ["Ivan", 84]
# ]
# with open("result.txt", "w", encoding="utf-8") as file:
#     for name, score in students:
#         print(f"{name};{score}", file=file)
# print("Звіт result.txt створено.")









