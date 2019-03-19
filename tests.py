from abc import ABCMeta


class MyClass(metaclass=ABCMeta):
    pass

MyClass.register(list)

print(issubclass(tuple, MyClass))
print(issubclass(list, MyClass))