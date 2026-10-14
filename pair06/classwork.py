import math
from math import *
import statistics as stat
import random
from datetime import date
import demo
from tkinter import*









# # print(math.sqrt(81))
# # a = [10,15,3,5,8,9]
# # print(f'Середній бал: {stat.mean(a)}')
# # r = int(input("r="))
# # circle_area=round(pi*pow(r,2))
# #
# # print(circle_area)
#
# # balls=25
# # n=6
# # from math import*
# # print(f'Повністю заповнені: {floor(balls/n)}')
# # print(f'Всього: {ceil(balls/n)}')
# #
# # numbers=[]
# # for i in range(10):
# #     numbers.append(random.randint(1,100))
# # print(numbers)
# # selected = random.choice(numbers)
# # print(selected)
#
# # print(f'Сьогодні:{date.today()}')
#
# print(demo.square(5))
# print(demo.is_even(7))
# grades = [12,5,7,9]
# print(demo.average(grades))

def text():

    lbl_text['text'] = 'hello world'
def clear():
    lbl_text['text'] =''

window = Tk()
window.title('my first window')
window.geometry('500x400')
window.resizable(False, False)
window['bg']= "#F19CBB"
label = Label(window,text="Супер-пупер програма",font=("Arial",18),bg="#F19CBB", pady=20)
#label.place(x=0, y=0)
label.pack()
frame = Frame(window, bg="#F19CBB")
frame.pack()
bt1 = Button(frame, text='OK')
bt1.grid(row=0,column=0)
bt2 = Button(frame, text='Cancel',activebackground="lightgreen")
bt2.grid(row=0,column=1,padx=10)
bt2.bind("<Button-1>",clear)
lbl_text = Label(frame, text='', font=('Arial,18'))
lbl_text.grid(row=1, column=0, columnspan=2)

window.mainloop()










