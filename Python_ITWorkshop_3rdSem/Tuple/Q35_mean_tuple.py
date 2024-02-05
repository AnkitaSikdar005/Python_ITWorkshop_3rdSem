# Python program to calculate the mean of elements in a tuple of integers 
# Define the tuple 
numbers = (1, 2, 3, 4, 5) 
# Calculate the sum of the numbers 
sum_of_numbers = 0 
for num in numbers: 
  sum_of_numbers += num 
 
# Calculate the mean 
mean = sum_of_numbers / len(numbers) 
 
# Print the mean 
print("The mean is:", mean)