class Rectangle:
    
    def __init__(self, one_side, other_side) -> None:
        self.one_side = one_side
        self.other_side = other_side
        self.x1, self.y1 = one_side
        self.x2, self.y2 = other_side
    
    def perimeter(self):
        a = abs(self.y2 - self.y1)
        b = abs(self.x2 - self.x1)
        
        return round((a + b) * 2, 2)
    
    def area(self):
        a = abs(self.y2 - self.y1)
        b = abs(self.x2 - self.x1)
        
        return f"{a * b:.2f}"
        
        
rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())

rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())
# x1, y1 = (3.2, -4.3)
# print(x1)