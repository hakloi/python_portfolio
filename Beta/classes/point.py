class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self, x1, y1):
        self.x += x1
        self.y += y1
        
    def length(self, second):
        return round(((abs(self.x - second.x)** 2 + abs(self.y - second.y)** 2 ) ** 0.5), 2)
    
    
point = Point(3, 5)
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)

first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))