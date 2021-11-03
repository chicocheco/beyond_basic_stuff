"""It’s common to say that parent-child classes represent “is a” relation-
ships. A ChildClass object is a ParentClass object because it has all the same
methods that a ParentClass object has, including some additional methods it
defines. This relationship is one way: a ParentClass object is not a ChildClass
object."""


class ParentClass:
    def print_hello(self):
        print('Hello, world!')


class ChildClass(ParentClass):
    def some_new_method(self):
        print("ParentClass objects don't have this method.")


class GrandchildClass(ChildClass):
    def another_new_method(self):
        print('Only GrandchildClass objects have this method.')


print('Create a ParentClass object and call its methods:')
parent = ParentClass()
parent.print_hello()
print('Create a ChildClass object and call its methods:')
child = ChildClass()
child.print_hello()
child.some_new_method()
print('Create a GrandchildClass object and call its methods:')
grandchild = GrandchildClass()
grandchild.print_hello()
grandchild.some_new_method()
grandchild.another_new_method()
print('An error:')
parent.someNewMethod()
