"""
Point
"""

class Point():
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

if __name__ == "__main__":
    
    p1 = Point(0, 0, 0)

print("Point 1: {}x{}x{}".format(p1.x, p1.y, p1.z))