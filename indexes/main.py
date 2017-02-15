from indexes.bias import calculate as c
from models.ag_model import AG
from models.utils import *


def calculate(vals):
    return c(vals, 6)


if __name__ == '__main__':
    ags = array_from_file(AG, 'D:\MyCode\python\\agtd\\ag.txt')
    ags.reverse()

    indexes = calculate(ags)

    print(indexes[-1])
