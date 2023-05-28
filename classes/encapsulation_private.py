class MyClass:
    def __init__(self):
        self.__value_private = 56
        self.__method_private()

    def __method_private(self):
        print("This is a private method")
        print("The value is: ", self.__value_private)
