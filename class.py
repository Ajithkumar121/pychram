class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def getdetails(self):
        self.name=input("enter your name")
        self.mark=int (input ("enter your mark"))
    def putd(self):
        print (self.name,self.mark)

class techer(Student):
    def display (self):
        print("am derived class1")

class parent(techer):
    def newfun(self):
        print("am derived class2")
class admin(parent):
        def funadmin(self):
            print("im admin")
obj=admin("","")
obj.getdetails()
obj.putd()
obj.display()
obj.newfun()
obj.funadmin()