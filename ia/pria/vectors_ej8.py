import math

class Vector2D :
    '''Vectores 2D
        Variables:
            Number: x, y'''
    def __init__(self,x,y):
        self.x = x
        self.y = y


    def modules(self):
        return math.sqrt(2*self.x + 2*self.y)
    
    def scalar_prod(self, num=1):
        self.x = self.x*num
        self.y = self.y*num

    def __str__(self):
        return ('Vector2D: ({},{})'.format(self.x,self.y))


    @staticmethod
    def sum(vec1,vec2):
        return Vector2D((vec1.x+vec2.x) , (vec1.y+vec2.y))
    
    @staticmethod
    def subtract(vec1,vec2):
        return Vector2D((vec1.x-vec2.x) , (vec1.y-vec2.y))


class Vector3D(Vector2D):
    '''Vectores 3D
        Variables:
            Number: x, y, z'''
    def __init__(self,x,y,z):
        super().__int__(x,y)
        self.z = z

    def str(self):
        return ('Vector 3D: ({},{},{})'.format(self.x, self.y, self.z))
    
    def module(self):
        return math.sqrt(2*self.x + 2*self.y + 2*self.z)
    
    def scalar_prod(self,num=1):
        super().scalar_prod(num)
        self.z = self.z*num
    
    @staticmethod
    def dot_product(vec1, vec2):
        return Vector3D(vec1.x*vec2.x, vec1.y*vec2.y, vec1.z*vec2.z)
    
    @staticmethod
    def distance(vec1, vec2):
        return ((vec1.x-vec2.x)**2 + (vec1.y-vec2.y)**2 + (vec1.z-vec2.z)**2)
    

