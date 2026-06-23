class Shape():
    def GetArea(self):
        pass

# CREATE A SUBCLASS FOR TRIANGLE
class Triangle(Shape):
    def __init__(self, base, height):
        self.__base = base
        self.__height = height
    
    def GetArea(self):
        return (self.__base * self.__height) / 2

# CREATE A SUBCLASS FOR RECTANGLE
class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def GetArea(self):
        return self.__height * self.__width

# CREATE A SUBCLASS OF RECTANGLE FOR SQUARE
class Square(Rectangle):
    def __init__(self, sideLength):
        super().__init__(sideLength, sideLength)

sq = Square(12)
print(sq.GetArea())