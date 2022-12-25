

""" 
1) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени, 
оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали 
и чего удалось добиться 
"""



from timeit import timeit


# код№1

def without_func(line):
    # без встроенной функции
    return ' '.join(s[:1].upper() + s[1:] for s in line.split(' '))


line = input("Введите слова через пробел: ")
print(without_func(line))


# код №2

def ttl_func(text):
    # на основе встроенной функции
    return text.title() # функция title() возвращает строку с заглавной первой буквой каждого слова в верхний регистр

output_text = []

for line in input('Введите слова через пробел: ').split(' '):
    output_text.append(ttl_func(line)) # append добавляет элемент в конец списка

print(f'{" ".join(output_text)}') # функция join может использоваться с любым итерируемым объектом, но результатом всегда будет строка


print(timeit("without_func(line)", globals=globals()))
print(timeit("ttl_func", globals=globals()))

"""
Введите слова через пробел: гнев богиня воспой
Гнев Богиня Воспой
Введите слова через пробел: гнев богиня воспой                          
Гнев Богиня Воспой
1.1600734120002016
0.0322196150000309
"""

"""
использование встроенной функции title() в коде №2 сокращает время 
в 100 с лишним раз. При измерении затрат памяти обоих скриптов выяснилось, 
что в коде №1 с (математическим решением) обнаружино  событий (Occurrences), 
что на 8 больше, чем у кодв №2. Возможно с этим и связана разница во времени.
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    21     17.5 MiB     17.5 MiB           1   @profile
    22                                         def without_func(line):
    23     17.5 MiB      0.0 MiB           9       return ' '.join(s[:1].upper() + s[1:] 
    for s in line.split(' '))

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     17.5 MiB     17.5 MiB           1   @profile
    33                                         def ttl_func(text):
    34     17.5 MiB      0.0 MiB           1       return text.title() 
"""