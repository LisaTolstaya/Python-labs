#1
# try:
#     a=float(input("Введіть перше число"))
#     b=float(input("Введіть друге число"))
#     operation=input("Введіть операцію(+,-,*,/)")
#     if operation=="+":
#         print(a+b)
#     elif operation=="-":
#         print(a-b)
#     elif operation=="*":
#         print(a*b)
#     elif operation=="/":
#         print(a/b)
#     else:
#         raise ValueError("Операція обрана не з наявних")
#
# except ValueError as error:
#     if str(error)=="Операція обрана не з наявних":
#         print(error)
#     else:
#         print("Некоректний запис чисел")
# except ZeroDivisionError:
#     print("На 0 ділити не можна")

#2
# def input_grade(grade):
#     while True:
#         try:
#             grade = int(input("Введіть оцінку:"))
#             if grade>=1 and grade<=12:
#                 return grade
#                 break
#             else:
#                 raise ValueError("Оцінка не лежить у діапазоні від 1 до 12")
#         except ValueError as error:
#             if str(error)=="Оцінка не лежить у діапазоні від 1 до 12":
#                 print(error)
#             else:
#                 print("Не коректний запис числа")
#
# score=input_grade("Ваша оцінка:")
# print(f"Оцінка: {score} ")

#3

# students= ["Оля","Таня", "Аня"]
# subjects={"Математика":9,"Англійська":12,"Інформатика":11}
# choice= input("Введіть число(1-учень, 2-предмет)")
# if choice=="1":
#     try:
#         input_index=int(input('введіть індекс :'))
#         print(f'Учень: {students[input_index]}')
#     except IndexError:
#         print("Не коректний індекс")
#     except ValueError:
#         print("Не правильно записане число,що означає індекс")
# elif choice=="2":
#     try:
#         input_subjects=input("Введіть назву предмета:")
#         print(f'Предмет:{subjects[input_subjects]}')
#     except KeyError:
#         print("Немає шуканого предмету у словнику")
# else:
#     print("Введіть 1 або 2")

#4
normal_count=0
with_problem_count=0
normal_lines=[]
try:
    with open('students.txt', 'r', encoding='utf-8') as f:
        for number_row, line in enumerate(f, start=1):
            try:
                line=line.strip()
                if not line:
                    continue
                if ";" not in line:
                    raise ValueError('Немає ; у рядку')

                parts= line.split(";")

                name= parts[0]
                grade= int(parts[1])
                if grade<0 or grade>100:
                    raise ValueError('Поза діапазоном 0-100')
                normal_lines.append((name,grade))
                normal_count+=1
            except ValueError as error:
                with_problem_count+=1
                if str(error)=='Поза діапазоном 0-100':
                    print(f'Рядок {number_row}:{error}')
                elif str(error)=='Немає ; у рядку':
                    print(f'Рядок {number_row}:{error}')
                else:
                    print(f"Рядок {number_row}: число не ціле")
except FileNotFoundError:
    print('Файл не знайдено')

normal_lines.sort(reverse=True)
with open('report.txt', 'x', encoding='utf-8') as file:
    for grade,name in normal_lines:
        file.write(f'{name};{grade}\n')
print(f'К-сть рядків з правильним записом:{normal_count}')
print(f'К-сть рядків з неправильним записом:{with_problem_count}')



















