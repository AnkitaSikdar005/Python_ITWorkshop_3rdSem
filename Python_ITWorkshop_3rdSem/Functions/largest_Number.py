def max_of_three():
 

 num1 = float(input("Enter first number: "))
 num2 = float(input("Enter second number: "))
 num3 = float(input("Enter third number: "))

 # Use a concise conditional expression to find the maximum
 maximum = max(num1, num2, num3)

 return maximum

# Get the largest number from the function
largest_number = max_of_three()

# Print the result
print("The largest number is:", largest_number)
