# Write Python code which accepts name of a product and in turn returns
# their respective prices

product={"laptop":4000,"mobile":15000,"TV":50000,"Hdd":3000,"ram":2800}
for a in product.items():
    print(a)

print("List out all the odd numbers from 1 to 100 using lists in Python.")
oddnum=[odd for odd in range(101) if odd%2==1 ]
print(oddnum)