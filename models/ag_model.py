from models.base_vol_model import BaseVolModel


class AG(BaseVolModel):
    __avg = 0
    __vol_money = 0

    def __init__(self, raw):
        BaseVolModel.__init__(self, raw)
        parts = raw.split('\t')
        if len(parts) < 10:
            print(raw, " error format ag")
            return
        self.__avg = float(parts[8])
        self.__vol_money = float(parts[9])

    def __repr__(self):
        return '\t'.join([BaseVolModel.__repr__(self), str(self.__avg), str(self.__vol_money)])


if __name__ == '__main__':
    print('AG', AG(
        '2017-2-9	4078	4107	4075	4082	14	0.34%	3921628.00	4089	16035536896.00'))
