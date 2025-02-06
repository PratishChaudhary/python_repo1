class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    def vecta(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    def __add__(self,x):
        return f"{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k"
v1 = Vector(1,2,3)
print(v1.vecta())

v2 = Vector(2,-3,4)
print(v2.vecta())

print(v1+v2)