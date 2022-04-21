class p:
    a = 10
    def m1(self):
        print("method of parent class")
class c:
    a = 20
    def m2(self):
        print("this is the method of child class")
class c1(c,p):
    pass

obj=c1()
print(obj.a)    ## according to method resolving order(MRO)