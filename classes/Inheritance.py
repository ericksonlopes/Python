class Main:
    def __init__(self):
        self.name = "John"
        self.size = 100


class SeekAttr(Main):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    main = Main()

    print(main.name, main.size)

    seek = SeekAttr()

    print(seek.name, seek.size)
