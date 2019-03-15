import inspect
import multiple_inheritance
class MyClass:
    my_class_attribute = 'bar'
    def __init__(self):
        self.my_atttribute = 42
    def my_func(self):
        return "foo"
    def my_metho(self):
        return "foobar"

o = MyClass()



""" Intro à Python: tout un est un objet. Mais qu'est-ce qu'un objet?
- Il peut avoir des attributs (optionel)
- Il peut avoir des méthodes (optionel)
- On peut le sous-classer
- On peut le passer en argument ou comme attribut d'un autre objet (s'il est d'un type acceptable)
 """

# On peut sous-classer même les types de bases, comme int (integer)
class MyInt(int):               # sous-class de int
    def double_me(self):        # définir une nouvelle méthode
        return self.real*2      # real est l'attribut contenant la valeur (réelle) d'un int
    def __str__(self):         # équivalent du to_string() de int
        return "My favorite number will always be 42"

regular_int = 66
my_int = MyInt(66)
print(my_int*2)                # 132
print(my_int.double_me())      # 132
print(str(my_int))             # "My favorite number will always be 42"
print(str(regular_int))        # 66

# On peut faire un dictionnaire de méthodes, car les méthodes sont des objets et on peut les appeler
dict_methos = {'dble_me':my_int.double_me}
print(dict_methos['dble_me']())             #132

""" Il faut avoir une racine à l'arbre d'héritage. En python, il s'agit de la classe 'object'.
 Qu'est-ce donc que cette classe object?"""
print(inspect.getmro(MyInt))            # MyInt --->-- int ---->--- object

# Récupérons les constituants de la classe objet par instrospection
print("\n Les attributs & méthodes de la classe objet")
object_attributes = sorted([att for att in dir(object) if not callable(getattr(object, att))])
object_methods = sorted([att for att in dir(object) if callable(getattr(object, att))])
print(object_attributes)
print(object_methods)

# Récupérons ceux de MyClass
MyClass_attributes = sorted([att for att in dir(o) if not callable(getattr(o, att))])
MyClass_methods = sorted([att for att in dir(o) if callable(getattr(o, att))])

# Et faisons un disjonction pour savoir ce qui diffère
print("\nDifférence d'attributs: ")
print(list(set(object_attributes)^set(MyClass_attributes)))
print("Différence méthodes: ")
print(list(set(object_methods)^set(MyClass_methods)))


""" Les attributs & méthodes définis dans MyClass sont tous présents (évidemment absent de object.
__doc__ est issue de la documentation python, absent de MyClass puisque nous ne l'avons pas (re)définit.

__weakref__ garde une list des références à un objet courant pour le garbage collector. En Python, une instance
est effacée s'il n'y a plus de (weak) références à cette instance.

__module__ est le module dans lequel est définie la classe (__main__ ou metaclass.py pour MyClass, rien pour object)

Le reste sont des attributes & méthodes propres à MyClass

"""


print("\nUne méthode est un objet, que l'on peut donc assigner à un variable: ")
method_objet = MyClass.my_func
print(method_objet.__class__)
print("Un attribut est un objet, que l'on peut aussi assigner: ")
att_obj = o.my_atttribute
print(att_obj.__class__)

print("\no's instance __dict__")
print(o.__dict__)
print(MyClass.__dict__)
print(MyClass.__dict__['my_class_attribute'])


object_attributes = sorted([att for att in dir(o) if not callable(getattr(o, att))])
object_methods = sorted([att for att in dir(o) if callable(getattr(o, att))])

print("Python's Object class attributes: ")
print(object_attributes)
print("Python's Object class methods: ")
print(object_methods)


print("\n A method is also an object: ")
o_repr = o.__repr__
o_eq = o.__eq__
print(o_repr.__class__)
repr_attributes = sorted([att for att in dir(o_repr) if not callable(getattr(o_repr, att))])
repr_methods = sorted([att for att in dir(o_repr) if callable(getattr(o_repr, att))])

print("Method wrapper's class attributes: ")
print(list(set(object_attributes)^set(repr_attributes)))
print("Method wrapper's class methods: ")
print(list(set(object_methods)^set(repr_methods)))

sor = sorted
print(sor.__class__)
object_attributes = sorted([att for att in dir(sor) if not callable(getattr(sor, att))])
object_methods = sorted([att for att in dir(sor) if callable(getattr(sor, att))])

print("Python's sorted attributes: ")
print(object_attributes)
print("Python's sorted methods: ")
print(object_methods)