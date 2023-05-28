class Main:
    def __init__(self):
        self.name = "Erickson"


class Master:
    def __init__(self):
        self.size = 200


class SeekAttr(Master, Main):
    def __init__(self):
        Master.__init__(self)
        Main.__init__(self)


if __name__ == '__main__':
    seek = SeekAttr()

    print(seek.size, seek.name)
