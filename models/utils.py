def array_from_file(cls, path, limit=-1):
    results = []
    with open(path, encoding='utf-8') as f:
        # table header
        f.readline()
        i = 0
        line = f.readline()
        while line is not None and len(line.strip('\n')) > 0:
            results.append(cls(line.replace('\n', '')))

            i += 1
            line = f.readline()
            if i == limit:
                line = None
    return results


class DateValue:
    __date = None
    __value = 0

    def __init__(self, date, value):
        self.__date = date
        self.__value = value

    def get_value(self):
        return self.__value

    def get_date(self):
        return self.__date

    def __repr__(self):
        return '\t'.join([str(self.__date), str(self.__value)])


class MA(DateValue):
    def __init__(self, rsv, last, alpha, date):
        DateValue.__init__(self, date, alpha * rsv + (1 - alpha) * last)
