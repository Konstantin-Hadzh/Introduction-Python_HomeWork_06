

""" 
6) Реализовать функцию int_func(), принимающую слово из маленьких латинских 
букв и возвращающую его же, но с прописной первой буквой. Например, 
print(int_func(‘text’)) -> Text. 
Продолжить работу над заданием. 
В программу должна попадать строка из слов, разделенных пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод 
исходной строки, но каждое слово должно начинаться с заглавной буквы. 
Необходимо использовать написанную ранее функцию int_func()
"""


from memory_profiler import profile



# код№1

@profile
def without_func(line):
    return ' '.join(s[:1].upper() + s[1:] for s in line.split(' '))

line = input("Введите слова через пробел: ")
print(without_func(line))



# код №2

@profile
def ttl_func(text):
    return text.title() 

output_text = []

for line in input('Введите слова через пробел: ').split(' '):
    output_text.append(ttl_func(line)) 
    break
print(f'{" ".join(output_text)}') 

"""
При одинаковых затратах памяти в коде №1 обнаружено 9 событий в сравнении 
с 1 событием в коде №2. Что, вероятно, указывает на то, что код №2 быстрее 
выполняет задачу
"""

"""
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

