# Write a function which would divide two numbers, design the function in a
# manner that it handles the divide by zero exception.

# def divi(a,b):
#     return a/b
# c=int(input("Enter the value of c:"))
# d=int(input("Enter the value of d:"))
#
# try:
#     result = divi(c, d)
#     print(f"{result}")
# except :
#     print("zero division error")

def cal(a,b):
    try:
        return a/b
    except:
        print("there is a division error")
e=int(input("enter the value of e? "))
d=int(input("enter the value of d? "))
c=cal(e,d)
print(c)





