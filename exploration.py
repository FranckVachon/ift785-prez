import inspect
import multiple_inheritance




""" Intro à Python: tout un est un objet. Mais qu'est-ce qu'un objet?
- Il peut avoir des attributs (optionel)
- Il peut avoir des méthodes (optionel)
- On peut le sous-classer
- On peut le passer en argument ou comme attribut d'un autre objet (s'il est d'un type acceptable)
 """

# Tout est sous-classable
class MyInt(int):             # sous-class de int
    def double_me(self):      # nouvelle méthode
        return self.real*2    # .real ==> valeur du int
    def __str__(self):        # override string rep.
        return "42 is the best number"

regular_int = 66
my_int = MyInt(66)
print(my_int*2)                # 132
print(my_int.double_me())      # 132
print(str(my_int))             # "42 is the best number"
print(str(regular_int))        # 66


""" Il faut avoir une racine à l'arbre d'héritage. 
    En python, il s'agit de la classe 'object'.
    Qu'est-ce donc que cette classe object?"""
print(inspect.getmro(MyInt))


class MyClass:
    my_class_attribute = 'bar'
    def __init__(self):
        self.my_atttribute = 42
    def my_func(self):
        return "foo"
    def my_metho(self):
        return "foobar"
o = MyClass()

print("\nUne méthode EST objet: assignable à une variable: ")
method_objet = MyClass.my_func
print(method_objet.__class__)
print("Un attribut EST objet, que l'on peut assigner: ")
att_obj = o.my_atttribute
print(att_obj.__class__)
print("\nSi on peut assigner: dictionnaire de méthodes:")
dict_methos = {'my_func':o.my_func, 'my_method': MyClass.my_metho}
print(dict_methos['my_func']())      # foo
print(dict_methos['my_method'](''))  # foobar
print("\nMais méthod class != méthod instance!")
CLS = MyClass.my_func
OBJ = o.my_func
print("cls.metho == obj.metho? " + str(MyClass.my_func is o.my_func))


# Récupérons les constituants de la classe "object" par instrospection
o_attributes = sorted([att for att in dir(object) if not callable(getattr(object, att))])
o_methods = sorted([att for att in dir(object) if callable(getattr(object, att))])

# Récupérons ceux de MyClass
mc_attributes = sorted([att for att in dir(o) if not callable(getattr(o, att))])
mc_methods = sorted([att for att in dir(o) if callable(getattr(o, att))])

# Et faisons un disjonction pour savoir ce qui diffère
print("\nDifférence d'attributs: ")
print(list(set(o_attributes) ^ set(mc_attributes)))
print("Différence méthodes: ")
print(list(set(o_methods) ^ set(mc_methods)))


""" Les attributs & méthodes définis dans MyClass sont tous présents (évidemment absent de object.
__doc__ est issue de la documentation python, absent de MyClass puisque nous ne l'avons pas (re)définit.

__weakref__ garde une list des références à un objet courant pour le garbage collector. En Python, une instance
est effacée s'il n'y a plus de (weak) références à cette instance.

__module__ est le module dans lequel est définie la classe (__main__ ou metaclass.py pour MyClass, rien pour object)

Le reste sont des attributes & méthodes propres à MyClass
"""
some_var = o
some_var.my_atttribute = 4

print(o.__dict__)
print("\no's instance __dict__")
print(o.__dict__)
print(MyClass.__dict__)
print(MyClass.__dict__['my_class_attribute'])


o_attributes = sorted([att for att in dir(o) if not callable(getattr(o, att))])
o_methods = sorted([att for att in dir(o) if callable(getattr(o, att))])

print("Python's Object class attributes: ")
print(o_attributes)
print("Python's Object class methods: ")
print(o_methods)


print("\n A method is also an object: ")
o_repr = o.__repr__
o_eq = o.__eq__
print(o_repr.__class__)
repr_attributes = sorted([att for att in dir(o_repr) if not callable(getattr(o_repr, att))])
repr_methods = sorted([att for att in dir(o_repr) if callable(getattr(o_repr, att))])

print("Method wrapper's class attributes: ")
print(list(set(o_attributes) ^ set(repr_attributes)))
print("Method wrapper's class methods: ")
print(list(set(o_methods) ^ set(repr_methods)))

sor = sorted
print(sor.__class__)
o_attributes = sorted([att for att in dir(sor) if not callable(getattr(sor, att))])
o_methods = sorted([att for att in dir(sor) if callable(getattr(sor, att))])

print("Python's sorted attributes: ")
print(o_attributes)
print("Python's sorted methods: ")
print(o_methods)