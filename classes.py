class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def drive(self):
        print(f"{self.make} {self.model} is driving")

    def get_vehicle_info(self):
        print(f"{self.make} {self.model}")

my_car = Vehicle("Honda", "Civic")
# print(my_car.make)
# print(my_car.model)
my_car.drive()
my_car.get_vehicle_info()

class Airplane(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
        self.wings = 2

    def drive(self):
         print(f"{self.make} {self.model} is flying")


class Helicopter(Vehicle):
    def __init__(self, make, model, wings):
        super().__init__(make, model)

    def drive(self):
        print(f"{self.make} {self.model} is hovering")

class Boat(Vehicle):
    pass


my_plane = Airplane("Boeing", "747")
my_plane.drive()
my_plane.get_vehicle_info()

my_helicopter = Helicopter("Cessna", "172", 2)
my_helicopter.drive()
my_helicopter.get_vehicle_info()

my_boat = Boat("Honda", "Civic")
my_boat.drive()
my_boat.get_vehicle_info()