#!/usr/bin/env python
# Written by: DGC

#==============================================================================
class Vehicle(object):

    def __init__(self, type_name):
        self.type = type_name
        self.wheels = None
        self.doors = None
        self.seats = None

    def view(self):
        print(
            "This vehicle is a " +
            self.type +
            " with; " +
            str(self.wheels) +
            " wheels, " +
            str(self.doors) +
            " doors, and " +
            str(self.seats) +
            " seats."
            )

#==============================================================================
class VehicleBuilder(object):
    """
    An abstract builder class, for concrete builders to be derived from.
    """
    def __init__(self):
        self.vehicle = None

    def make_wheels(self):
        raise NotImplementedError

    def make_doors(self):
        raise NotImplementedError

    def make_seats(self):
        raise NotImplementedError

    def build(self):
        self.make_wheels()
        self.make_doors()
        self.make_seats()
        return self.vehicle

#==============================================================================
class CarBuilder(VehicleBuilder):

    def __init__(self):
        self.vehicle = Vehicle("Car ")

    def make_wheels(self):
        self.vehicle.wheels = 4

    def make_doors(self):
        self.vehicle.doors = 3

    def make_seats(self):
        self.vehicle.seats = 5

#==============================================================================
class BikeBuilder(VehicleBuilder):

    def __init__(self):
        self.vehicle = Vehicle("Bike")

    def make_wheels(self):
        self.vehicle.wheels = 2

    def make_doors(self):
        self.vehicle.doors = 0

    def make_seats(self):
        self.vehicle.seats = 2

#==============================================================================
if (__name__ == "__main__"):
    car_maker = CarBuilder()
    car = car_maker.build()
    car.view()

    bike_maker = BikeBuilder()
    bike = bike_maker.build()
    bike.view()
