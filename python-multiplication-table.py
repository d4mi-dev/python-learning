import time
#Тест с библиотекой time и циклом for
print("Введите число:")
number = int(input())

for multi in range(1,11):
    result = number*multi
    print(number,"*",multi,"=",result)
    time.sleep(0.3)
#Таблица умножения от одного до любого числа (в моем случае до 10)