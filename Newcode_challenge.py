# Assume you want to build two functions for discounting products on a
# website.
# Function number 1 is for student discount which discounts the current price
# to 10%.
# Function number 2 is for additional discount for regular buyers which
# discounts an additional 5% on the current student discounted price.
# Depending on the situation, we want to be able to apply both the discounts
# on the products.

def discount(product):
    return a-(product*10/100)
a=(int(input("Enter the price of the product? \n")))
b=round(discount(a))


buyer=input("if you are a regular buyer enter 'yes'\n").lower()
if buyer=="yes":
    def add_discount(newprice):
        return b-(newprice*5/100)

    print(f"Your final discount is {add_discount(b)}")
else:
    print(b)