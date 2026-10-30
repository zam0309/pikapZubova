import sys
import math


def to_float(s):
    try:
        return float(s)
    except ValueError:
        return None


def read_coef(prompt):
    match to_float(input(prompt)):
        case None:
            print('Нужно ввести число.')
            return read_coef(prompt)
        case value:
            return value

def get_coef(index, prompt):
    if index >= len(sys.argv):
        return read_coef(prompt)

    arg = sys.argv[index]
    match to_float(arg):
        case None:
            print('Некорректное значение в командной строке:', arg)
            return read_coef(prompt)
        case value:
            return value

def t_roots(a, b, d):
    match d:
        case d if d < 0:
            return []
        case 0:
            return [-b / (2 * a)]
        case _:
            return [(-b+math.sqrt(d)) / (2*a), (-b-math.sqrt(d)) / (2*a)]


def x_roots(t):
    match t:
        case t if t > 0:
            return [math.sqrt(t), -math.sqrt(t)]
        case 0:
            return [0.0]
        case _:
            return []


def get_roots(a, b, c):
    d = b*b - 4*a*c
    roots = [x for t in t_roots(a, b, d) for x in x_roots(t)]
    return d, roots


def print_roots(d, roots):
    print('Дискриминант D =', d)
    match roots:
        case []:
            print('Действительных корней нет')
        case [x]:
            print('Один корень:', x)
        case _:
            print('Корни:', ', '.join(map(str, roots)))


def main():
    a = get_coef(1, 'Введите коэффициент A: ')
    b = get_coef(2, 'Введите коэффициент B: ')
    c = get_coef(3, 'Введите коэффициент C: ')
    match a:
        case 0:
            print('A = 0, уравнение не биквадратное')
        case _:
            d, roots = get_roots(a, b, c)
            print_roots(d, roots)

main()
