class Shape:
    def __init__(self):
        pass

    def area(self):
        print("Area of the shape: 0")

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        square_area = self.length ** 2
        print(f"Area of the square: {square_area}")


if __name__ == "__main__":
    n = int(input("n:"))
    square = Square(n)
    
    square.area()


    shape = Shape()
    shape.area()