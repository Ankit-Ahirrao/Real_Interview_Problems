# two rectable fina overlapping area




class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def overlap_rectangle(self, other):
        if not self.isOverlapped(other): return None
        x1 = max(self.x1, other.x1)
        x2 = min(self.x2, other.x2)
        y1 = max(self.y1, other.y1)
        y2 = min(self.y2, other.y2)
        return Rectangle (x1=x1, x2=x2, y1=y1, y2=y2)

rect_one = Rectangle(0, 0, 4, 4)
rect_two = Rectangle(0, 0, 4, 4)
overlap = rect_one.overlap_rectangle(rect_two)