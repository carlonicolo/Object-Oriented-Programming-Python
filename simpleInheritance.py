# Create a simple Competitor class
class Competitor:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    # Method Prints competitors stats
    def print_stats(self):
        print(f"{self.name} is {self.age} years old and weighs {self.weight} pounds.")

# Create a Fighter class that inherits from Competitor


class Fighter(Competitor):
    pass


fighter = Fighter("Conor McGregor", 32, 170)
fighter.print_stats()
