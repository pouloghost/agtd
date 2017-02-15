from indexes.utils import ValueWindow


class RSI:
    __date = None
    __value = 0

    def __init__(self, span, date):
        self.__date = date
        a = 0
        b = 0
        for diff in span:
            if diff > 0:
                a += diff
            else:
                b -= diff

        self.__value = a / (a + b) * 100

    def set(self, date, value):
        self.__date = date
        self.__value = value

    def __repr__(self):
        return '\t'.join([str(self.__date), str(self.__value)])


def get_diff(m):
    return m.get_diff()


def calculate(base_models, n):
    rsis = []
    window = ValueWindow(base_models, n)
    cur = window.next(get_diff)
    while len(cur) == n:
        model = window.cur_index()
        rsis.append(RSI(cur, model.get_date()))
        cur = window.next(get_diff)

    return rsis


if __name__ == '__main__':
    print(RSI([2, -2, 3, 3, 3, -4, 2, -5, -6, 1, 1, 1, -3, -3], '2017-02-09'))
