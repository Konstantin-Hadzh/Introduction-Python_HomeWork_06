

from memory_profiler import profile


# код №1
@profile
def my_func1(x, y):
    return x ** y

print(my_func1(int(input('аргумент x: ')), int(input('аргумент y: '))))



# код №2
@profile
def my_func2(x, y):
    return pow(x, y)


print(my_func2(int(input('аргумент x: ')), int(input('аргумент y: '))))

""" 
По затратам памяти нет принципиальной разницы между использованием оператора 
возведения в степень и встроенной функции возведения в степень pow 
"""

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     17.5 MiB     17.5 MiB           1   @profile
     8                                         def my_func1(x, y):
     9     17.5 MiB      0.0 MiB           1       return x ** y


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    16     17.5 MiB     17.5 MiB           1   @profile
    17                                         def my_func2(x, y):
    18     17.5 MiB      0.0 MiB           1       return pow(x, y)
"""