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
    
    # Class Method can be used without instanciating an object
    @classmethod
    def adding_things(cls, num1, num2):
        return cls("Tedddy", num1 + num2)
    
    # doesnt involve the class
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter("Razal", 22)
player2 = PlayerCharacter("Rizin", 26)

# player1.run()
# player2.run()
# print(player1.age)
# print(player2.age)

print(player1.adding_things(3, 5))
print(PlayerCharacter.adding_things(3, 5))