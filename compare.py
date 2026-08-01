# 3 tah sonkayar modde boro sonkaya nirnoyer program leko

num1 = (input("Enter 1st number"))
num2 = (input("Enter 2nd number"))
num3 = (input("Enter 3rd number"))

if num1>=num2 and num1>=num3:
    largest = num1
elif num2>=num1 and num2>num3:
    largest = num2
else:
    largest = num3
print(f"The largest number is:{largest}")