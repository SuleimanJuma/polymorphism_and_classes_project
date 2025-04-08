
# Base class Animal
class Animal:
    def move(self):
        pass  # Empty method to be overridden by subclasses

# Subclass Dog
class Dog(Animal):
    def move(self):
        print("The dog runs.")

# Subclass Fish
class Fish(Animal):
    def move(self):
        print("The fish swims.")

# Subclass Bird
class Bird(Animal):
    def move(self):
        print("The bird flies.")

# Example usage:
dog = Dog()
fish = Fish()
bird = Bird()

dog.move()   # Output: The dog runs.
fish.move()  # Output: The fish swims.
bird.move()  # Output: The bird flies.
