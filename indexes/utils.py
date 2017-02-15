class ValueWindow:
    __arr = []
    __window = []
    __n = 0
    __p = -1

    def __init__(self, arr, n):
        self.__arr = arr
        self.__n = n

    def next(self, func):
        # new obj
        if -1 == self.__p:
            for i in range(0, min(len(self.__arr), self.__n)):
                self.__window.append(self.__arr[i])
            self.__p = 0
            return list(map(func, self.__window))

        del self.__window[0]

        if self.__p + self.__n < len(self.__arr):
            self.__window.append(self.__arr[self.__p + self.__n])
            self.__p += 1

        return list(map(func, self.__window))

    def cur_index(self):
        return self.__window[-1]


if __name__ == '__main__':
    window = ValueWindow(range(0, 21), 5)
    cur = window.next(lambda s: s)
    while len(cur) == 5:
        print(cur)
        cur = window.next(lambda s: s)
