#using for loop
num = int(input("Enter a number"))
c=0
print("Factors are:\n")
for i in range(1,num+1):
  if(num%i==0):
     c=c+1
     print(i,end=" ")
#    break
   
if(c==2):
  print("\nPrime number")
else:
  print("Not prime number")  

  #Using while loop
num2 = int(input("ENTER THE NUMBER: "))
fact = 0
i =1
print("FACTORS ARE= \n", end=" ")
while i<= num2:
    if num2 %i ==0:
        print(i,"\n",end=" ")
        fact +=1
    i +=1
if fact ==2:
    print("\nIT IS A PRIME NUMBER!!")
else:
    print("\nIT IS NOT A PRIME NUMBER")