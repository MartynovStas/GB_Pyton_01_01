#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать
#один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

#*Пример:*
#3 2 4 -> yes
#3 2 1 -> no
a,b,c = int(input('В-те 1-ю сторону: ')),int(input('В-те 2-ю сторону: ')),int(input('В-те кол-во долек: '))
if c < a*b and (c % a == 0 or c % b == 0):
    print('Yes')
else:
    print('NO')