#1
from functools import total_ordering
# total = 0
# count = 0
# avr = 0
# for i in range(1, 21):
#      if i %3==0 or i % 5 == 0:
#          total += i
#          count += 1
# if count >0:
#      avr = round(total/count, 2)
# print("Сума чисел кратних 3 і 5:", total)
# print("Кількість чисел кратних 3 і 5:", count)
# print("Середнє значення чисел кратних 3 і 5:", avr)

#2

# total= 0
# count= 0
# max_digit = 0
# min_digit = 9
# n = int(input("N: "))
# if n== 0:
#     total= 0
#     count= 1
#     max_digit = 0
#     min_digit = 0
# else:
#     while n > 0:
#         digit = n % 10
#         total += digit
#         count += 1
#         if digit > max_digit:
#             max_digit = digit
#         if digit < min_digit:
#             min_digit = digit
#         n //=10
# print("кількість цифр,: ", count)
# print("суму цифр: ",total)
# print("максимальна цифра: ",min_digit)
# print("мінімальна цифра: ",max_digit)

#3
# n = int(input("N: "))
# for i in range(1, n+1):
#     num = i
#     sen = True
#     while num >0:
#         digit= num % 10
#         if digit ==0 or i % digit !=0:
#             sen = False
#             break
#         num //=10
#     if sen:
#         print(i)

#4
# height = int(input("висота: "))
# width = int(input("ширина: "))
# symbc = (input("символ контуру: "))
# symbf = (input("символ внутрішньої частини: "))
# if width< 3 or height < 3:
#     print("Помилка")
# else:
#     for row in range(height):
#         for col in range(width):
#             if row == 0 or row == height - 1 or col == 0 or col == width - 1:
#                 print(symbc, end="")
#             else:
#                 print(symbf, end="")
#         print()







