# result=[]
# for i in "ajithkumar":
#     result.append(i)
# print(result)
#
# a=[s for s in 'inmakes']
# print(a)

result=["python","program","code","random","rock","people"]
new=[]
for c in result:
    if "p" in c:
        new.append(c)
print(new)

newone=[i for i in result if "o" in i]
print(newone)