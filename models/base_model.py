from datetime import *


class BaseModel:
    # fields
    __date = None
    __open = 0
    __high = 0
    __low = 0
    __close = 0
    __diff = 0
    __diff_per = 0

    def __init__(self, raw):
        parts = raw.split('\t')
        if len(parts) < 7:
            print(raw, " error format base")
            return

        date_parts = list(map(lambda s: int(s), parts[0].split('-')))

        if not len(date_parts) == 3:
            print(parts[0], " error format")
            return

        self.__date = date(date_parts[0], date_parts[1], date_parts[2])

        self.__open = float(parts[1])
        self.__high = float(parts[2])
        self.__low = float(parts[3])
        self.__close = float(parts[4])
        self.__diff = float(parts[5])

        origin_per = parts[6]
        per_index = origin_per.find('%')
        if not per_index == -1:
            self.__diff_per = float(origin_per[:per_index])
        else:
            self.__diff_per = float(origin_per)

    def __repr__(self):
        return '\t'.join([str(self.__date), str(self.__open), str(self.__high),
                          str(self.__low), str(self.__close), str(self.__diff), str(self.__diff_per)])

    def get_date(self):
        return self.__date

    def get_diff(self):
        return self.__diff

    def get_close(self):
        return self.__close

    def get_high(self):
        return self.__high

    def get_low(self):
        return self.__low


if __name__ == '__main__':
    print("AG", BaseModel(
        "2017-2-9	4078	4107	4075	4082	14	0.34%	3,921,628.00	4089	16,035,536,896.00"))
    print("USD", BaseModel("2017-2-9	100.24	100.67	100.08	100.65	0.39	0.39%	335700"))
