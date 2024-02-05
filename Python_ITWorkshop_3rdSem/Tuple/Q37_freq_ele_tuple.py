tup = eval(input("ENETR A TUPLE: "))

result = {}
x = list(tup)
y=[]
for i in x:
    if i not in y:
        y.append(i)
for i in y:
    result[i]=x.count(i)
print(result)


#method2

# Python program to count the frequency of all the elements in a tuple 
 
# Define the tuple 
numbers = (1, 2, 2, 3, 4, 4, 5, 6, 6, 6) 
 
# Ini�alize an empty dic�onary for the frequencies 
frequencies = {} 
 
# Iterate over the elements in the tuple 
for num in numbers: 
    # If the element is not in the dic�onary, add it with a frequency of 1 
    if num not in frequencies: 
        frequencies[num] = 1 
    # If the element is already in the dic�onary, increment its frequency 
    else: 
        frequencies[num] += 1 
 
# Print the frequencies 
print("The frequencies are:", frequencies)