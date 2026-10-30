from operator import itemgetter


class Proc:
    def __init__(self, id, name, lines, db_id):
        self.id = id
        self.name = name
        self.lines = lines
        self.db_id = db_id


class Db:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class ProcDb:
    def __init__(self, db_id, proc_id):
        self.db_id = db_id
        self.proc_id = proc_id


dbs = [
    Db(1, 'Продажи'),
    Db(2, 'Склад'),
    Db(3, 'Персонал'),
    Db(11, 'Продажи (резервная)'),
    Db(22, 'Склад (резервная)'),
    Db(33, 'Персонал (резервная)'),
]

procs = [
    Proc(1, 'обновление_заказов', 120, 1),
    Proc(2, 'расчет_выручки', 85, 1),
    Proc(3, 'учет_остатков', 60, 2),
    Proc(4, 'начисление_окладов', 150, 3),
    Proc(5, 'выборка_сотрудников', 45, 3),
    Proc(6, 'перенос_данных', 70, 3),
]

procs_dbs = [
    ProcDb(1, 1),
    ProcDb(1, 2),
    ProcDb(2, 3),
    ProcDb(3, 4),
    ProcDb(3, 5),
    ProcDb(3, 6),
    ProcDb(11, 1),
    ProcDb(11, 6),
    ProcDb(22, 3),
    ProcDb(33, 4),
    ProcDb(33, 5),
]


def main():
    one_to_many = [(p.name, p.lines, d.name)
                   for d in dbs
                   for p in procs
                   if p.db_id == d.id]

    many_to_many = [(p.name, p.lines, d.name)
                    for d in dbs
                    for pd in procs_dbs
                    for p in procs
                    if d.id == pd.db_id and p.id == pd.proc_id]

    print('Задание Б1')
    res1 = sorted(one_to_many, key=itemgetter(0))
    print(res1)

    print('\nЗадание Б2')
    res2 = []
    for d in dbs:
        count = len([x for x in one_to_many if x[2] == d.name])
        if count > 0:
            res2.append((d.name, count))
    res2 = sorted(res2, key=itemgetter(1), reverse=True)
    print(res2)

    print('\nЗадание Б3')
    res3 = {}
    for p in procs:
        if p.name.endswith('ов'):
            res3[p.name] = [x[2] for x in many_to_many if x[0] == p.name]
    print(res3)


if __name__ == '__main__':
    main()
