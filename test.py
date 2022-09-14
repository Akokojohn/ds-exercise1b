
x=4
while True:
     print(f'value of x = {x}')
     if not x > 0:
          break
     x-=1

"""
from abc import ABC, abstractmethod
class A(ABC):
     @abstractmethod
     def get(self):
          pass

class B(A):
     def set(self):
          return 'B'
          


b=B()
print(b.set())

"""