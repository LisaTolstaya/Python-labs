# def say_hello():
#     print("hello world")
#
# say_hello()

# def say_hello(name):
#     print(f'hello {name}!')
# say_hello('Lisa')
# say_hello('Alisa')

# def rectangle_area(width,height):
#     return width*height
#
# width=int(input("ВВедіть ширину"))
# height=int(input("Введіть висоту"))
#
# S=rectangle_area(width,height)
# print(f"Площа= {S} см2")

# def hello_world(name,message):
#     print(f'Hello {name},your message is: {message}')
# hello_world('Lisa','URAA')

# def price_with_discount(price, discount=0):
#     return price-price*discount/100
# print(price_with_discount(1000,10))

# def min_max(numbers):
#     return min(numbers), max(numbers)
#
#
# numbers=[1,2,3,4,5,6,7,8,9,10]
# min_,max_=min_max(numbers)
# print(min_max(numbers))

# def is_even(num):
#     """Повертає True якщо парне """
#     return num % 2 == 0
# print(is_even(3))
#
# def rectangle_area(width,height):
#     return width*height
#
# def main():
#     width=7
#     height=5
#
#     print(f'Ширина,{width} ')
#     print(f'Довжина,{height}')
#     result = rectangle_area(width,height)
#     print(f'Surplace of rectangle {result}')
# main()

#1
# def say_hello():
#     print("Привіт,Python!")
# say_hello()

#2
# def greet(name):
#     print(f"Привіт, {name}!")
# greet("Ivan")

#3
# def area_rectangle(a, b):
#     return a * b
# area = area_rectangle(7, 4)
# print("Площа:", area)

#4
# def square_print(x):
#     print(x * x)
# def square_return(x):
#     return x * x
# square_print(5)
# result = square_return(5)
# print("Результат можна використати:", result + 10)
#

#5
# def greet(name, message="Привіт"):
#     print(f"{message}, {name}!")
# greet("Anna")
# greet("Ivan", "Добрий день")

#6
# def student_info(name, group, grade):
#     print(f"{name}: група {group}, оцінка {grade}")
# student_info(grade=11, name="Anna", group="10-IT")

#7
# def min_max(numbers):
#     return min(numbers), max(numbers)
# minimum, maximum = min_max([7, 2, 15, 4, 9])
# print("Min:", minimum)
# print("Max:", maximum)

#8
# def is_valid_grade(grade):
#     return 1 <= grade <= 12
# grade = int(input("Оцінка: "))
# if is_valid_grade(grade):
#     print("Коректна оцінка")
# else:
#     print("Помилка")

#9
# def average(numbers):
#     return sum(numbers) / len(numbers)
# def count_positive(numbers):
#     count = 0
#     for number in numbers:
#         if number > 0:
#             count += 1
#     return count
# numbers = [4, -2, 8, 0, 5]
# print("Середнє:", average(numbers))
# print("Додатних:", count_positive(numbers))

#10
# def total_sum(*numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total
# print(total_sum(5, 10))
# print(total_sum(1, 2, 3, 4, 5))

#11
# def area_rectangle(a, b):
#     return a * b
# def main():
#     width = float(input("Ширина: "))
#     height = float(input("Висота: "))
#     result = area_rectangle(width, height)
#     print("Площа:", result)
# main()

#12
# def input_grades():
#     return [10, 8, 12, 9, 11]
# def average(grades):
#     return sum(grades) / len(grades)
# def best_grade(grades):
#     return max(grades)
# def print_report(grades):
#     print("Оцінки:", grades)
#     print("Середній бал:", round(average(grades), 2))
#     print("Найкраща оцінка:", best_grade(grades))
# def main():
#     grades = input_grades()
#     print_report(grades)
# main()



