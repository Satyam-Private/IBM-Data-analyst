class Circle:
    def __init__(self , color , radius):
        self.color = color 
        self.radius = radius
    def printInfo(self):
        print("the color of the circle is : " , self.color)
        print("the radius of the circle is : " , self.radius)

Circle1 = Circle("red" , 10)
Circle1.printInfo()