class Circle:
    def __init__(self , color , radius):
        self.color = color 
        self.radius = radius
    def printInfo(self):
        print("the color of the circle is : " , self.color)
        print("the radius of the circle is : " , self.radius)
    def add_radius(self , additional):
        self.radius = self.radius + additional

Circle1 = Circle("red" , 10)
Circle1.printInfo()
Circle1.add_radius(5)
Circle1.printInfo()