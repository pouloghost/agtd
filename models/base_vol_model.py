from models.base_model import BaseModel


class BaseVolModel(BaseModel):
    __vol = 0

    def __init__(self, raw):
        BaseModel.__init__(self, raw)
        parts = raw.split('\t')
        if len(parts) < 8:
            print(raw, " error format base vol")
            return
        self.__vol = float(parts[7])

    def __repr__(self):
        return BaseModel.__repr__(self) + '\t' + str(self.__vol)


if __name__ == '__main__':
    print('AG', BaseVolModel(
        '2017-2-9	4078	4107	4075	4082	14	0.34%	3921628.00	4089	16035536896.00'))

