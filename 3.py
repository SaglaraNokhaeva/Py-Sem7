# 5. Напишите функцию triangle(a, b, c), которая принимает 
# на вход три длины отрезков и определяет, можно ли из этих отрезков составить треугольник.
# Входные данные
# Выходные данные
# triangle(1, 1, 2)
# Это не треугольник
# triangle(7, 6, 10)

def Triangle(a, b, c):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False
a = int(input('введите а: '))
b = int(input('введите b: '))
c = int(input('введите c: '))
print('Это треугольник' if Triangle(a, b, c) else "Это не треугольник")