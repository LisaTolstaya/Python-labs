#1
#num=[12,3, 4, 14, -12, 5, 10, 16, -4]
# print("Мінімальне значення: ",min(num))
# print("Максимальне значення: ",max(num))
# print("Сума: ",sum(num))
# print("Середнє: ",round(sum(num)/len(num),2))
# pos=[]
# neg=[]
# parni=[]
# divby3=[]
# for n in num:
#     if n>0:
#         pos.append(n)
#     elif n<0:
#         neg.append(n)
#     if n%2==0:
#         parni.append(n)
#     if n%3==0:
#         divby3.append(n)
# print(pos)
# print(neg)
# print(parni)
# print(divby3)

#2
# group1={'Anna','Ivan','Olha'}
# group2={'Ivan','Maksym','Olha'}
# print("Усі: ",group1|group2 )
# print("Є в обох группах: ", group1 & group2)
# print("Тільки group1: ", group1 - group2)
# print("Тільки group2: ", group2 - group1)

#3
# prices = {'fish':200, 'milk':30, 'apples':50}
# prices['milk']=48
# prices['tea']=75
# print(prices.get("chocolate", "Товар не знайдено"))
#
# for name, price in prices.items():
#     if price <= 100 and price >= 40:
#         print(f"{name} - {price} грн")

#4
# group_info=('10-IT','2026/2027')
# print(group_info)
# best_student=""
# best_average=0
# zyrnal={
#     "Anna":[10, 11, 12, 9, 10],
#     "Ivan":[8, 9, 10, 11, 9]
# }
# zyrnal['Katya']= [6, 7, 10, 11, 9]
# print(zyrnal)
# for name, grades in zyrnal.items():
#     average=sum(grades) / len(grades)
#     print(name, round(average,1))
#     if average>best_average:
#         best_average=average
#         best_student=name
# print("Найкращий учень:",best_student)


