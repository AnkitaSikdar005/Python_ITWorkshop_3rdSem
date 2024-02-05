# values = input("Input some comma seprated numbers : ")
# list = values.split(",")
# tuple = tuple(list)
# print('Tuple : ',tuple)


# Prompt the user for input 
numbers = input("Please enter a sequence of comma-separated numbers: ") 
# Split the string into a list of strings using comma as the separator 
numbers_list = numbers.split(',') 
# Convert the list of strings to a list of integers 
numbers_list = [int(num) for num in numbers_list] 
# Convert the list to a tuple 
numbers_tuple = tuple(numbers_list) 
# Print the tuple 
print("The tuple is:", numbers_tuple)


