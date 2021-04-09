from vars_properties import print_vars


class MyClass():
    def __init__(self):
        pass


def foo():
    a = 1
    b = MyClass()
    c = [1, 2, 3]
    print_vars()


if __name__ == '__main__':
    foo()
