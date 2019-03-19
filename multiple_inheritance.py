import os, sys
import inspect

class Interactive:
    def __init__(self, foo=None, **kwargs):
        self.foo = foo
        print(Interactive.__qualname__+ "." +  str(sys._getframe().f_code.co_name) + " " + str(foo))
    def to_string(self):
        return " Interactive "

class Draggable(Interactive):
    def __init__(self, pos, **kwargs):
        print(Draggable.__qualname__ + "." +  str(sys._getframe().f_code.co_name) + " " + str(pos))
        self.pos = pos
        self.shadow_pos = pos
        super().__init__(**kwargs)
    def dragging(self, dpos):
        self.shadow_pos  =  [sum(x) for x in zip(self.shadow_pos,dpos)]
        print(Draggable.__qualname__ + "." +  str(sys._getframe().f_code.co_name) + " " + str(self.shadow_pos))
    def release(self):
        self.pos = self.shadow_pos
        self.shadow_pos = self.pos
        print(self.__class__.__name__ + "." +  str(sys._getframe().f_code.co_name) + " " + str(self.pos))
    def to_string(self):
        return " Draggable " + super().to_string()

class Window(Interactive):
    def __init__(self, size, **kwargs):
        self.size = size
        super().__init__(**kwargs)
        print(Window.__qualname__+ "." +  str(sys._getframe().f_code.co_name) + " " + str(size))
    def close(self):
        print(" (Window.close) bye bye now... ")
    def to_string(self):

        return " Window " + super().to_string()

class Component(Draggable, Window):
    def __init__(self, pos, size, foo=None):
        super().__init__(pos=pos, size=size, foo=foo)
    def to_string(self):
        return "I'm a" + super().to_string() + " Component "

class FixedComponent(Window):
    def __init__(self, pos, size, foo=None):
        super().__init__(pos=pos, size=size, foo=foo)
    def to_string(self):
        return "I'm a" + super().to_string() + " Component "

class BorinComponent:
    def to_string(self):
        return "I do nothing at all"

def demo_multiple_1(args):
    c = Component(pos=(42,42), size=100, foo="bar")
    print("Component obj attributes: " + str([att for att in dir(c) if not att.startswith('__') and not callable(getattr(c,att))]))

    c.dragging(dpos=(12,-5))
    c.dragging(dpos=(-7,7))
    c.release()
    c.close()
    ans = c.to_string()
    print(ans)


    print(inspect.getmro(Component))

def demo_diamond(args):
    pass


if __name__ == '__main__':

    import sys
    args = sys.argv[1:]
    demo_multiple_1(args)