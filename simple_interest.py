print("simple interest calculator")
def simple_interest(a,b,c):
    return a*b*c/100
p=int(input("enter the value of p? "))
n=int(input("enter the value of N? "))
r=int(input("enter the value of R? "))
interest=simple_interest(p,n,r)
print(interest)
