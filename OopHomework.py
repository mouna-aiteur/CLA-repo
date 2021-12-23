# 1-Writting the rectangular class
class Rectangle:
    def __init__(self,width,lenght):
        self.width = width
        self.lenght = lenght
    # fuction that compute the area of the ractangle
    def area(self):
        area = self.width*self.lenght
        return area
# asking for the width and lenght of the rectangle
w = float(input("enter the width of the rectangle : "))
l = float(input("enter the lenght of the rectangle : "))
rectangleArea =  Rectangle(w,l)
print("the area is : ",rectangleArea.area())
#2-the vehicle class
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
#3- Vehicule class without any attributes or methods
class Vehicle:
    pass

#4- child class Bus
class Bus(Vehicle):
    pass
