class Main:
    def __getattr__(self, attr):
        setattr(self, attr, "default")
        return attr


class SeekAttr(Main):
    def __getattr__(self, attr):
        return super().__getattr__(attr)


if __name__ == '__main__':
    master = Main()

    master.name = "John"
    master.size = 100

    print(master.name, master.size)

    seek = SeekAttr()
    seek.name = "Maria"
    seek.size = 200

    print(seek.name, seek.size)
