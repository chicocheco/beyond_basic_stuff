import collections.abc
import operator


class WizCoinException(Exception):
    """The wizcoin module raises this when the module is misused."""
    pass


class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        """Create a new WizCoin object with galleons, sickles, and knuts."""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        # NOTE: __init__() methods NEVER have a return statement.

    def value(self):
        """The value (in knuts) of all the coins in this WizCoin object."""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + self.knuts

    def weight_in_grams(self):
        """Returns the weight of the coins in grams."""
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)

    # --snip--

    @property
    def galleons(self):
        """Returns the number of galleon coins in this object."""
        return self._galleons

    @galleons.setter
    def galleons(self, value):
        # Using setters to validate data
        if not isinstance(value, int):
            raise WizCoinException('galleons attr must be set to an int, not a ' + value.__class__.__qualname__)
        if value < 0:
            raise WizCoinException('galleons attr must be a positive int, not ' + value.__class__.__qualname__)
        self._galleons = value

    @property
    def total(self):
        """Total value (in knuts) of all the coins in this WizCoin object."""
        # Read-only property (when there is no setter or deleter method for e.g. 'total') so you can't do wc.total = 100
        return (self.galleons * 17 * 29) + (self.sickles * 29) + self.knuts

    # comparison dunder methods
    def _comparison_operator_helper(self, operator_func, other):  # higher-order function
        """A helper method for our comparison dunder methods."""
        if isinstance(other, WizCoin):
            return operator_func(self.total, other.total)
        elif isinstance(other, (int, float)):
            return operator_func(self.total, other)
        elif isinstance(other, collections.abc.Sequence):
            other_value = (other[0] * 17 * 29) + (other[1] * 29) + other[2]
            return operator_func(self.total, other_value)
        elif operator_func == operator.eq:
            return False
        elif operator_func == operator.ne:
            return True
        else:
            return NotImplemented

    def __eq__(self, other):  # eq is "EQual"
        return self._comparison_operator_helper(operator.eq, other)

    def __ne__(self, other):  # ne is "Not Equal"
        return self._comparison_operator_helper(operator.ne, other)

    def __lt__(self, other):  # lt is "Less Than"
        return self._comparison_operator_helper(operator.lt, other)

    def __le__(self, other):  # le is "Less than or Equal"
        return self._comparison_operator_helper(operator.le, other)

    def __gt__(self, other):  # gt is "Greater Than"
        return self._comparison_operator_helper(operator.gt, other)

    def __ge__(self, other):  # ge is "Greater than or Equal"
        return self._comparison_operator_helper(operator.ge, other)


"""
Don’t confuse read-only properties with constant variables. Constant variables are written in all uppercase and 
rely on the programmer to not modify them. 
"""
