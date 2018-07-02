"""
Example
"""

from C_point import Point

class Rectangle():

    def __init__(self, point1):
        self.point1 = point1
         
    def get_size(self):
        """
        returns the rectangle size as the distance from origin  
        """
        return Point(abs(self.point1.x), abs(self.point1.y), abs(self.point1.z) )

    def __str__(self):
        return "Rectangle corners:\n{}".format(self.point1)

if __name__ == "__main__":
    
    p1 = Point(0, 0, 0)


    rectangle = Rectangle(p1)
    
    print(rectangle)

    print(rectangle.get_size())
