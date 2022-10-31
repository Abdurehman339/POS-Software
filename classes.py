class Rectangle:
    def __init__(myRectangle,length,width):
        myRectangle.length = length
        myRectangle.width = width
    
    def Perimeter(myRectangle):
        myRectangle.perimeter = 2*(myRectangle.length + myRectangle.width)
    
    def Area(myRectangle):
        myRectangle.area = (myRectangle.length*myRectangle.width)
    
    def Display(myRectangle):
        print("length of the rectangle are: " + str(myRectangle.length))
        print("width of the rectangle are: " + str(myRectangle.width))
        print("Peremiters of the rectangle are: " + str(myRectangle.perimeter))
        print("Area of the rectangle are: " + str(myRectangle.area)) 

Rectangle1 = Rectangle(6,6)
Rectangle1.Perimeter()
Rectangle1.Area()
Rectangle1.Display()