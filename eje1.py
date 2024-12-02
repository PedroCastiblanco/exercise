import  math as ma
class Point:
    def __init__(self,x:float,y:float):
        self.x=x
        self.y=y

    def __repr__(self):
        return str(self.__dict__)
    #def __geti

class Line:
    def __init__(self,a:Point,b:Point):
        self.p1=a
        self.p2=b

class Rectangle:
    def __init__(self,method:int):
        self.width:float
        self.height:float
        self.center:Point
        self.method=method
        self.c1:Point
        self.c2:Point

    def du(self):
        if(self.height==0):
                self.height=self.width
        if(self.width==0):
                self.width=self.height

    def compute_area(self):
        if self.method==1:
            self.du()
            return self.height*self.width
        if self.method==2:
            self.du()
            return self.height*self.width
        if self.method==3:       
            return  abs((self.c2[0]-self.c1[0])*(self.c2[1]-self.c1[1]))
        
    def compute_perimeter(self):
        if self.method==1:
            self.du()
            return 2*self.height+2*self.width
        if self.method==2:
            self.du()
            return 2*self.height+2*self.width
        if self.method==3:       
            return  2*abs(self.c2[0]-self.c1[0])+2*abs(self.c2[1]-self.c1[1])

    def __repr__(self):
        return str(self.__dict__)
    
class Square(Rectangle):
    def __init__(self, method):
        super().__init__(method)
        self.width=float(0)
        self.height=float(0)
        self.center:Point
        self.c1:Point
        self.c2:Point
        

    def convertir(self):
        if self.method==1:
            self.du()
            self.c1=(0,0)
            self.c2=(self.c1[0] +self.width ,self.c1[1] +self.height)
        if self.method==2:
            self.du()
            self.c1=(self.center[0]-(self.width/2) ,self.center[1]-(self.height/2))
            self.c2=(self.center[0]+(self.width/2) ,self.center[1]+(self.height/2))
        if self.method==3:
            if self.c1[0]>self.c2[0]:
                if self.c1[1]>self.c2[1]:
                    a,b=self.c1,self.c2
                    self.c1,self.c2=b,a
                else:
                    a1:float=self.c1[0]
                    a2:float=self.c1[1]
                    b1:float=self.c2[0]
                    b2:float=self.c2[1]
                    a:Point=(b1,a2)
                    b:Point=(a1,b2)
                    self.c1=a
                    self.c2=b
            elif self.c1[1]>self.c2[1]:
                a1:float=self.c1[0]
                a2:float=self.c1[1]
                b1:float=self.c2[0]
                b2:float=self.c2[1]
                a:Point=(a1,b2)
                b:Point=(b1,a2)
                self.c1=a
                self.c2=b
                #a=Point(self.c1[0], self.c2[1])
                #b=Point(self.c2[0], self.c1[1])
                #self.c1,self.c2=a,b

    
    def compute_interference_point(self,p:Point):
        self.convertir()
        if (self.c1[0]<=p[0]<=self.c2[0] and self.c1[1]<=p[1]<=self.c2[1]):
            return True
        else:
            return False

    def compute_interference_line(self,L:Line):
        if self.compute_interference_point(L.p1) and self.compute_interference_point(L.p2):
            return True
        else:
            return False

    def __repr__(self):
        return str(self.__dict__)

A=Square(3)
A.c1=(0,0)
A.c2=(5,5)
B=Square(2)
B.width=4
B.center=(2,3)
#B.c1=(4,0)
#B.c2=(0,4)
#a=Point(1,1)
#b=Point(5,5)
c=Line((1,1),(1,3))
#print(A.compute_interference_point((1,5)))

print(B.compute_interference_point((1,1)))
print(B.compute_interference_point((1,3)))
print(B.compute_interference_line(c))

#print(A.compute_area(),A.compute_perimeter())
print(B.compute_area(),B.compute_perimeter())
#print(C.compute_area(),C.compute_perimeter())

