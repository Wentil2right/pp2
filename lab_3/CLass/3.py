class Shape:
    def __init__(self):
        pass

    def area(self):
        print("Area of the shape: 0")

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        rectangle_area = self.length * self.width
        print(f"Area of the rectangle: {rectangle_area}")

if __name__ == "__main__":
    a = int(input("a:"))
    b = int(input("b:"))
    rectangle = Rectangle(a,b)

    rectangle.area()

    shape = Shape()

    shape.area()