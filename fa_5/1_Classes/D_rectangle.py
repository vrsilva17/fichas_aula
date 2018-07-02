"""
Example
"""

from C_point import Point

class Cubo():

    def __init__(self, point1, tamanho):
        self.point1 = point1
        self.tamanho = tamanho
         
    def __str__(self):
        return "Cubo corners:\n{}\n{}".format(self.point1, self.tamanho)

    def get_size(self):
        """
        returns the rectangle size as the distance from origin  
        """
        return Point(abs(self.point1.x + self.tamanho), abs(self.point1.y + self.tamanho), abs(self.point1.z + self.tamanho) )

if __name__ == "__main__":
    
    p1 = Point(0, 0, 0)
    tamanho = 5

    cubo = Cubo(p1, tamanho)
    
    print(cubo)

    print(cubo.get_size())

