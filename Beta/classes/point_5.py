class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self, x1, y1):
        self.x += x1
        self.y += y1
        
    def length(self, second):
        return round(((abs(self.x - second.x) ** 2 + abs(self.y - second.y) ** 2) ** 0.5), 2)


class PatchedPoint(Point):

    def __init__(self, *args) -> None:
        match len(args):
            case 0: 
                super().__init__(0, 0)
            case 1:
                super().__init__(*args[0])
            case 2:
                super().__init__(*args)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"
    
    def __add__(self, other):
        return PatchedPoint(self.x + other[0], self.y + other[1])
    
    def __iadd__(self, other):
        self.x += other[0]
        self.y += other[1]
        return self
    
point = PatchedPoint()
print(point)
new_point = point + (2, -3)
print(point, new_point, point is new_point)

first_point = second_point = PatchedPoint((2, -7))
first_point += (7, 3)
print(first_point, second_point, first_point is second_point)