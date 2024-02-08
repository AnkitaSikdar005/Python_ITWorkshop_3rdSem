'''The zip() function in Python is used to combine two or more iterable objects into a single iterable,
     where corresponding elements from the input iterable are paired together as tuples.
     list1 = [1, 2, 3]
     list2 = [4, 5, 6]

zipped_list = zip(list1, list2)

for item in zipped_list:
    print(item)
 (1, 4)
(2, 5)
(3, 6)'''

name =eval(input("ENTER A LIST OF EMPLOYEE NAMES: "))
salary= eval(input("ENTER A LIST OF SALARIES: "))
if len(name)== len(salary):
    x= dict(zip(name,salary))
    print(x)
else: 
    print("ENTER EQUAL NUMBER OF EMPLOYEE NAMES AND SALARY!!")
    
