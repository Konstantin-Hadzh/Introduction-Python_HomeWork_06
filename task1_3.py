

from timeit import timeit


# код №1
def my_func1(x, y):
    return x ** y

print(my_func1(int(input('аргумент x: ')), int(input('аргумент y: '))))



# код №2
def my_func2(x, y):
    return pow(x, y)

print(my_func2(int(input('аргумент x: ')), int(input('аргумент y: '))))



print("время 1: ",(timeit("my_func1", globals=globals(), number=1000)))
print("время 2: ",(timeit("my_func2", globals=globals(), number=1000)))

"""
аргумент x: 3
аргумент y: 3
27
аргумент x: 3
аргумент y: 3
27
время 1:  3.7298003007890657e-05
время 2:  4.3502997868927196e-05
"""

""" Оператор возведения в степень, лежащий в основе my_func1 немного 
быстрее встроенной функции pow 
"""