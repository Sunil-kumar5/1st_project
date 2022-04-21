# from abc import ABC,abstractmethod
# class b(ABC):
#     a = 10
#     def m1(self):
#         print("hello how are u")
# obj = b()
# obj.m1()

###

from abc import ABC,abstractmethod
class b(ABC):
    a = 10
    @abstractmethod
    def m1(self):
        print("hello how are u")
class c(b):
    def m1(self):
        return super().m1
obj=c()
obj.m1()