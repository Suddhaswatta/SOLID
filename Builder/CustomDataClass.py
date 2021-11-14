from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError("Implement Area method")
    
class Circle(Shape) :
    
    def __init__(self,r: int):
        self.r = r
    
    def area(self)->float:
        return math.pi*self.r
    
    def __repr__(self)->str:
        return f"Circle {self.r} with hash {self.__hash__()}"
    
    def __hash__(self)->int:
        return hash(self.area())
    
    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)
        
c = Circle(4.0)    
c1= Circle(4) 
print(f'{str(c)} , {str(c1)}')
print(c==c1)
    