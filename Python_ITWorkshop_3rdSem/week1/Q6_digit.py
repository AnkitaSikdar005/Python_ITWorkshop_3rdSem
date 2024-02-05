n= int((input("ENTER A NUMBER: ")))
#M-1
for i in range(4,0,-1):
    n= n%(10**i)
    print(n)

#M-2
n1=(input("ENTER A NUMBER: "))
# for i in range(len(n1),0,-1):
for i in range(len(n1)):
    print(n1[i:])