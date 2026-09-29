x, y =map(int, input("Введіть через пробіл координати: ").split())
print(x, y)
if x > 0 and y > 0:
    print("1 чверть")
elif x > 0 and y < 0:
    print("4 чверть")
elif x < 0 and y > 0:
    print("2 чверть")
elif x < 0 and y < 0:
    print("3 чверть")