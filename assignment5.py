class Superhero:
    """Represents a generic superhero with basic attributes and abilities."""

    def __init__(self, name, secret_identity, power_level):
        """Initializes a Superhero object."""
        self.name = name
        self.secret_identity = secret_identity
        self.power_level = power_level
        self.is_flying = False  # Default state

    def reveal_identity(self):
        """Reveals the superhero's secret identity."""
        return f"The amazing {self.name} is secretly {self.secret_identity}!"

    def fly(self):
        """Makes the superhero fly."""
        self.is_flying = True
        return f"{self.name} takes to the skies!"

    def land(self):
        """Makes the superhero land."""
        self.is_flying = False
        return f"{self.name} gracefully lands."

    def use_power(self):
        """A generic action for using their power."""
        return f"{self.name} uses their incredible power!"

    def __str__(self):
        """String representation of the Superhero object."""
        flying_status = "flying" if self.is_flying else "on the ground"
        return f"{self.name} (Power Level: {self.power_level}, Currently: {flying_status})"

# Inheritance Layer: Specialized Superheroes
class FlyingSuperhero(Superhero):
    """Represents a superhero with inherent flying abilities."""

    def __init__(self, name, secret_identity, power_level, flight_speed):
        """Initializes a FlyingSuperhero object."""
        super().__init__(name, secret_identity, power_level)
        self.flight_speed = flight_speed
        self.is_flying = True  # Flying superheroes are always flying by default

    def fly(self):
        """Overrides the fly method for a more specific flying action."""
        return f"{self.name} soars through the air at a speed of {self.flight_speed}!"

    def land(self):
        """Overrides the land method, as they are inherently flyers."""
        self.is_flying = True # They remain flyers
        return f"{self.name} makes a swift aerial maneuver."

    def use_power(self):
        """A specific power usage related to flight."""
        return f"{self.name} unleashes a powerful aerial attack!"

    def __str__(self):
        return f"{super().__str__()} (Flight Speed: {self.flight_speed})"

class SuperStrengthSuperhero(Superhero):
    """Represents a superhero with super strength."""

    def __init__(self, name, secret_identity, power_level, strength_level):
        """Initializes a SuperStrengthSuperhero object."""
        super().__init__(name, secret_identity, power_level)
        self.strength_level = strength_level

    def use_power(self):
        """A specific power usage related to super strength."""
        return f"{self.name} uses their immense strength, with a force of {self.strength_level} tons!"

    def lift(self, weight):
        """Demonstrates lifting ability."""
        return f"{self.name} effortlessly lifts {weight}!"

    def __str__(self):
        return f"{super().__str__()} (Strength Level: {self.strength_level})"

# Creating Superhero objects
superman = FlyingSuperhero("Superman", "Clark Kent", 95, "Mach 2")
wonder_woman = SuperStrengthSuperhero("Wonder Woman", "Diana Prince", 92, "100+ tons")
batman = Superhero("Batman", "Bruce Wayne", 70) # Non-flying, non-super strength

# Demonstrating methods and attributes
print(superman.name)
print(superman.reveal_identity())
print(superman.fly())
print(wonder_woman.use_power())
print(batman.fly())
print(batman.land())

print("\n--- Polymorphism in Action ---")
def superhero_action(hero):
    """Demonstrates polymorphism by calling the use_power method on different superhero types."""
    print(f"{hero.name}: {hero.use_power()}")

superhero_action(superman)
superhero_action(wonder_woman)
superhero_action(batman)

print("\n--- String Representations ---")
print(superman)
print(wonder_woman)
print(batman)