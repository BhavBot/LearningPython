class Celsius:
    def __init__(self, temp  = 0,city = "defaultcity"):
        self.temp = temp
        self.city = city
        
    def to_fahr(self):
            return (self.temp * 1.8) + 32
    @property
    def temp(self):
        print("this is getter")
        return self._temp
    @temp.setter
    def temp(self,value):
        print("this is setter")
        if value<(-273.15):
            raise ValueError("no absolute zero lower wrong")
        else:
            self._temp=value
        
deg = Celsius(300,"Bangolare")

# print("Fahr:", deg.to_fahr())
# print("access directly:", deg.temp)

# for k, v in deg.__dict__.items():
#     print(f"{k}={v}")

deg.temp = 23
newdeg = deg.temp


