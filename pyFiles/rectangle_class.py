class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return (self.length * self.width)
    
class Square(Rectangle):
    def __init__(self, side_length):
        """Square inherients from Rectangle, and instead of taking two attributes, we take one and set it to both.
        """
        self.length = side_length
        self.width = side_length

square = Square(4)
print(square.area()) # 16