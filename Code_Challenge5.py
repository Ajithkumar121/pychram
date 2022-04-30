# 1. Write Python code to open a file named demo.txt and write some
# random data into it.
# 2. Open the file, read the contents and display them as output.
# 3. Write python code to add additional text to the existing file on a new line
# without deleting the previous contents.



# file=open("demo.txt",'w')
# file.close()

file=open("demo.txt","a")
file.write("thank you")
file.close()


file=open("demo.txt",'r')
a=file.read()
print(a)
file.close()






