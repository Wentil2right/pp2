class ex1:
    def __init__(self):
        self.string = ''
    def get(self):
        self.string = input("string:")
    def upper(self):
        print(self.string.upper())
        
result = ex1()
result.get()
result.upper()
