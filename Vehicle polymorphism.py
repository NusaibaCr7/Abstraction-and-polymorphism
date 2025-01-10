class Porsche():
    def Model(self):
        print("Porsche car model: Porsche 911 Carrera ")
        
    def topSpeed(self):
        print("Top Speed of Porsche: 293km/h")
        
    def mileage(self):
        print("Mileage of Porsche: 9 l/km")
        
class Ferrari():
    def Model(self):
        print("Ferrari car model: Ferrari F80 ")
        
    def topSpeed(self):
        print("Top Speed of Ferrari: 350km/h")
        
    def mileage(self):
        print("Mileage of Ferrari: 5.8 l/km")
        
class Mercedes():
    def Model(self):
        print("Mercedes car model: Mercedes-Benz G63 AMG ")
        
    def topSpeed(self):
        print("Top Speed of Mercedes: 220km/h")
        
    def mileage(self):
        print("Mileage of Mercedes: 6.1 l/km")
        

class Koenigsegg():
    def Model(self):
        print("Koenigsegg car model: Koenigsegg Agera RS ")
        
    def topSpeed(self):
        print("Top Speed of Koenigsegg: 447km/h")
        
    def mileage(self):
        print("Mileage of Koenigsegg: 8 l/km")


class Pagani():
    def Model(self):
        print("Pagani car model: Pagani Zonda F ")
        
    def topSpeed(self):
        print("Top Speed of Pagani: 370km/h")
        
    def mileage(self):
        print("Mileage of Pagani: 6.9 l/km")
        
o1 = Porsche()
o2 = Ferrari()
o3 = Mercedes()
o4 = Koenigsegg()
o5 = Pagani()

for car in (o1, o2, o3, o4, o5):
    car.Model()
    car.topSpeed()
    car.mileage()
    
    print()