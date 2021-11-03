"""
Turning an Attribute into a Property

In Python you can easily change an attribute's value. You can imply that a particular attribute should not by modified
outside the class by adding a leading _ (underscore) or convert them to properties.
"""


# 1) Example using private attributes
class ClassWithRegularAttributes:
    def __init__(self, some_parameter):
        self._some_attribute = some_parameter  # you should not change it, but you can anyway


"""
obj = ClassWithRegularAttributes('some initial value')
print(obj._some_attribute) # Prints 'some initial value'
obj._some_attribute = 'changed value'
print(obj._some_attribute) # Prints 'changed value'
del obj._some_attribute # Deletes the some_attribute attribute.
"""


# 2) Example using properties
class ClassWithProperties:
    def __init__(self):
        self.some_attribute = 'some initial value'

    @property
    def some_attribute(self):
        # _some_attribute is a private attribute
        # but in the context of getter, setter and deleter methods,
        # this attribute is called backing field or backing variable
        return self._some_attribute

    @some_attribute.setter
    def some_attribute(self, value):
        self._some_attribute = value

    @some_attribute.deleter
    def some_attribute(self):
        del self._some_attribute


"""
WARNING!
Do not ever use the property (variable without _ prefix) inside the getter, setter or deleter methods.

To prevent this recursion, the code inside your getter, setter, and deleter methods should always act on the backing 
variable (which should have an underscore prefix in its name), never the property. Code outside these methods should 
use the property, although as with the private access underscore prefix convention, nothing prevents you from 
writing code on the backing variable anyway.
"""


class ClassWithBadProperty:
    def __init__(self):
        self.some_attribute = 'some initial value'

    @property
    def some_attribute(self):  # This is the "getter" method.
        # We forgot the _ underscore in `self._some_attribute here`, causing us to use the property and call the
        # getter method again:
        return self.some_attribute  # This calls the getter again!

    @some_attribute.setter
    def some_attribute(self, value):
        self._someAttribute = value  # This is the "setter" method.


obj = ClassWithBadProperty()
print(obj.some_attribute)  # Error because the getter calls the getter.

"""Note: The most common need for using properties is to validate data or to make
sure it’s in the format you want it to be in. See the example of wizcoin."""
