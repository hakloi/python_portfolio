# class Rectangle:
#     def __init__(self, corner1, corner2) -> None:
#         self.left_down = [min(corner1[0], corner2[0]),
#                           min(corner1[1], corner2[1])]
#         self.up_right = [max(corner1[0], corner2[0]),
#                          max(corner1[1], corner2[1])]
        
#     def turn(self):
#         self.up_right[0], self.up_right[1] = self.up_right[1], self.up_right[0]
#         self.left_down[0], self.left_down[1] = self.left_down[1], self.left_down[0] 
        
#     def scale(self, factor):
#         self.up_right[0] = round(self.up_right[0] * factor, 2) 
#         self.up_right[1] = round(self.up_right[1] * factor, 2) 
#         self.left_down[0] = round(self.left_down[0] * factor, 2)
#         self.left_down[1] = round(self.left_down[1] * factor, 2)
        
#     def perimeter(self):
#         return round((self.up_right[0] - self.left_down[0]) * 2 +
#                      (self.up_right[1] - self.left_down[1]) * 2, 2)

#     def area(self):
#         return round((self.up_right[0] - self.left_down[0]) *
#                      (self.up_right[1] - self.left_down[1]), 2)

#     def get_pos(self):
#         return round(self.left_down[0], 2), round(self.up_right[1], 2)

#     def get_size(self):
#         return round(self.up_right[0] - self.left_down[0], 2), \
#             round(self.up_right[1] - self.left_down[1], 2)

#     def move(self, dx, dy):
#         self.left_down[0] += dx
#         self.left_down[1] += dy
#         self.up_right[0] += dx
#         self.up_right[1] += dy

#     def resize(self, width, height):
#         self.up_right[0] = self.left_down[0] + width
#         self.left_down[1] = self.up_right[1] - height

class Rectangle:

    def __init__(self, corner_1: tuple, corner_2: tuple):
        self.corner_1 = corner_1
        self.corner_2 = corner_2
        self.left_x = min(self.corner_1[0], self.corner_2[0])
        self.left_y = max(self.corner_1[1], self.corner_2[1])
        self.width = abs(self.corner_2[0] - self.corner_1[0])
        self.length = abs(self.corner_2[1] - self.corner_1[1])
        self.x_center = round(self.left_x + self.width / 2.0, 2)
        self.y_center = round(self.left_y - self.length / 2.0, 2)

    def get_size(self):
        return (round(self.width, 2), round(self.length, 2))

    def move(self, dx, dy):
        self.left_x += dx
        self.left_y += dy

    def get_pos(self):
        return (round(self.left_x, 2), round(self.left_y, 2))

    def resize(self, width, height):
        self.width = width
        self.length = height

    def perimeter(self):
        return round((self.width + self.length) * 2, 2)

    def area(self):
        return round(self.width * self.length, 2)

    def turn(self):
        width = self.length
        length = self.width
        self.left_x = self.x_center - width / 2.0
        self.left_y = self.y_center + length / 2.0
        self.length = length
        self.width = width

    def scale(self, factor):
        self.width = round(self.width * factor, 2)
        self.length = round(self.length * factor, 2)
        self.left_x = self.x_center - self.width / 2.0
        self.left_y = self.y_center + self.length / 2.0

# rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
# print(rect.get_pos(), rect.get_size(), sep='\n')
# rect.turn()
# print(rect.get_pos(), rect.get_size(), sep='\n')
rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.scale(2.0)
print(rect.get_pos(), rect.get_size(), sep='\n')