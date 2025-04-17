class Animal:
    """Base class for animals with a move action."""
    def __init__(self, name):
        self.name = name

    def move(self):
        """Generic move action."""
        return f"{self.name} is moving."

class Mammal(Animal):
    """Base class for mammals."""
    def __init__(self, name, legs):
        super().__init__(name)
        self.legs = legs

class Bird(Animal):
    """Base class for birds."""
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

class Vehicle:
    """Base class for vehicles with a move action."""
    def __init__(self, model):
        self.model = model

    def move(self):
        """Generic move action for vehicles."""
        return f"The {self.model} is in motion."

# Animals
class Dog(Mammal):
    def move(self):
        return f"{self.name} is running on {self.legs} legs. 🐕"

class Fish(Animal):
    def move(self):
        return f"{self.name} is swimming. 🐠"

class Eagle(Bird):
    def move(self):
        return f"{self.name} is soaring through the sky. 🦅"

# Vehicles
class Car(Vehicle):
    def move(self):
        return f"The {self.model} is driving. 🚗"

class Plane(Vehicle):
    def move(self):
        return f"The {self.model} is flying. ✈️"

class Boat(Vehicle):
    def move(self):
        return f"The {self.model} is sailing on water. 🛥️"

# Creating instances of different classes
my_dog = Dog("Buddy", 4)
my_fish = Fish("Goldie")
my_eagle = Eagle("Sky", "2 meters")
my_car = Car("Sedan")
my_plane = Plane("Boeing 747")
my_boat = Boat("Sailboat")

# Demonstrating the move() method for each object
animals = [my_dog, my_fish, my_eagle]
vehicles = [my_car, my_plane, my_boat]

print("--- Animals Moving ---")
for animal in animals:
    print(animal.move())

print("\n--- Vehicles Moving ---")
for vehicle in vehicles:
    print(vehicle.move())

print("\n--- Polymorphism in Action (Combined) ---")
things_that_move = [my_dog, my_fish, my_eagle, my_car, my_plane, my_boat]
for thing in things_that_move:
    print(f"{thing.name if hasattr(thing, 'name') else thing.model}: {thing.move()}")