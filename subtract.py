a = input("Enter first binary number: ")
b = input("Enter second binary number: ")

num1 = int(a, 2)
num2 = int(b, 2)

result = num1 - num2

print("Binary Subtraction:", bin(result)[2:])
