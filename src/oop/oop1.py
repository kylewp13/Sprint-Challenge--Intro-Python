# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# base class for Vehicle
class Vehicle:
    pass

# class for GroundVehicle
class GroundVehicle(Vehicle):
    pass

# class for FlightVehicle
class FlightVehicle(Vehicle):
    pass

# class for Starship
class Starship(FlightVehicle):
    pass

# class for Airplane
class Airplane(FlightVehicle):
    pass

# class for Car
class Car(GroundVehicle):
    pass

# class for Motorcycle
class Motorcycle(GroundVehicle):
    pass