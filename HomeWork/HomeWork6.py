# Задача со свездочкой
print("Введите рекомендуемое расстояния для бега")
recomend = int(input())
print("Введите нерекомендуемое расстояния для бега(не должно быть больше первого значения)")
notRecomend = int(input())
print("Введите какое расстояние вы бегаете сегодня")
distant = int(input())
if recomend <= distant < notRecomend:
    print("Это нормально")
elif distant >= notRecomend:
    print("Много бегать вредно")
elif distant < recomend:
    print("Слишком мало бегаете")
