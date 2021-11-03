# Inheritance example. Car is a Vehicle. Motorcycle is a Vehicle. LunarRover is a Vehicle.
class Vehicle:
    def __init__(self):
        print('Vehicle created.')

    def start_ignition(self):
        pass  # Ignition starting code goes here.

    def change_tire(self):
        pass  # Tire changing code goes here.


class Car(Vehicle):
    def __init__(self):
        print('Car created.')


class Motorcycle(Vehicle):
    def __init__(self):
        print('Motorcycle created.')


class LunarRover1(Vehicle):
    def __init__(self):
        print('LunarRover created.')


"""What if I want to add a change_spark_plug() method which apply only to vehicles with a combustion engine like cars
and motorcycles?

By favoring composition over inheritance, we can create separate CombustionEngine and ElectricEngine classes. Then we 
design the Vehicle class so it “has an” engine attribute, either a CombustionEngine or ElectricEngine object, 
with the appropriate methods: """


# Composition example. Vehicle has a CombustionEngine (default) or ElectricEngine.
class CombustionEngine:
    def __init__(self):
        print('Combustion engine created.')

    def change_spark_plug(self):
        pass  # Spark plug changing code goes here.


class ElectricEngine:
    def __init__(self):
        print('Electric engine created.')


class Vehicle:
    def __init__(self):
        print('Vehicle created.')
        self.engine = CombustionEngine()  # Use this engine by default.


# --snip--
class LunarRover(Vehicle):
    def __init__(self):
        print('LunarRover created.')
        self.engine = ElectricEngine()


# Or you might want to simply have the change_spark_plug() method for LunarVehicle do nothing.
class LunarRover(Vehicle):
    change_spark_plug = None  # For when composition was not used, just neutralize this change_spark_plug method

    def __init__(self):
        print('LunarRover created.')
