#1
# def circle_area(r):
#     pi = 3.14159
#     return pi * (r **2)
# def rectangle_area(width, height):
#     return width * height
# def triangle_area(height, side):
#     return 0,5 * side *height
# def main():
#     choice = input("Оберіть:коло/прямокутник/трикутник")
#     if choice == "коло":
#         r=float(input("радіус:"))
#         print(f'Площа {circle_area(r)}')
#     elif choice=="прямокутник":
#         width = float(input("Ширина:"))
#         height = float(input("Довжина:"))
#         print(f'Площа {rectangle_area(width, height)}')
#     elif choice =="трикутник":
#         side=float(input("Сторона:"))
#         height=float(input("Висота:"))
#         print(f'Площа {triangle_area(height,side)}')
# main()

#2
# def is_primen(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#         else:
#             return True
# def divirsion(n):
#     result=[]
#     for i in range(1,n+1):
#         if n%i==0:
#             result.append(i)
#     return result
# def digit_sum(n):
#     total=0
#     for i in str(n):
#         total+=int(i)
#     return total
# def main():
#     n=int(input("Введіть число: "))
#
#     print(f'Просте число: {is_primen(n)}')
#     print(f'Дільники: {divirsion(n)}')
#     print(f'Сума цифр: {digit_sum(n)}')
# main()

#3
def average(grades):
    return sum(grades)/len(grades)
def minimun(grades):
    return min(grades)
def maximun(grades):
    return max(grades)
def count_above(grades, value):
    count=0
    for grade in grades:
        if grade > value:
            count+=1
    return count
def main():
    grades=[10,8,12,9,11]
    value=9
    print(f'Середнє: {average(grades)}')
    print(f'Мінімальне: {minimun(grades)}')
    print(f'Максимальне: {maximun(grades)}')
    print(f'Кількість: {count_above(grades, value)}')

main()



















