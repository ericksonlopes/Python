class MyClass:
    def __init__(self):
        self._query_protect = "select * from table"

    def _method_protect(self):
        print("This is a protected method")
        print("The query is: ", self._query_protect)
