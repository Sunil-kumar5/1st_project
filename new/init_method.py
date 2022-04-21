class bank:
    bname="SBI"
    bm="hulk"
    loc="basvangudi"
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal=sal
    def display(self):
        print(self.bname)
        print(self.bm)
        print(self.name)    # Objectmethod / instancemethod
        print(self.age)
        print(self.sal)

    @classmethod
    def change_bname(cls,newname):
        cls.bname=newname

    @classmethod
    def change_manager(cls,newname):
        cls.bm=newname

    @staticmethod
    def input_name():
        return input("enter the nsme:")

raja=bank("sunil",22,56767)
# raja.display()
# raja.__init__("fghj",67,4567)
# print(raja.name,raja.age,raja.sal)    #sunil 22 56767

# bank.change_bname("ICICI")
# bank.change_manager("boss")
# raja.display()

dinga = (bank.input_name(),27,22323)

