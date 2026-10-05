'''
Write OOP classes to handle the following scenarios:

A user can create and view 2D coordinates
A user can find out the distance between 2 coordinates
A user can find the distance of a coordinate from origin
A user can check if a point lies on a given line
A user can find the distance between a given 2D point and a given line
'''

class point:

    def __init__(self,x,y):
        self.x_cod= x
        self.y_cod= y

    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)

    def euclidian_distance(self,other):
        return ((self.x_cod-other.x_cod)**2+(self.y_cod-other.y_cod)**2)**0.5

    def distance_from_origin(self):
        return self.euclidian_distance(point(0,0))
        # return (self.x_cod**2+ self.y_cod**2)**0.5

class line :

    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c =c

    def __str__(self):
        return '{}x+{}y+c=0'.format(self.a,self.b,self.c)

    def point_On_Line(line,point):
        if line.a*point.x_cod+line.b*point.y_cod+line.c==0:
            return "Lies on the line."
        else:
            return "Does not lie on the line."

    def shortest_distant(line,point):
        return abs(line.a*point.x_cod+line.b*point.y_cod+line.c)/((line.a)**2+((line.b)**2))**0.5


    

p1 = point(2,2)
#<x,y>   implemneted using  __init__  and  __str__
print(p1)
# ditance between two point  -- used p1.euclidian_distance(p2)
x2=int (input("Enter x coordiante "))
y2= int (input("Enter y coordinate "))
p2 = point (x2,y2)
print (p2)
print(p1.euclidian_distance(p2))
print(p2.distance_from_origin())

l1=line (2,3,-5)
p1=point (2,2)
print(l1.point_On_Line(p1))
print(l1.shortest_distant(p1))

