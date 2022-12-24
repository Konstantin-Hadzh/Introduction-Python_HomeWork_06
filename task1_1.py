

""" 2) Пользователь вводит время в секундах. Переведите время в часы, 
минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование 
строк """

from timeit import timeit

import datetime

# код №1
user_interval_sec1 = int(input('Введите значение интервала в секундах: '))
clock = user_interval_sec1 // 3600
min = (user_interval_sec1 % 3600) // 60
sec = user_interval_sec1 % 3600 % 60
print(f'{clock}:{min}:{sec}')

# код №2
user_interval_sec2 = int(input("Введите значение интервала в секундах: ")) 
time_format = str(datetime.timedelta(seconds = user_interval_sec2)) 
print(time_format)

print(timeit("user_interval_sec1", globals=globals(), number=1000000000))
print(timeit("user_interval_sec2", globals=globals(), number=1000000000))

"""
Введите значение интервала в секундах: 987
0:16:27
Введите значение интервала в секундах: 987
0:16:27
24.096624088000112
23.44809645400005
"""


"""
Использование класса timedelta() модуля datetime в коде №2 для решения 
задачи немного (в 1,02 раза приблизительно) эффективнее по врнмени чисто математического решения 
варианта №1.
"""