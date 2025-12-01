class Rectangle:
    
    def __init__(self, one_side, other_side) -> None:
        self.down_left = [min(one_side[0], other_side[0]), 
                          min(one_side[1], other_side[1])]
        self.up_right = [max(one_side[0], other_side[0]), 
                         max(one_side[1], other_side[1])]
    
    def get_pos(self):
        return (round(self.down_left[0], 2), round(self.up_right[1], 2))

    def get_size(self):
        return (abs(round(self.up_right[0] - self.down_left[0], 2)),
                abs(round(self.up_right[1] - self.down_left[1], 2)))
    
    def move(self, dx, dy):
        self.down_left[0] += dx
        self.up_right[0] += dx
        self.down_left[1] += dy
        self.up_right[1] += dy
        
    def resize(self, width, height):
        self.up_right[0] = self.down_left[0] + width
        self.down_left[1] = self.up_right[1] - height
        
# rect = Rectangle((3.2, -4.3), (7.52, 3.14))
# print(rect.get_pos(), rect.get_size())
# rect.move(1.32, -5)
# print(rect.get_pos(), rect.get_size())

rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.get_pos(), rect.get_size())
rect.resize(23.5, 11.3)
print(rect.get_pos(), rect.get_size())


    # def perimeter(self):
    #     a = abs(self.y2 - self.y1)
    #     b = abs(self.x2 - self.x1)
        
    #     return round((a + b) * 2, 2)
    
    # def area(self):
    #     a = abs(self.y2 - self.y1)
    #     b = abs(self.x2 - self.x1)
        
    #     return f"{a * b:.2f}"