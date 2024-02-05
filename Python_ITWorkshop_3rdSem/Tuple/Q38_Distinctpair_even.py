# Python program to find the distinct pairs of numbers whose product is even from a tuple of integers 
# Define the tuple 
numbers = eval(input("ENTER A TUPLE: "))
# numbers = (1, 2, 3, 4, 5, 6) 
# Initialize an empty list for the pairs 
pairs = [] 
# Iterate over the elements in the tuple 
for i in range(len(numbers)): 
    for j in range(i+1, len(numbers)): 
# If the product of the two numbers is even, add the pair to the list 
      if (numbers[i] * numbers[j]) % 2 == 0: 
        pairs.append((numbers[i], numbers[j])) 
# Print the pairs 
print("The pairs are:", pairs) 