#Задание 2 (Арифметические операции)

# a = int(input('чётное'))
# print(a*2)

#2
# a = int(input('не чётное'))
# print(a*3)

#3
# a = int(input('1 чел'))
# b = int(input('2 чел'))
# print(b-a-1)

#4
# a = int(input())
# b = int(input())
# for i in range(a|1, b+1, 2):
#     print(i, end=' ')

#5
# n = int(input('школьники '))
# k = int(input('тыблоки '))
# print('взяли', k // n)
# print('осталось', k % n)

#6
# a = int(input('дюймы '))
# fut = a / 12
# ird = fut / 3
# mil = ird / 1760
# print(f'{mil}  мили, {ird}  ярды, {fut}  футы, {a}  дюймы')

#7
# a = int(input('копеек '))
# pol = a * 0.25
# alt = a / 3
# gr = a / 10
# rub = a / 100
# print(f'{rub} рублей, {gr} гривен, {alt} алтынов, {pol} полушек')

#8
# import math
# a = int(input('квартира '))
# print(math.ceil(a/4))

#9
# a = int(input('бочки '))
# a1 = a * 40
# a2 = a1 * 10
# a3 = a2 * 10
# a4 = a3 * 2 
# print(f'{a1} вёдер, {a2} штофов, {a3} чарок, {a4} шкаликов')

#10
# a = int(input('вершков '))
# a2 = a / 4
# a3 = a / 16
# a4 = a / 48 
# print(f'{a4} саженей, {a3} аршин, {a2} пядей, {a} вершков')

#11
# x = int(input('x'))
# y = int(input('y'))
# n = int(input('n'))
# print(n + (n-1) * y)

#12
# x = int(input("Введите расстояние до ближайшего фонарного столба (м): "))
# y = int(input("Введите расстояние между фонарными столбами (м): "))
# z = int(input("Введите длину вашего шага (м): "))
# n = int(input("Введите количество шагов: "))
# print((x + n * z) // y)

#13
# L = int(input("Введите длину бревна (м): "))
# x = int(input("Введите длину одного куска (м): "))
# print(L // x)

#14
# L = int(input("Введите длину бревна (м): "))
# n = int(input("Введите количество распилов (мест): "))
# print(L / (n+1))


#15
# import math
# d = int(input("Введите диаметр резинового кольца (м): "))
# n = int(input("Введите количество распилов (мест): "))
# print(math.pi * d / (n-1))



#Задание 3 (Строки)

# text = "Мы обязательно научимся программировать!"

# # 1. Выводим третий символ этой строки
# text1 = text[2]
# print(f"Третий символ: {text1}")

# # 2. Выводим предпоследний символ этой строки
# text2 = text[-2]
# print(f"Предпоследний символ: {text2}")

# # 3. Выводим первые пять символов этой строки
# text3 = text[:5]
# print(f"Первые пять символов: {text3}")

# # 4. Выводим всю строку, кроме последних двух символов
# text4 = text[:-2]
# print(f"Вся строка, кроме последних двух символов: {text4}")

# # 5. Выводим все символы с чётными индексами
# text5 = text[::2]
# print(f"Символы с чётными индексами: {text5}")

# # 6. Выводим все символы с нечётными индексами
# text6 = text[1::2]
# print(f"Символы с нечётными индексами: {text6}")

# # 7. Выводим четыре символа из центра строки
# text7 = len(text) // 2
# print(f"Четыре символа из центра строки: {text[text7 - 2:text7 + 2]}")

# # 8. Выводим символы с индексами, кратными трём
# text8 = text[::3]
# print(f"Символы с индексами, кратными трём: {text8}")

# # 9. Выводим все символы в обратном порядке
# text9 = text[::-1]
# print(f"Все символы в обратном порядке: {text9}")

# # 10. Выводим все символы строки через один в обратном порядке, начиная с последнего
# text10 = text[::-1][::2]
# print(f"Все символы через один в обратном порядке: {text10}")

# # 11. Удаляем второе слово из строки
# words = text.split()
# words.pop(1)
# text11 = ' '.join(words)
# print(f"Строка без второго слова: {text11}")

# # 12. Заменяем второе слово на строку «никогда не»
# words[1] = "никогда не"  
# text12 = ' '.join(words)
# print(f"Строка с заменой второго слова: {text12}")

# # 13. Добавляем в конец строки «на Python»
# text13 = text + " на Python"
# print(f"Строка с добавлением в конец: {text13}")

# # 14. Ставим последнее слово первым в строке
# text14 = ' '.join([words[-1]] + words[:-1])
# print(f"Строка с последним словом первым: {text14}")

# # 15. Выводим длину данной строки
# text15 = len(text)
# print(f"Длина данной строки: {text15}")


# Задание 5 (Условный оператор)

# 4. Запросите у пользователя два числа

# num1 = float(input("Введите первое число: "))
# num2 = float(input("Введите второе число: "))

# if num1 > num2:
#     res = num1 - num2
#     print(f"Первое число больше второго. Разница: {res}")
# elif num2 > num1:
#     res1 = num1 + num2
#     print(f"Второе число больше первого. Сумма: {res1}")
# else:
#     print(f"Оба числа равны: {num1}")



# 5. Запросите у пользователя два целых числа 𝑚 и 𝑛.
# m = int(input("Введите целое число m: "))
# n = int(input("Введите целое число n: "))

# if n != 0:  
#     if m % n == 0:
#         res = m // n
#         print(f"{m} делится на {n} нацело. Частное: {res}")
#     else:
#         print(f"{m} на {n} нацело не делится.")
# else:
#     print("Ошибка: Деление на ноль невозможно.")



# 6. Напишите программу для решения квадратного уравнения 𝑎𝑥2 + 𝑏𝑥 + 𝑐 = 0
# import math

# a = float(input("Введите коэффициент a: "))
# b = float(input("Введите коэффициент b: "))
# c = float(input("Введите коэффициент c: "))

# D = b**2 - 4*a*c

# if D < 0:
#     print("Корней нет.")
# elif D == 0:
#     x1 = -b / (2 * a)
#     print(f"Уравнение имеет один корень: x1 = {x1}")
# else:
#     x1 = (-b + math.sqrt(D)) / (2 * a)
#     x2 = (-b - math.sqrt(D)) / (2 * a)
#     print(f"Уравнение имеет два корня: x1 = {x1}, x2 = {x2}")




# 7. Напишите программу, решающую кубическое уравнение вида 𝑦3+𝑝𝑦+𝑞 = 0
# import cmath


# p = float(input("Введите коэффициент p: "))
# q = float(input("Введите коэффициент q: "))


# D = (q / 2) ** 2 + (p / 3) ** 3

# if D > 0:
    
#     u1 = (-q / 2 + D ** 0.5) ** (1/3)
#     u2 = (-q / 2 - D ** 0.5) ** (1/3)
#     y1 = u1 + u2
#     print(f"Уравнение имеет один действительный корень: y1 = {y1}")
# elif D == 0:
#  
#     y1 = - (3 * p) / (3 * (1 if p != 0 else 1e-10))
#     print(f"Уравнение имеет один тройной корень: y1 = {y1}")
# else:
#     r = (-q / 2) ** (1/3)
#     theta = cmath.phase(complex(-D ** 0.5, 0)) / 3
#     y1 = r * cmath.exp(complex(0, theta))
#     y2 = r * cmath.exp(complex(0, theta + (2 * cmath.pi / 3)))
#     y3 = r * cmath.exp(complex(0, theta - (2 * cmath.pi / 3)))
    
#     print(f"Уравнение имеет три корня:")
#     print(f"y1 = {y1}")
#     print(f"y2 = {y2}")
#     print(f"y3 = {y3}")



# 8. Напишите программу, которая запрашивает у пользователя его возраст

# age = int(input("Введите ваш возраст (целое число лет): "))


# if age < 0 or age > 120:
#     for _ in range(5):
#         print("Ошибка! Это программа для людей!")
# elif 0 <= age < 7:
#     print("Вам в детский сад")
# elif 7 <= age < 18:
#     print("Вам в школу")
# elif 18 <= age < 25:
#     print("Вам в профессиональное учебное заведение")
# elif 25 <= age < 60:
#     print("Вам на работу")
# elif 60 <= age <= 120:
#     print("Вам предоставляется выбор")


# 9. Напишите программу, которая поможет вам оптимизировать путешествие на автомобиле.
# s = float(input("Сколько километров вы хотите проехать на автомобиле? "))
# v = float(input("Сколько литров топлива расходует автомобиль на 100 километров? "))
# t = float(input("Сколько литров топлива в вашем баке? "))

# res = (s / 100) * v

# if t >= res:
#     print(f"Достаточно топлива для поездки. Вам потребуется {res} литров.")
#     print("Вы сможете проехать желаемое расстояние.")
# else:
#     print(f"Недостаточно топлива для поездки. Вам не хватает {res - t} литров.")
#     print("Вы не сможете проехать желаемое расстояние.")\


# 10. Пользователь вводит три действительных числа
# a = float(input("Введите длину стороны a: "))
# b = float(input("Введите длину стороны b: "))
# c = float(input("Введите длину стороны c: "))

# if a + b <= c or a + c <= b or b + c <= a:
#     print("Такого треугольника не существует.")
# else:
#     print("Такой треугольник существует.")
#     if a == b == c:
#         print("Треугольник равносторонний.")
#     elif a == b or b == c or a == c:
#         print("Треугольник равнобедренный.")
#     else:
#         print("Треугольник разносторонний.")
#     if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
#         print("Треугольник прямоугольный.")



# 11. Известен вес боксёра-любителя
# ves = int(input("Введите вес боксёра (кг): "))
# if ves < 60:
#     print("Легкий вес")
# elif 60 <= ves < 64:
#     print("Первый полусредний вес") 
# elif 64 <= ves < 69:
#     print("Полусредний вес") 
# else:
#     print("Вес за пределами категорий") 



# 12. В чемпионате по футболу
# point = int(input("Введите количество очков, полученных командой: "))
# if point == 3:
#     print("Выигрыш") 
# elif point == 1:
#     print("Ничья") 
# elif point == 0:
#     print("Проигрыш") 
# else:
#     print("Некорректное количество очков") 


# 13. Составить программу, которая в зависимости от порядкового номера дня недели (от 1 до 7) 
# day = int(input("Введите порядковый номер дня недели (от 1 до 7): "))
# if day == 1:
#     print("Понедельник")
# elif day == 2:
#     print("Вторник")
# elif day == 3:
#     print("Среда")
# elif day == 4:
#     print("Четверг")
# elif day == 5:
#     print("Пятница")
# elif day == 6:
#     print("Суббота")
# elif day == 7:
#     print("Воскресенье")


# 14. Составить программу, которая в зависимости от порядкового номера месяца (1, 2, ..., 12)
# day = int(input("Введите порядковый номер дня недели (от 1 до 7): "))
# if day == 1:
#     print("Январь")
# elif day == 2:
#     print("Февраль")
# elif day == 3:
#     print("Март")
# elif day == 4:
#     print("Апрель")
# elif day == 5:
#     print("Май")
# elif day == 6:
#     print("Июнь")
# elif day == 7:
#     print("Июль")
# elif day == 8:
#     print("Август")
# elif day == 9:
#     print("Сентябрь")
# elif day == 10:
#     print("Октябрь")
# elif day == 11:
#     print("Ноябрь")
# elif day == 12:
#     print("Декабрь")


# 15. Составить программу, которая в зависимости от порядкового номера месяца (1, 2, ..., 12) 
# num = int(input("Введите порядковый номер месяца (от 1 до 12): "))
# if num == 1 or num == 2 or num == 12:
#     print("Зима") 
# elif num >= 3 and num <= 5:
#     print("Весна") 
# elif num >= 6 and num <= 8:
#     print("Лето") 
# elif num >= 9 and num <= 11:
#     print("Осень") 





# Задание 6 (Списки. Кортежи. Словари)
#1Списки

# listok1 = list(range(0, 101, 10))
# listok2 = list(range(0, 101, 10))
# listok2[-1] = 200
# e = listok1[:5] + listok2[5:]
# f = listok1[:5] + listok2[5:]
# f.append(210)
# f.append(220)
# print(listok1)
# print("Задание a: ", listok1[1])
# print("Задание a: ", listok2[4])
# print("Задание b: ", listok1[1])
# print("Задание c: ", listok2)
# print("Задание d: ", listok1 + listok2)
# print("Задание e: ", e)
# print("Задание f: ", f)
# print("Задание g: ", max(f), min(f))



# 2. Кортежи
# coll = 10
# num = tuple(range(1, coll + 1))
# suname = ("Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов", "Попов", "Лебедев", "Ковалев", "Николаев", "Михайлов")
# print("Фамилия студента с номером 5:", suname[4])  
# print("Элемент во втором кортеже под номером 5:", suname[4])  
# sum_name = list(zip(num, suname))
# print("Объединенный кортеж:", list(zip(num, suname)))
# print("Срез из соединенного кортежа:", sum_name[2:6])


#3. Словари
# School = {
#     "1а": 25,
#     "1б": 30,
#     "2в": 28,
#     "3а": 22,
#     "4б": 35
# }

# print(School)
# #b
# class_name = input("класс какой: ")
# if class_name in School:
#     print(f"в {class_name} учатся {School[class_name]}")
# else:
#     print("Такого класса не существует.")

# #c
# School["1а"] = 27
# School["2в"] = 31
# School["3а"] = 25

# print('обновили', School)

# #d
# School["5а"] = 20
# School["6б"] = 32
# print(School)

# e
# del School["4б"]
# print(School)


# 3.6 Задания на циклы
# Задание 7 (Задания на рекуррентные сотношения)
# n = 5
# # a) 1, 2, 3, 4, ...
# a = [1 + i for i in range(n)]

# # b) 0, 5, 10, 15, ...
# b = [5 * i for i in range(n)]

# # c) 1, 1, 1, 1, ...
# c = [1] * n

# # d) 1, -1, 1, -1, ...
# d = [1 if i % 2 == 0 else -1 for i in range(n)]

# # e) 1, -2, 3, -4, ...
# e = [(-1)**i * (i + 1) for i in range(n)]

# # f) 2, 4, 8, 16, ...
# f = [2**i for i in range(n)]

# # g) 2, 4, 16, 256, ...
# g = [2**(2**i) for i in range(n)]

# # h) 0, 1, 2, 3, 0, ...
# h = [i % 4 for i in range(n)]

# # i) 1!, 3!, 5!, 7!, ...
# import math
# i = [math.factorial(2 * j + 1) for j in range(n)]

# print(a, b, c, d, e, f, g, h, i)



# Задание 8 (Задания на цикл с условием)
# 1. Напишите программу, которая будет суммировать вводимые с клавиатуры числа до тех пор, пока они положительны.

# total = 0
# while True:
#     number = int(input("Введите числa: "))
#     if number < 0:
#         break
#     total += number
# print("Сумма положительных чисел:", total)

# 2. Напишите программу, которая будет суммировать вводимые с клавиатуры числа до тех пор, пока они отрицательны.
# total = 0
# while True:
#     number = int(input("Введите отрицательное числ: "))
#     if number >= 0:
#         break
#     total += number
# print("Сумма отрицательных чисел:", total)

# 3. Напишите программу, которая будет суммировать вводимые с клавиатуры

# total = 0
# while True:
#     number = float(input("Введите число: "))
#     if number == 0:
#         break
#     total += number
# print("Сумма введённых чисел:", total)

# 4. Напишите программу, которая будет суммировать вводимые с клавиатуры
# total = 0
# while True:
#     number = int(input("Введите чётное число: "))
#     if number % 2 != 0:
#         break
#     total += number
# print("Сумма чётных чисел:", total)

# 5. Дано число 𝑛. Напечатать те натуральные числа, квадрат которых не превышает 𝑛.

# n = int(input("Введите натуральное число n: "))
# i = 1
# while i * i <= n:
#     print(i)
#     i += 1

# 6. Дано число 𝑛. Найти первое натуральное число, квадрат которого больше 𝑛.

# n = int(input("Введите натуральное число n: "))
# i = 1
# while i * i <= n:
#     i += 1
# print(i)


# 7. Дано число 𝑛. Среди чисел
# n = float(input("Введите число n: "))
# s = 0  
# i = 1  
# while True:
#     s += 1 / i  
#     if s > n: 
#         print("Первое число, большее n:", s)
#         break   
#     i += 1 


# 8. Дано число 𝑎 (1 < 𝑎 < 1.5).
# a = float(input("Введите число a (1 <= a <= 1.5): "))
# s = 1  
# i = 2  

# while True:
#     s += 1 / i  
#     if s < a:  
#         print("Первое число, меньшее a:", s)
#         break   
#     i += 1      


# # 9. Напишите программу, которая запрашивает у пользователя
# sump = [-9999,]#кастыл
# i = 0
# while True:
#     a = int(input('число больше предыдущего'))
#     sump.append(a)
#     if sump[i] < sump[i+1]:
#         i += 1
#     else:
#         break
# print(sum(sump[1:-1]))


# 10. Напишите программу, которая запрашивает у пользователя
# sump = [99999,]#кастыл
# i = 0
# while True:
#     a = int(input('число больше menshe'))
#     sump.append(a)
#     if sump[i] > sump[i+1]:
#         i += 1
#     else:
#         break
# print(len(sump[1:-1]))

# 11. Напишите программу, которая запрашив
# sump = []
# while True:
#     try:
#         a = int(input())
#         sump.append(a)
#     except:
#         print(len(sump))
#         break


# 12
# count = 0

# while True:
#     number = float(input("Введите число: "))
    
#     if number < 10:
#         count += 1 
#     else:
#         break  
# print("Количество введённых чисел:", count)


#13
# number = input("Введите натуральное число с различными цифрами: ")
# max_digit = number[0]  
# index_from_start = 1  
# index_from_end = len(number)  

# for i in range(len(number)):
#     if number[i] > max_digit:  
#         max_digit = number[i]
#         index_from_start = i + 1  
#         index_from_end = len(number) - i  

# print(f"Порядковый номер максимальной цифры {max_digit}:")
# print(f"От начала: {index_from_start}")
# print(f"От конца: {index_from_end}")


# 14
# number = input("Введите натуральное число с различными цифрами: ")
# min_digit = number[0] 
# index_from_start = 1    
# index_from_end = len(number)  

# for i in range(len(number)):
#     if number[i] < min_digit:  
#         min_digit = number[i]
#         index_from_start = i + 1  
#         index_from_end = len(number) - i  

# print(f"Порядковый номер минимальной цифры {min_digit}:")
# print(f"От начала: {index_from_start}")
# print(f"От конца: {index_from_end}")


# 15
# number = input("Введите натуральное число: ")
# max_digit = max(number)
# count_max_digit = number.count(max_digit)
# print(f"Максимальная цифра {max_digit} встречается {count_max_digit} раз(а) в числе {number}.")


# Задание 9 (Задания на цикл со счётчиком)

# 1
# num = 0
# for i in range(1, 91):
#     if i % 2 == 0: 
#         num += i  
# print(f"Сумма всех четных чисел от 1 до 90 включительно: {num}")


#2
# a = int(input("Введите значение a: "))
# b = int(input("Введите значение b: "))
# count = 0
# for i in range(a, b + 1):
#     if i % 2 == 0:  
#         count += i  
# print(f"Сумма всех четных чисел от {a} до {b} включительно: {count}")

#3
# count = 0
# for i in range(1, 91):
#     if i % 2 != 0: 
#         count += i  
# print(f"Сумма всех нечётных чисел от 1 до 90 включительно: {count}")

#4

# a = int(input("Введите значение a: "))
# b = int(input("Введите значение b: "))

# count = 0

# for i in range(a, b + 1):
#     if i % 2 != 0: 
#         count += i  
# print(f"Сумма всех нечётных чисел от {a} до {b} включительно: {count}")

# 5
# for i in range(1, 10):
#     print(f"{i} x 5 = {i*5}")


# 6
# for i in range(1, 10):
#     print(f"{i} x 9 = {i*9}")

# 7
# n = int(input('Число от 1 до 9: '))
# for i in range(1, 10):
#     print(f"{i} x 9 = {i*9}")


# 8
# price= int(input("Введите стоимость 1 кг сыра (в рублях): "))
# for i in range(50, 1001, 50):
#     res = (i / 1000) * price
#     print(f"{i} грам - {res} рублей")


# 9
# price= int(input("Введите стоимость 1 кг сыра (в рублях): "))
# for i in range(100, 2001, 100):
#     res = (i / 1000) * price
#     print(f"{i} грам - {res} рублей")


# 10
# count = 0
# for i in range(10, 101):
#     count += i  
# print(f"Сумма всех целых чисел от 10 до 100: {count}")


# 11
# a = 10
# l = 100
# n = l - a + 1
# numbers = n * (a + l) // 2
# print(f"Сумма всех целых чисел от {a} до {l}: {numbers}")


# 12
# b = int(input("Введите значение b: "))

# count = 0

# for i in range(10, b + 1):
#     count += i 

# print(f"Сумма всех целых чисел от 10 до {b}: {count}")


# 13
# a = int(input("Введите значение a: "))
# b = int(input("Введите значение b: "))

# count = 0

# for i in range(a, b + 1):
#     count += i

# print(f"Сумма всех целых чисел от {a} до {b}: {count}")


# 14
# count = 1

# for i in range(10, 101):
#     count *= i  

# print(f"Произведение всех целых чисел от 10 до 100: {count}")


# 15
# a = int(input("Введите значение a: "))
# b = int(input("Введите значение b: "))

# count = 1

# for i in range(a, b + 1):
#     count *= i  

# print(f"Произведение всех целых чисел от {a} до {b}: {count}")




# Глава 4
# Массивы. Модуль numpy

# Задание 11
#1
# import numpy as np

# array_10 = np.zeros(10)
# array_55 = np.zeros(55)

# matrix_3x4 = np.zeros((3, 4))

# array_3d = np.zeros((2, 4, 5))

# np.savetxt('array_10.txt', array_10)
# np.savetxt('array_55.txt', array_55)
# np.savetxt('matrix_3x4.txt', matrix_3x4)
# np.savetxt('array_3d.txt', array_3d.reshape(-1, 5)) 
# print(array_10)


#6
# import numpy as np
# import math

# e = math.e

# step = e / 50
# array_range = np.arange(-e, e + step, step)

# print("Созданный массив:")
# print(array_range)
# np.savetxt('array_range.txt', array_range)


#11
# import numpy as np
# array = np.array([[i] * 5 for i in range(1, 6)])
# np.savetxt('array11.txt', array)
# print(array)


# Задание 12 Задания выполняйте все по порядку.
# import numpy as np


# matrix = np.loadtxt('array_range.txt')

# if matrix.ndim == 1:
#     matrix = matrix.reshape(-1, 1)  

# print("Загруженная матрица:")
# print(matrix)


# vector = np.arange(0, matrix.shape[0])  

# result_matrix = matrix + vector[:, np.newaxis]  

# print("Результирующая матрица после прибавления вектора:")
# print(result_matrix)

# max_element = np.max(result_matrix)
# min_element = np.min(result_matrix)

# print(f"Максимальный элемент: {max_element}")
# print(f"Минимальный элемент: {min_element}")

# row_sums = np.sum(result_matrix, axis=1)
# print("Сумма элементов по каждой строке:")
# print(row_sums)

# np.savetxt('result_matrix.txt', result_matrix)
# np.savetxt('vector.txt', vector)

# print("Результаты успешно сохранены в файлы 'result_matrix.txt' и 'vector.txt'.")


# Глава 5
# Графики. Модуль matplotlib


# Задание 14 - 15
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(-2, 2, 100)
# y = x**2
# plt.plot(x, y, color='red', linewidth=20)
# plt.plot(x, y)
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.grid(True)
# plt.show()

# Задание 16-17

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-1, 1, 100)


fig, axs = plt.subplots(6, 1, figsize=(6, 12))  # 6 строк и 1 столбец


for degree in range(1, 7):  # Степени от 1 до 6
    y = x ** degree  # Вычисляем y для текущей степени
    axs[degree - 1].plot(x, y)  # Добавляем линию на соответствующий подграфик
    axs[degree - 1].set_title(f'$f(x) = x^{degree}$')  # Заголовок для каждого подграфика
    axs[degree - 1].grid(True)  # Включаем сетку
    axs[degree - 1].set_xlim(-1, 1)  # Ограничиваем ось x
    axs[degree - 1].set_ylim(-1, 1)  # Ограничиваем ось y
    axs[degree - 1].set_xlabel("x")  # Подпись оси x
    axs[degree - 1].set_ylabel("f(x)")  # Подпись оси y


plt.suptitle("Степенные одночлены от $x^1$ до $x^6$", fontsize=16)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Уплотняем графики и оставляем место для общего заголовка
plt.show()




# Задание 18

# import matplotlib.pyplot as plt

# labels = ['Студенты с пятёрками', 'Студенты с другими оценками']
# sizes = [15, 5]  
# colors = ['#ff9999', '#66b3ff']  
# explode = (0.1, 0)  


# plt.figure(figsize=(8, 6))
# plt.pie(sizes, explode=explode, labels=labels, colors=colors,
#         autopct='%1.1f%%', shadow=True, startangle=140)

# plt.axis('equal')  
# plt.title('Доли студентов группы, сдавших сессию на одни пятёрки')
# plt.show()

# Задание 19
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# # Определяем диапазон значений для x и y
# x = np.linspace(-3, 3, 100)
# y = np.linspace(-3, 3, 100)

# # Создаем сетку значений
# X, Y = np.meshgrid(x, y)
# Z = X**3 + Y**3  # Вычисляем значения функции

# # Создание трёхмерного графика
# fig = plt.figure(figsize=(12, 6))

# # Подграфик для трёхмерного графика
# ax1 = fig.add_subplot(121, projection='3d')
# ax1.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
# ax1.set_title('Трёхмерный график $z = x^3 + y^3$')
# ax1.set_xlabel('X')
# ax1.set_ylabel('Y')
# ax1.set_zlabel('Z')

# # Подграфик для закрашенной контурной диаграммы
# ax2 = fig.add_subplot(122)
# contour = ax2.contourf(X, Y, Z, cmap='viridis')  # Закрашенная контурная диаграмма
# ax2.set_title('Контурная диаграмма $z = x^3 + y^3$')
# ax2.set_xlabel('X')
# ax2.set_ylabel('Y')
# plt.colorbar(contour)  # Добавляем цветовую шкалу

# # Отображение графиков
# plt.tight_layout()
# plt.show()



# Задание 20 Работа с текстовыми файлами.
import numpy as np

# with open('output.txt', 'w') as file:
#     file.write("Число\tКвадрат\tКуб\n")
#     for i in range(1, 101):
#         square = i ** 2
#         cube = i ** 3
#         file.write(f"{i}\t{square}\t{cube}\n")




# 2

# with open('trigonometric.txt', 'w') as file:
#     file.write("x\tsin(x)\tcos(x)\n")
#     step = np.pi / 24
#     x_values = np.arange(0, 2 * np.pi, step)

#     for x in x_values:
#         sin_value = np.sin(x)
#         cos_value = np.cos(x)
#         file.write(f"{x:.4f}\t{sin_value:.4f}\t{cos_value:.4f}\n")



# 3
# with open('Зачёт.txt', 'w', encoding='utf-8') as file:
#     num_students = int(input("Введите количество учеников в вашей группе: "))

#     for i in range(num_students):
#         full_name = input(f"Введите Фамилию Имя Отчество для ученика {i + 1}: ")
#         grade = input("Введите оценку: ")
#         file.write(f"{full_name}\t{grade}\n")

# print("Данные успешно записаны в файл 'Зачёт.txt'.")


# 4
# try:
#     with open('Зачёт.txt', 'r', encoding='utf-8') as file:
#         surname = input("Введите фамилию ученика: ")
#         found = False
        
#         for line in file:
#             full_name, grade = line.strip().split('\t')
#             if full_name.startswith(surname):
#                 print(f"Оценка для {full_name}: {grade}")
#                 found = True
#                 break
        
#         if not found:
#             print(f"Ученик с фамилией '{surname}' не найден.")
# except FileNotFoundError:
#     print("Файл 'Зачёт.txt' не найден.")