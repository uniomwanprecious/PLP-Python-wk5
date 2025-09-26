# Part 1: Design Your Own Class - Superhero

class Superhero:
    # Constructor to initialize a Superhero object
    def __init__(self, name, secret_identity, power):
        self.name = name  # Attribute 1: Name
        self.secret_identity = secret_identity  # Attribute 2: Secret Identity
        self.power = power  # Attribute 3: Power

    # Method to perform a heroic action
    def fight_crime(self):
        print(f"{self.name} is fighting crime with their {self.power}!")

    # A getter method to reveal the secret identity
    def reveal_identity(self):
        print(f"The secret identity of {self.name} is {self.secret_identity}.")

# Part 1, Step 4: Add an inheritance layer
class FlyingHero(Superhero):
    # This class inherits from Superhero and has a new attribute
    def __init__(self, name, secret_identity, power, flight_speed):
        # Call the parent class's constructor
        super().__init__(name, secret_identity, power)
        self.flight_speed = flight_speed  # New attribute for flying heroes

    # Override the fight_crime method to be more specific
    def fight_crime(self):
        print(f"{self.name} is flying at {self.flight_speed} mph to fight crime!")

# Create objects (instances of the classes)
hero1 = Superhero("Captain Courage", "John Smith", "super strength")
hero2 = FlyingHero("Aero-Knight", "Jane Doe", "flight", 500)

# Demonstrate the methods
hero1.fight_crime()
hero1.reveal_identity()

print("-" * 20)  # Separator

hero2.fight_crime()
hero2.reveal_identity()

# Part 2: Polymorphism Challenge

class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        # This is a generic method that will be overridden
        print(f"{self.name} is moving.")

class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Boat:
    def move(self):
        print("Sailing ⛵")

# Create a list of objects from different classes
vehicles = [Car(), Plane(), Boat()]

# Iterate through the list and call the same method on each object
# The output is different for each object, demonstrating polymorphism.
print("--- Polymorphism in action ---")
for vehicle in vehicles:
    vehicle.move()
    