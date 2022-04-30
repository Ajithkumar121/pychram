class hospital:
    def __init__(self,adminname,doctorname,sistername,dep):
        self.adminname=input("Enter admin name?\n ")
        self.doctorname=input("Enter doctor name?\n ")
        self.sistername=input("Enter sister name?\n ")
        self.dep=input("Which department?\n ")

class patientward:
    def getdet(self):
        self.name=input("Enter patient name? \n")
        self.age=int(input("Enter your age?\n"))

    def putdet(self):
        print(self.name,self.age)

class department(hospital,patientward):
    def display(self):
        print(self.adminname,self.doctorname,self.sistername,self.dep)


det=department("","","","")
det.display()
det.getdet()
det.putdet()
