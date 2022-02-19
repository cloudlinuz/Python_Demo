# Checking the bmi calculation using python
# Asking for the user Height and Weight.

height = input("Please enter your Height in m : ")
weight = input("Please enter your Weight im kg : ")

# calculating the BMI
print(type(height))
print(type(weight))

height_value = float(height)
weight_value = int(weight)

print(type(height_value))
print(type(weight_value))

bmi = weight_value / height_value ** 2
bmi_value = round(bmi, 1)
print(f"Your BMI value is : {bmi_value}")
