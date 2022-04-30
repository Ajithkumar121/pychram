a,b=0,0
n=int(input("Enter a number?"))
for i in range(2,n//2):
    if n%i==0:
        c=1
        break
if b==1:
    print("the number is not prime")
else:
    print("the number is prime")