import  math as ma
class Point:
    def __init__(self,x:float,y:float):
        self.x=x
        self.y=y

    def __repr__(self):
        return str(self.__dict__)
    
class Line():
    def __init__(self, start:Point, end:Point):
        self.start=start
        self.end=end
        self.length:float
        self.slope:float

    def compute_length(self):
        self.length=ma.sqrt((self.end[0]-self.start[0])**2+(self.end[1]-self.start[1])**2)
        return self.length
    
    def compute_slope(self):
        self.slope=ma.degrees(ma.atan((self.end[1]-self.start[1])/(self.end[0]-self.start[0])))
        return self.slope

    def compute_horizontal_cross(self):
        if (self.start[1]<=0<=self.end[1] or self.start[1]>=0>=self.end[1]):
            return True
        else:
            return False
        
    def compute_vertical_cross(self):
        if (self.start[0]<=0<=self.end[0] or self.start[0]>=0>=self.end[0]):
            return True
        else:
            return False
        
    def __repr__(self) -> str:
        return str(self.__dict__)
    
    

A=Line((-1,1),(2,4))
print(A.compute_length())
print(A.compute_slope())
print(A.compute_horizontal_cross())
print(A.compute_vertical_cross())
        