'''
code editor -----print()----> console(output screen)

if there is a need to bring user input from output screen or
console to the code editor or to store in a variable, we need
input() funtion.

syntax:

    variable=input()

step1: Give message to user => print()
step2: store that input into variable => var=input()
'''

'''
print("Enter first number:")
x=input()
##print("Value of x is:",x)
print("Enter second number")
y=input()
z=x+y
print("Addition of",x,"and",y,"is:",z)


In above code values are not getting added, they are joined
or concatenated.
Input given by user in python is always stored as
string by default.

If there is need to convert string to number following
functions.
int():   This function is used to convert string to integer.
float(): This function is used to convert string to float.
'''

print("Enter first number:")
x=input() #string
#print(type(x))
#a=int(x)
a=float(x)
#print(type(a))
print("Enter second number")
y=input()
b=int(y)

z=a+b # z=10+20=30
print("Addition of",a,"and",b,"is:",z)

