"""Multiple inheritance is straightforward as long as the parent classes’
method names are distinct and don’t overlap. These sorts of classes are
called mixins."""


class Airplane:
    def fly_in_the_air(self):
        print('Flying...')


class Ship:
    def float_on_water(self):
        print('Floating...')


class FlyingBoat(Airplane, Ship):
    """No overlapping methods. You can call both float_on_water() as wel as fly_in_the_air() methods."""
    pass
