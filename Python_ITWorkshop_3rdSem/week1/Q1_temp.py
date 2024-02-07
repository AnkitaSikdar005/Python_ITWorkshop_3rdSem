#method1
def temp_con(temp):
    return (9*temp/5)+32

cel= float(input("ENTER A TEMPERATURE IN CELCIUS: "))
print("TEMPERATURE IN FARENHEIT IS: ",temp_con(cel))


#method2
cel1= float(input("ENTER A TEMPERATURE IN CELCIUS: "))
f=int((9*cel1/5 + 32))
print("TEMPERATURE IN FARENHEIT IS: ",f)
