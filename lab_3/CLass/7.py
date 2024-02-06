class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def coordinate(self):
        print(f"x = {self.x},y = {self.y}")
    def add(self,x1,y1):
        self.x +=x1
        self.y +=y1
    def new_coor(self,x1, y1):
        return(((self.x - x1)**2 + (self.y - y1)**2)**(1/2))


p = point(int(input("x = ")),int(input("y = ")))
p.coordinate()   
p.add(int(input('x1 = ')),int(input('y1 = ')))
print(f'distance = {p.new_coor(int(input()), int(input()))}')
        