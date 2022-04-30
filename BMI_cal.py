# Create a BMI calculator, BMI which stands for Body Mass Index can be
# calculated using the formula:
# BMI = (weight in Kg)/(Height in Meters)^2.
# Write python code which can accept the weight and height of a person and
# calculate his BMI.
# note: Make sure to use a function which accepts the height and weight
# values and returns the BMI value.

def bmi(W,H):
  return W/H**2
weight=int(input("What is your Weight in Kg? "))
height=float(input("what is your Height in M? "))
bmi_calc=bmi(weight,height)
print(bmi_calc)