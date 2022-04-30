#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪



print("Welcome To Tip Calculator")
a=input("What Was The Total Bill Amount? $")
b= float (a)
c=input("What Was The Tip Persentage Your Are Giving?" )
d=int(c)
e=(b * d )/ 100
e +=b
f=int (input("How Many People To Split The Bill? "))
g= round(e/f,2)
print(f"Each Person Should Pay: {g}")

