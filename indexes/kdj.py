import sys

from indexes.utils import ValueWindow
from models.utils import DateValue, EMA


def get_close(m):
    return m.get_high(), m.get_low()


def get_value(m):
    return m.get_value()


class RSV(DateValue):
    def __init__(self, cur, c, date):
        high = 0
        low = sys.maxsize
        for (h, l) in cur:
            if h > high:
                high = h
            if l < low:
                low = l
        value = (c - low) / (high - low) * 100
        DateValue.__init__(self, date, value)


class KDJ:
    __date = None
    __k = 50
    __d = 50
    __j = 50

    def __init__(self, k, d, j, date):
        self.__k = k
        self.__d = d
        self.__j = j
        self.__date = date

    def __repr__(self):
        return '\t'.join([str(self.__date), str(self.__k), str(self.__d), str(self.__j)])


def calculate(base_models, rsv_n, kd_n):
    rsvs = get_rsv(base_models, rsv_n)

    ks = get_k(kd_n, rsvs)

    date_d = get_d(kd_n, ks)

    kdjs = get_all(date_d, kd_n, ks)

    return kdjs


def get_all(date_d, kd_n, ks):
    kdjs = []
    for k in ks:
        date = k.get_date()
        d = date_d[date]
        k_v = k.get_value()
        d_v = d.get_value()

        kdjs.append(KDJ(k_v, d_v, kd_n * k_v - (kd_n - 1) * d_v, date))
    return kdjs


def get_d(kd_n, ks):
    date_d = {}
    ds = []
    for d_k in ks:
        last_d = 50
        if not 0 == len(ds):
            last_d = ds[-1].get_value()
        d = EMA(d_k.get_value(), last_d, 1 / kd_n, d_k.get_date())
        ds.append(d)
        date_d[d.get_date()] = d
    return date_d


def get_k(kd_n, rsvs):
    ks = []
    for k_rsv in rsvs:
        last_k = 50
        if not 0 == len(ks):
            last_k = ks[-1].get_value()
        ks.append(EMA(k_rsv.get_value(), last_k, 1 / kd_n, k_rsv.get_date()))
    return ks


def get_rsv(base_models, rsv_n):
    rsvs = []
    rsv_window = ValueWindow(base_models, rsv_n)
    rsv_cur = rsv_window.next(get_close)
    while rsv_n == len(rsv_cur):
        rsv_index = rsv_window.cur_index()
        rsvs.append(RSV(rsv_cur, rsv_index.get_close(), rsv_index.get_date()))
        rsv_cur = rsv_window.next(get_close)
    return rsvs
