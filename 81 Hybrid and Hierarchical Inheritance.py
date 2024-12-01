# Hybrid inheritance:It is combinaton of multiple inheritance and single inheritance in oop.

class baseclass:
    pass

class derived1(baseclass):
    pass

class derived2(baseclass):
    pass
class derived3(derived1,derived2):
    pass




# Hierchical inheritance:(tree like structure) It is type of inheritance in OOP where multiple subclasses inherit from a single base class.In other words ,a single base class acts as a parent class for multiple subclass.

class basecl:
    pass
class d1(basecl):
    pass

class d2(basecl):
    pass

class d3(d1):
    pass

