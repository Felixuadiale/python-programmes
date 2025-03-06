from abc import ABC , abstractmethod
class Abclass(ABC):
    def print(self,x):
        print("Passed Value:", x)

    @abstractmethod
    def task(self):
        print("We are inside Absclass task")

class test_class(Abclass):
    def task(self):
        print("We are inside test_class task")
test_obj = test_class()
test_obj.task()
test_obj.task(100)