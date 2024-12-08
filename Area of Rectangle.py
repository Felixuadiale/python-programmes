class rectangle:
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def Rectangle_area(self):
        return self.rectangle*self.width
newRectangle=rectangle(12,10)
print("Dimension of Rectangle - Length : %d Width : %d" %(newRectangle.length, newRectangle.width))
print("Area of Rectangle :", newRectangle.rectangle_area())