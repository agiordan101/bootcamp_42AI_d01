class GotCharacter:
    def __init__(self, first_name=None, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    def __str__(self):
        return "A class representing the Stark family.\
        Or when bad things happen to good people."

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print("House words : {}".format(self.house_words), end="")

    def die(self):
        self.is_alive = False


class Lannister(GotCharacter):
    def __str__(self):
        return "A class representing the Lannister family."

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "Les Lannister on est beau et tro for"

    def print_house_words(self):
        print("House words : {}".format(self.house_words), end="")

    def die(self):
        self.is_alive = False


arya = Stark("Arya")
joffrey = Lannister("Joffrey")

print(str(arya))

arya.print_house_words()
print()
print(arya.is_alive)
arya.die()
print(arya.is_alive)
