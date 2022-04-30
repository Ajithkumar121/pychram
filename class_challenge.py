# Using the concept of object oriented programming and inheritance, create
# a super class named Computer, which has two sub classes named Desktop and Laptop.

# Define two methods in the Computer class named getspecs and
# displayspecs, to get the specifications and display the specifications of the computer.

# You can use any specifications which you want.
# The Desktop class and the Laptop class should have one specification which
# is exclusive to them for example laptop can have weight as a special specification.

# Make sure that the sub classes have their own methods to get and display
# their special specification.
# Create an object of laptop/ desktop and make sure to call all the methods
# from the computer class as well as the methods from the own class


class computer:
    def __init__(self,ram,graphics,ssd,hdd,core):
        self.ram=ram
        self.graphics=graphics
        self.ssd=ssd
        self.hdd=hdd
        self.core=core
    def getspec(self):
        print("Enter the specs of super computer")
        self.ram=input("Enter the ram: ")
        self.graphics=input("Enter graphics memory: ")
        self.ssd=input("ssd memory is: ")
        self.hdd=input("hdd memory is: ")
        self.core=input("core is: ")

    def display(self):
        print(self.ram,self.graphics,self.ssd,self.hdd,self.core)

class desktop(computer):
    def desktop_add(self):
        self.merit=input("Enter the advantages of desktop? ")
    def display1(self):
        print(self.merit)

class laptop(computer):
    def lap(self):
        self.weight=int(input("Enter the weight of laptop: "))
        self.lap_merit=input("Enter the advantages? ")

    def display2(self):
        print(self.weight,self.lap_merit)

super=laptop("","","","","")
supperlap=desktop("","","","","")
super.getspec()
super.display()
super.lap()
super.display2()
supperlap.desktop_add()
supperlap.display1()






