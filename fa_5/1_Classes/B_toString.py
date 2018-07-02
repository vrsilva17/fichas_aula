"""
Point
"""

class Point():
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Point: {}x{}x{}".format(self.x, self.y, self.z)

if __name__ == "__main__":
    
    p1 = Point(0, 0, 0)

    print(p1)

