#OOP - Wizard Game
class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name, age): # Dunder Method / Constructor Method
        if(self.membership):
            self.name = name
            self.age = age

    def run(self):
        print(f"{self.name} is Running")
        return 0


player1 = PlayerCharacter("Razal", 22)
player2 = PlayerCharacter("Rizin", 26)

player1.run()
player2.run()
print(player1.age)
print(player2.age)