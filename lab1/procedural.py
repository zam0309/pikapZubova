import sys
import math


def get_coef(index, prompt):
    if index < len(sys.argv):
        try:
            return float(sys.argv[index])
        except ValueError:
            print('Некорректное значение в командной строке:', sys.argv[index])

    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Нужно ввести число.')


def get_roots(a, b, c):
    d = b*b-4*a*c
    roots = []
    if d < 0:
        return d, roots

    if d == 0:
        for_t = [-b / (2 * a)]
    else:
        for_t = [(-b + math.sqrt(d)) / (2 * a),(-b - math.sqrt(d)) / (2 * a)]

    for t in for_t:
        if t > 0:
            roots.append(math.sqrt(t))
            roots.append(-math.sqrt(t))
        elif t == 0:
            roots.append(0.0)
    return d, roots


def main():
    a = get_coef(1, 'Введите коэффициент A: ')
    b = get_coef(2, 'Введите коэффициент B: ')
    c = get_coef(3, 'Введите коэффициент C: ')

    if a == 0:
        print('A = 0, уравнение не биквадратное')
        return

    d, roots = get_roots(a, b, c)
    print('Дискриминант D =', d)
    if len(roots) == 0:
        print('Действительных корней нет')
    else:
        print('Корни:', ', '.join(str(x) for x in roots))

main()

