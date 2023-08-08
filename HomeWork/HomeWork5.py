# Задача 1 3 вопроса
print("Как вас зовут?")
name = input()
print("Кем вы работаете?")
work = input()
print("Сколько вам лет?")
age = input()
print("------------Информация о вас------------")
print(("Имя:"), (name))
print(("Профессия:"), (work))
print(("Возраст:"), (age))

# Задача 2 Деление двух сумм
print("Введите 4 числа")
x = int(input())
y = int(input())
z = int(input())
r = int(input())

firstSumm = x + y
secondSumm = z + r
print(firstSumm / secondSumm)

# Задача 3 Максимальное среди трех чисел
print("Введите 3 числа")
x = int(input())
y = int(input())
z = int(input())

if x > y and x > z:
    print(x)
elif y > x and y > z:
    print(y)
elif z > x and z > y:
    print(z)

# Задача 4 Среднее число
print("Введите 3 числа")
x = int(input())
y = int(input())
z = int(input())

if y < x < z:
    print(x)
elif x < y < z:
    print(y)
elif x < z < y:
    print(z)

# Задача 5 Следующее предыдущее число
print("Введите число")
x = int(input())
print(("Следующее число для числа"), (x), ("это"), (x + 1))
print(("Предыдущее число для числа"), (x), ("это"), (x - 1))

# Задача 6 Достаточно ли денег По условию, нужно купить:
# хлеб (стоит 30 рублей), молоко (стоит 50 рублей) и сыр (стоит 100 руб)
print("Сколько у Вас денег?")
x = int(input())
if x == 180:
    print("Спасибо, что без сдачи")
elif x < 180:
    print("Недостаточно денег")
elif x > 180:
    change = x - 180
    print(("Ваша сдача:"), (change))
