while 1:
    i = input(">>>")#Запрос ввода
    i = i.split(" ")#Делим по пробелам
    a = 0
    while a < len(i):
        try:
            i[a] = int(i[a])#строки в числа
        except ValueError:
            print("Value Error")#при ошибке пишем ошибку и останавливаем цикл
            break
        a = a + 1
    z = 0#Переменная с результатом
    for c in i:
        z = z + c#Считаем все
    print(z)#Выводим результат