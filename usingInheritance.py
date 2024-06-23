# Example using inheritance

class UFC:

    def weight_class(self, weight):
        # Maps weight to weight class
        return "Lightweight"

# Fighter class inherits from UFC


class Fighter(UFC):

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)


fighter = Fighter("Khabib")
print(fighter.weight_class(155))
fighter.print_name()
