#Найдите сумму цифр трехзначного числа.
#*Пример:*
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) |
namber = input('Введите трёх значное число: ')
rsult= 0
if len(namber) == 3:
    for i in namber:
        rsult += int(i)
    print(rsult)
else:
    print('Вы ввели не трёх значное число')

