
n = int(input("Enter a value for n: "))
# Initialize an empty dictionary 
dictionary = {} 
# Iterate over the numbers from 1 to n (both included) 
for i in range(1, n+1): 
# Add the pair (i, i*i) to the dictionary 
    dictionary[i] = i*i 
# Print the dictionary 
print("The dictionary is:", dictionary) 