"""it’s often favorable to use a technique called composition for classes with “has a” relationships.
Composition is the class design technique of including objects in your class
rather than inheriting those objects’ class."""

import wizcoin


class WizardCustomer(wizcoin.WizCoin):
    """DO NOT DO THIS. The wizard.value() and wizard.weightInGrams() method names are misleading: it seems like they
    would return the wizard’s value and weight rather than the value and weight of the wizard’s coins. """

    def __init__(self, name):
        self.name = name
        super().__init__(0, 0, 0)


wizard = WizardCustomer('Alice')
print(f'{wizard.name} has {wizard.value()} knuts worth of money.')
print(f'{wizard.name}\'s coins weigh {wizard.weight_in_grams()} grams.')


class WizardCustomer:
    """DO THIS. When you use composition, any changes to the WizCoin class’s methods won’t change the WizardCustomer
    class’s methods. This technique offers more flexibility in future design changes for both classes and leads to
    more maintainable code."""

    def __init__(self, name):
        self.name = name
        self.purse = wizcoin.WizCoin(0, 0, 0)


wizard = WizardCustomer('Alice')
print(f'{wizard.name} has {wizard.purse.value()} knuts worth of money.')
print(f'{wizard.name}\'s coins weigh {wizard.purse.weight_in_grams()} grams.')
