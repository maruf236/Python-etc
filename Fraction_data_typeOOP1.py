class Fraction:
    '''
    Data: 
    Numeretor =x
    Denominator =y 
    '''

    # parameterized constructor -- Need input during creating object
    def __init__(self, x,y):
        self.num=x
        self.den=y

    def __str__(self):
        return '{}/{}'.format(self.num,self.den)    # Return format of string that readable by human.

    def __add__(self,other):
        new_num= self.num*other.den+other.num*self.den
        new_den= self.den*other.den

        return '{}/{}'.format(new_num,new_den)

    def __sub__(self,other):
            new_num= self.num*other.den-other.num*self.den
            new_den= self.den*other.den
    
            return '{}/{}'.format(new_num,new_den)

    def __mul__(self,other):
            new_num= self.num*other.num
            new_den= self.den*other.den
    
            return '{}/{}'.format(new_num,new_den)
    
    def __truediv__(self,other):
            new_num= self.num*other.den
            new_den= self.den*other.num
            return '{}/{}'.format(new_num,new_den)

    def convert_to_decimal(self):
          return self.num/self.den

fr1 = Fraction(10,20)
print(type(fr1))             # <class '__main__.Fraction'>
print(fr1)      #10/20       #<__main__.Fraction object at 0x0000017FECCE86E0>

fr2 = Fraction(3,4)
print(fr2)                   # 3/4

print(fr1 + fr2)             
print(fr1 - fr2)
print(fr1 * fr2)
print(fr1 / fr2)
print(fr1.convert_to_decimal())