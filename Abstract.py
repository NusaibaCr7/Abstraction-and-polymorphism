from abc import ABC, abstractmethod

class hiddenClass(ABC):
    
    def print(self,x):
        print("Passed value: ",x)
        
    @abstractmethod
    def task(self):
        print("We are inside Abstract task")
        
class testClass(hiddenClass):
    
    def task(self):
        print("We are inside test_class task")
        
obj1 = testClass()
obj1.task()
obj1.print(100)

hidden = hiddenClass()
hidden.task()