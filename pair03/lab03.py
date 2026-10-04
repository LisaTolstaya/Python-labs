#1
# text= input("Введіть текст:")
# golosni="aeiouAEIOU"
# golosni_count = 0
# digit = 0
# bukvy = 0
# space = 0
# slova = text.split()
# slova_counts=len(slova)
# symbols_text=len(text)
# for char in text:
#     if char in golosni:
#         golosni_count +=1
#     if char.isdigit():
#         digit += 1
#     if char.isalpha():
#         bukvy +=1
#     if char==" ":
#         space+=1
# print("Символи:",symbols_text)
# print("Літери:",bukvy)
# print("Голосні:",golosni_count)
# print("Цифри:",digit)
# print("Пробілів:", space)
# print("Слова:",slova_counts)

#2
# text = input("Введіть ПІБ:")
# parts= text.split()
# if len(parts) ==3:
#     prizvyshe= parts[0].capitalize()
#     imya=parts[1][0].capitalize()
#     batko=parts[2][0].capitalize()
#     result=prizvyshe+" "+imya+"."+batko+"."
#     print(result)
# else:
#     print("Введіть 3 слова")

#3
# text1= input("Введіть перше слово:")
# text2= input("Введіть друге слово:")
# a = text1.lower().replace(" ","")
# b = text2.lower().replace(" ","")
# if sorted(a)==sorted(b):
#     print("Рядки є анаграмами.")
# else:
#     print("Рядки не є анаграмами.")

#4
# text = input("Введіть речення:")
# zamina = input("Яке слово замінити :")
# new_word=input("Додайте нове слово:")
# words=text.split()
# longest=words[0]
# smallest=words[0]
# for word in words:
#     if len(word)>len(longest):
#         longest=word
#     if len(word)<len(smallest):
#         smallest=word
# for char in range(len(words)):
#     if words[char]==zamina:
#         words[char]=new_word
# update_text = " ".join(words)
# print("Найдовше слово:",longest)
# print("Найкоротше слово:",smallest)
# print("Нове речення:",update_text)





