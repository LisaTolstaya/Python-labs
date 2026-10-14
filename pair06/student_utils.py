import random
import statistics as stat
def generate_grades(count):
    grades = []
    for i in range(int(count)):
        grades.append(random.randint(1,12))
    return grades

def average_grades(grades):
    return stat.mean(grades)

def get_level(average):
    if average>=10:
        return 'Високий'
    elif average>=7 and average<=9.99:
        return 'Достатній'
    elif average>=4 and average<=6.99:
        return 'Середній'
    else:
        return 'Початковий'


