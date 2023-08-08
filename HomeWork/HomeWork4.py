# Задание 1 Сумма меньше, больше, равна
print("Введите последовательно два числа")
x = int(input())
y = int(input())
if x + y > 10:
    print("Сумма больше")
elif x + y < 10:
    print("Сумма меньше")
elif x + y == 10:
    print("Сумма равна")

# Задание 2 Четное-нечетное
print("Введите целое число")
x = int(input())
if x > 0:
    print(1)
elif x < 0:
    print(-1)
elif x == 0:
    print(0)

# Задание 3 Минимальное значение
print("Введите последовательно 2 числа")
x = int(input())
y = int(input())
if x < y:
    print(x)
elif y < x:
    print(y)
elif y == x:
    print("Числа совпадают")
