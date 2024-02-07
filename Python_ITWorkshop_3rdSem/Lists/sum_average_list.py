# Get the list of numbers from the user
list1 = input("Enter a list of numbers separated by commas: ").split(",")

# Convert the strings in the list to numbers
numbers = [float(num) for num in list1]

# Calculate the sum and average
sum_of_numbers = sum(numbers)
average = sum_of_numbers / len(numbers)

# Print the results
print("Sum:", sum_of_numbers)
print("Average:", average)

