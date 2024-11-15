# glasses
class Person:
    name=""
    age=-1
    favcol=""
    
    def discribeme(self):
        print(f"""my name: {self.name}
my age: {self.age}
my favorate color: {self.favcol} """)
    def __init__(self,name="",age=-1,favcol=""):
        self.name=name
        self.age=age
        self.favcol=favcol
        
rushi=Person()
rushi.name="rushi"
rushi.age=30
rushi.favcol="red"

print(rushi.age)
rushi.discribeme()
amulya=Person("amulya",36,"yellow")
amulya.discribeme()

me=Person(favcol="blue")
me.discribeme()
venom=Person("Venom","???","Black")
venom.discribeme()

class Indoafrican(Person):
    language=""
    def __init__(self,name="",age=-1,favcol="",language=""):
        self.language=language
        super().__init__(name,age,favcol)
        
    def discribeme(self):
        super().discribeme()
        print(f"my language: {self.language}")
        
zimbabwe=Indoafrican("Venom",34,"pink","venomease")
zimbabwe.discribeme()
class Devil(Person):
    def discribeme(self):
        super().discribeme()
        print(f"my realm: Hell")
        
josh=Devil("Josh","20556 Eon","Blood Red")
josh.discribeme()

    
    
    
    
    
    