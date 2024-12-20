import  math as ma

def frange2(start, stop, step):#for con float
    n_items = int(ma.ceil((stop - start) / step))
    return [redu_deci(start + i*step )  for i in range(n_items+1)]

def redu_deci(a:float): #Reducir decimales a maxima 3 cifras significativas
    return round(int(a*1000)/1000,2)


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
        self.discretized_line:list

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
        
    def discretize_line(self,com:Point=None):# list,bool
        m:float=0
        b:float=0
        if self.end[0]!=self.start[0] :
            m=(self.end[1]-self.start[1])/(self.end[0]-self.start[0])
            b=(self.end[1]-m*self.end[0])
            N=[]
            H=frange2(self.start[0],self.end[0],0.05)
            for i in H:
                a=Point( i, redu_deci(m*i + b ))
                N.append(a)
            self.discretized_line=N
        else :
            N=[]
            H=frange2(self.start[1],self.end[1],0.05)
            for i in H:
                a=Point( self.start[0],i )
                N.append(a)
            self.discretized_line=N
            
        if com==None:
            return self.discretized_line
        elif com[0]==self.start[0]  and self.end[0]==self.start[0] and com[1] in range(self.start[1],self.end[1]+1):
            return True
        elif com[1]!=m*com[0]+b and com[0] in range(self.start[0],self.end[0]+1) and self.end[0]!=self.start[0]:
            return True
        else:
            return False

    def __repr__(self) -> str:
        return str(self.__dict__)
    

class Rectangle:
    def __init__(self,method:int):
        self.width:float
        self.height:float
        self.center:Point
        self.method=method
        self.c1:Point
        self.c2:Point
        self.L1:Line
        self.L2:Line
        self.L3:Line
        self.L4:Line

    def du(self):
        if(self.height==0):
                self.height=self.width
        if(self.width==0):
                self.width=self.height

    def set_Lines(self,L1:Line,L2:Line,L3:Line,L4:Line):
        self.L1=L1
        self.L2=L2
        self.L3=L3
        self.L4=L4

    def compute_area(self):
        if self.method==1:
            self.du()
            return self.height*self.width
        if self.method==2:
            self.du()
            return self.height*self.width
        if self.method==3:       
            return  abs((self.c2[0]-self.c1[0])*(self.c2[1]-self.c1[1]))
        if self.method==4:
            A=[self.L1.compute_length(),self.L2.compute_length(),self.L3.compute_length(),self.L4.compute_length()]
            c,d=1,0 
            for i in A:
                if i!=c:
                    c=c*i
                    d+=1
                    print(d)
                    if d==2:
                        return c
            if d<2:
                c=c**2
            return c
        
    def compute_perimeter(self):
        if self.method==1:
            self.du()
            return 2*self.height+2*self.width
        if self.method==2:
            self.du()
            return 2*self.height+2*self.width
        if self.method==3:       
            return  2*abs(self.c2[0]-self.c1[0])+2*abs(self.c2[1]-self.c1[1])
        if self.method==4:
            return self.L1.compute_length()+self.L2.compute_length()+self.L3.compute_length()+self.L4.compute_length()

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

    
    def compute_interference_point(self,p:Point):
        self.convertir()
        if (self.c1[0]<=p[0]<=self.c2[0] and self.c1[1]<=p[1]<=self.c2[1]):
            return True
        else:
            return False

    def compute_interference_line(self,L:Line):
        if self.compute_interference_point(L.start) and self.compute_interference_point(L.end):
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
C=Line((1,1),(1,3))
#print(A.compute_interference_point((1,5)))

print(B.compute_interference_point((1,1)))
print(B.compute_interference_point((1,3)))
print(B.compute_interference_line(C))

#print(A.compute_area(),A.compute_perimeter())
print(B.compute_area(),B.compute_perimeter())
#print(C.compute_area(),C.compute_perimeter())

a=Line((0,0),(0,4))
b=Line((0,4),(5,4))
c=Line((5,4),(5,0))
d=Line((5,0),(0,0))
D=Square(4)
D.set_Lines(a,b,c,d)
print(D.compute_area(),D.compute_perimeter())
#print(b.compute_length())

Z=Line((0,0),(0,6))
#print(Z.compute_length())
#print(Z.compute_slope())
#print(Z.compute_horizontal_cross())
#print(Z.compute_vertical_cross())
print(Z.discretize_line((1,1)))
