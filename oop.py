import sys
import math


class BiquadraticEquation:

    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        self.d = 0.0
        self.roots = []

    def get_coef(self, index, prompt):
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

    def read_coefs(self):
        self.a = self.get_coef(1, 'Введите коэффициент A: ')
        self.b = self.get_coef(2, 'Введите коэффициент B: ')
        self.c = self.get_coef(3, 'Введите коэффициент C: ')

    def calc_roots(self):
        a, b, c = self.a, self.b, self.c
        self.d = b * b - 4 * a * c
        self.roots = []
        if self.d < 0:
            return

        if self.d == 0:
            for_t = [-b / (2 * a)]
        else:
            for_t = [(-b + math.sqrt(self.d)) / (2 * a), (-b - math.sqrt(self.d)) / (2 * a)]

        for t in for_t:
            if t > 0:
                self.roots.append(math.sqrt(t))
                self.roots.append(-math.sqrt(t))
            elif t == 0:
                self.roots.append(0.0)

    def print_roots(self):
        print('Дискриминант D =', self.d)
        if len(self.roots) == 0:
            print('Действительных корней нет')
        else:
            print('Корни:', ', '.join(str(x) for x in self.roots))


def main():
    eq = BiquadraticEquation()
    eq.read_coefs()
    if eq.a == 0:
        print('A = 0, уравнение не биквадратное')
        return
    eq.calc_roots()
    eq.print_roots()

main()


