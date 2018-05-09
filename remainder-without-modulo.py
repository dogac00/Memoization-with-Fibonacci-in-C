num1 = int(input())
num2 = int(input())

print(num1 - (num1 // num2) * num2) # exploit the integer division
