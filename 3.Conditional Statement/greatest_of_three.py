'''
Greatest of the three number entered by user.
'''

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

if a>b:

    if a>c:

        print(a,"is greater")

    else:
        print(c,"is greater")

else:
    if b>c:
        print(b,"is greater")

    else:
        print(c,"is greater")
