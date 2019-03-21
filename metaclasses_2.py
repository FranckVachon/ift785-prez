import inspect
from abc import ABCMeta, abstractmethod
from multiple_inheritance import Component, FixedComponent, BorinComponent, Window, Draggable, Interactive


""" Interfaces  
Les Interfaces en Java sont souvvent amenées comme une mnaière de pallier au manque d'héritage (ou comme une meilleure
solution à celui-ci). Cependant, elles peuvent être un outils intéressants en temps que tel. On peut reproduire
une equivalence des interfaces en python avec les métaclasses & les méthodes abstraites.
"""


class DraggableWindowInterface(metaclass=ABCMeta):
    @abstractmethod
    def close(self):pass
    @abstractmethod
    def release(self):pass
    @abstractmethod
    def dragging(self,pos):pass

class BrokenComponent(DraggableWindowInterface, Window, Draggable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
# mc = BrokenComponent(pos=(42,42), size=100, foo="bar")

class WorkingComponent(DraggableWindowInterface, Window, Draggable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def close(self):
        super().close()
    def release(self):
        super().release()
    def dragging(self,pos):
        super().dragging(pos)
wmc = WorkingComponent(pos=(42,42), size=100, foo="bar")

if isinstance(wmc, DraggableWindowInterface):
    print("That'll work")


""" Problème: dans notre code, on doit à un certain moment s'assurer qu'un objet satisfasse ces comportements:
- Draggable
- Window
- Interactive

Supposons que notre hiérarchie soit beaucoup plus étendue que celle contenue dans multiple_inheritance. Supposons aussi
que cette vérification soit nécessaire potentiellement à plusieurs endroits séparés du code. Finalement, on pourrait 
devoir vérifier d'autres comportements plus tard.
 """

compo = Component((1,2),size=5, foo="bar")
fix_compo = FixedComponent(pos=(3,4),size=10, foo="fixedbar")
boring = BorinComponent()



# Option1: utiliser isinstance ou type
def check_me(obj):
    print("\n Checking component of cls: " + obj.__class__.__name__)
    if isinstance(obj, Draggable):
        if isinstance(obj, Window):
           if isinstance(obj,Interactive):
                print("I got it!")
    else:
        print("Sorry, can't do all that\n")

# Option2: try/catch
def try_me(obj):
    try:
        print("\n Try/catch component of cls: " + obj.__class__.__name__)
        obj.close()
        obj.to_string()
        obj.dragging(dpos=(5, -5))
        print(obj.__class__.__name__ + " object can do everything!")
    except:
        print(obj.__class__.__name__+ " couldn't do all that!")


# check_me(compo)
# check_me(boring)
#
# try_me(compo)
# try_me(boring)


""" Une meilleure solution: utiliser une métaclasse & register() """

from abc import ABCMeta

class LyingChild:
    def __init__(self, **kwargs):
        pass
class TrueChild(Window,Draggable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class GrandChild(TrueChild):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class DraggableInteractiveWindow(metaclass=ABCMeta):
    pass

DraggableInteractiveWindow.register(LyingChild)
DraggableInteractiveWindow.register(TrueChild)

lying_child = LyingChild(pos=(1,2),size=5, foo="bar")
true_child = TrueChild(pos=(3,4),size=10, foo="fixedbar")
grand_child = GrandChild(pos=(5,5),size=10, foo="bar")


# True dans les 3 cas
print(isinstance(lying_child, DraggableInteractiveWindow))
print(isinstance(true_child, DraggableInteractiveWindow))
print(isinstance(grand_child, DraggableInteractiveWindow))

grand_child.release()       # ok
true_child.release()        # ok
lying_child.release() # AttributeError: no attribute "release"


"""
STRENGTH: 
- We inherit the metaclasses - so children of registered classes are also registered classes
- We only need to do one check regardless of the # of behaviours (classes) involved - we just need a new ABC
for that behaviour profile & then check against that only
- Adding a class that adheres to a behaviour profile only requires registering one new class to the ABC and is always
done in the same place (the ABC)

WEAKNESSES:
- Should you NEED to type check? Are there better architectures that would require less type check?
- A register() is a promise. It is not enforced, nor is it enforceable.
"""

