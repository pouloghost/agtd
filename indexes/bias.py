from datetime import date
from functools import reduce

from models.base_model import BaseModel
from models.utils import DateValue


def add(x, y):
    if isinstance(x, BaseModel):
        x = x.get_close()
    if isinstance(y, BaseModel):
        y = y.get_close()

    return x + y


def calculate(base_models, n):
    biass = []
    total = reduce(add, base_models[0:n])
    last = base_models[n - 1].get_close()

    for i in range(n - 1, len(base_models)):
        now = base_models[i]
        total -= last
        total += now.get_close()
        value = (now.get_close() / total * n - 1) * 100
        biass.append(DateValue(now.get_date(), value))

        if now.get_date() == date(2017, 2, 9):
            print(str(i), str(now.get_close()), str(total), str(last), str(value))

        last = base_models[i - n + 1].get_close()

    return biass
