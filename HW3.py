def zadacha1():
    #Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
    #6 –> 1 1 2 3 5 8

    fibonachi = open('fibonachi.txt', mode = 'w' ,encoding='utf-8')
    n = int(input ('введите число элеметов последовательности Фибоначчи:'))
    a=0
    b=1
    for i in range (n):
        a,b = b,a+b
        fibonachi.writelines(str(a) + ' ')
    fibonachi.close()


def zadacha2():
    #Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
    #а –> абрикос, авокадо, апельсин, айва.

    fruits = open('fruits.txt', mode = 'r' ,encoding='utf-8')
    letter = input ('введите букву фрукта:').upper()
    text = fruits.readlines()
    for i in text:
        if i[0] == letter:
            print(i)


def zadacha3():
    #Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум,
    #отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.
    dictionary = \
        {'Привет':'Здравствуйте!',
        'Как тебя зовут?':'Меня зовут Настя',
        'Как дела?':'Не жалуюсь, спасибо, что спросили!'}
    key = str(input('Вы :').upper())
    if key in dictionary:
        print (f'Бот :{dictionary[key]}') 
    else:
        print("Бот: Не знаю, что на это ответить")
      
        
#zadacha1()
#zadacha2()
#zadacha3()
