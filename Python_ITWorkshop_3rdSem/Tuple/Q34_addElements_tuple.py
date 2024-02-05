# Python program to add elements in a tuple without using built-in functions 
# Define the original tuple 

original_tuple = (1, 2, 3) 
# Define the element to be added 
element_to_add = 4 
# Create a new tuple by concatenating the original tuple and a tuple containing the new element 
new_tuple = original_tuple + (element_to_add,) 
# Print the new tuple 
print("The new tuple is:", new_tuple)


#adding elements of tuple
def summation(test_tup):
    test = list(test_tup)
    count = 0
 
    for i in test:
        count += i
    return count
 
 

test_tup = eval(input("ENTER A TUPLE: "))
print(summation(test_tup))

