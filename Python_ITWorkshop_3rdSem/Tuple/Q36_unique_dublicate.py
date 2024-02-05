# Python program to display unique and duplicate elements of a tuple 
 
# Define the tuple 
numbers = (1, 2, 2, 3, 4, 4, 5, 6, 6, 6) 
 
# Ini�alize empty lists for unique and duplicate elements 
unique_elements = [] 
duplicate_elements = [] 
 
# Iterate over the elements in the tuple 
for num in numbers: 
    # If the element is not in the list of unique elements, add it 
    if num not in unique_elements: 
        unique_elements.append(num) 
    # If the element is already in the list of unique elements but not in the list of duplicates, add it to the list of duplicates 
    elif num not in duplicate_elements: 
        duplicate_elements.append(num) 
 
# Print the unique and duplicate elements 
print("The unique elements are:", tuple(unique_elements)) 
print("The duplicate elements are:", tuple(duplicate_elements))

#Inputing a Tuple , method2
def sort_numbers(numbers):
    un, du = [], []
    for num in numbers:
        if num not in un:
            un.append(num)
        else:
            du.append(num)
            if num in un:
                un.remove(num)
    print("Tuple with unique elements: ",tuple(un))
    print("Tuple with duplicate elements: ",tuple(du))
 
 
# print the unique tuple by extracting all the unique elements
numbers = eval(input("ENTER A TUPLE: "))
sort_numbers(numbers)