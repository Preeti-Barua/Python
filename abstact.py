from abc import *
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class snake(Animal):
    def move(self):
        print("crawl")
class dog(Animal):
    def move(self):
        print("run &walk")
a=snake()
a.move()
b=dog()
b.move()
        
        
