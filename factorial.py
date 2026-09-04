num = int (input("Enter a number:"))
factorial = 1
if (num == 0 or num ==1):
    print ("The factorial is 1")
elif num <0 :
    print ("facotrial does not exist for negative number")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
        print ("The factorial of",num,"is",factorial)