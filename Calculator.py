class Calculator:
    def subtract(self,num1,num2):
        diff = num1 - num2
        print("When "+str(num1) +" is subtracted by "+ str(num2) +" the answer is "+ str(diff))

    def add(self,num1,num2):
        sum = num2 + num1
        print("The sum of "+str(num1) +" and "+ str(num2) +" is "+ str(sum))  

    def multiply(self,num1,num2):
        product = num2 * num1
        print("The product of "+str(num1) +" and "+ str(num2) +" is "+ str(product))  

    def divide(self,num1,num2):
        quotient = num2 / num1
        print("The quotient when "+str(num1) +" divides "+ str(num2) +" is "+ str(quotient))    
    
def main():
    num =  Calculator()

    print("Choose your activity")
    print("1.Addition     2.Subtraction     3.Multiplication     4.Division")
    activity = int(input("Enter activity number: "))

    if (activity == 1):
        num1 = int(input("Enter the first addend: "))
        num2 = int(input("Enter the second addend: "))
        num.add(num1,num2)
    elif (activity == 2):
        num1 = int(input("Enter the minuend: "))
        num2 = int(input("Enter the subtrahend: "))
        num.subtract(num1,num2)
    elif (activity == 3):
        num1 = int(input("Enter the multiplicand: "))
        num2 = int(input("Enter the multiplier: "))
        num.multiply(num1,num2)
    elif (activity == 4):
        num1 = int(input("Enter the divisor: "))
        num2 = int(input("Enter the dividend: "))
        num.divide(num1,num2)
    else:
        print("Please enter a valid activity number")

main()