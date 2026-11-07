#Тест списков,объявляю переменные
chore1=input("Дело 1: ")
chore2=input("Дело 2: ")
chore3=input("Дело 3: ")
print(" ")

#Создаю список
todo_list=[chore1+":×",chore2+":×",chore3+":×"]
print(todo_list)

#Спрашиваем пользователя какое дело он сделал

for i in range(3):
    choise=int(input("Какое дело вы сделали? (Введите цифру 1,2,3): "))
    if choise == 1:
        todo_list[0] = chore1+"✓"
    elif choise == 2:
        todo_list[1] = chore2+"✓"
    elif choise == 3:
        todo_list[2] = chore3+"✓"
    else:
        print("Такого дела нет")
    print("Обновленный список: ", todo_list)