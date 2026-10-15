# #1
# rows=0
# words=0
# symbols=0
# max_line=0
# number_the_greater=0
# text_the_greater=""
# now=0
# with open('text.txt','r', encoding="utf-8") as file:
#     for line in file:
#         now+=1
#         rows+=1
#         words_in_line=line.split()
#         words += len(words_in_line)
#         symbols+=len(line)
#         clean_line=line.strip()
#         lenght=len(clean_line)
#         if lenght>max_line:
#             max_line=lenght
#             number_the_greater=now
#             text_the_greater=clean_line
# print(f' Зараз:{now}, Рядок:{rows}, К-сть слів:{words}, К-сть символів:{symbols}, Найбільший рядок:{max_line}, Його номер:{text_the_greater}')


#2
# word=input("ВВедіть слово")
# with open("text.txt","r", encoding="utf-8") as file:
#     lines=file.readlines()
#     for line_number, line in enumerate(lines,1):
#         if word in line.lower():
#             print(f'номер строки {line_number}: {line.strip()}')
#         else:
#             print('Немає таких слів у списках')

#3
with open('students.txt', 'r',encoding="utf-8") as file:
    lines=file.readlines()
A_students=[]
stud=[]
for line in lines:
    if ';' not in line:
        continue
    name,grade = line.strip().split(';')
    stud.append([name,grade])
    if int(grade)>80:
        A_students.append([name,int(grade)])
        A_students.sort(reverse=True)
        print(f'Імя:{name},оцінка:{grade}')







