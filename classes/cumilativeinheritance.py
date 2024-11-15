class Animal():
    def __init__(self,species):
        print(f"{species} is a type of class Animal")
        
class Mammal(Animal):
    def __init__(self,species):
        print(f"{species} is a type of class Mammal (warm blooded)")
        super().__init__(species)
        
class Nonwingedmammal(Mammal):
    def __init__(self,species):
        print(f"{species} is a type of class Nonwingedmammal (cant fly)") # lol get rekt L+ratio 
        super().__init__(species)
    def move(self):
        print("I am a non winged mammal and i cant fly")
        
class Nonmarinemammal(Mammal):
    def __init__(self,species):
        print(f"{species} is a type of class Nonmarinemammal (cant swim)") # lol get rekt L+ratio
        super().__init__(species)
    def move(self):
        print("I am a non marine mammal and i cant swim")
            
# Example of multiple inheritance

class Dog(Nonmarinemammal,Nonwingedmammal): # yoooooo
    def __init__(self,breed):
        print(f"my breed: with 4 legs: {breed}")
        super().__init__(breed)
    
    

cow=Nonwingedmammal("cow")
dog=Dog("Zinc retriever")
dog.move()