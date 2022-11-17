'''
elif=>elseif
Greatest of three number using logical operator
'''

a=int(input("Enter first number:")) #70,70
b=int(input("Enter second number:"))#50,50
c=int(input("Enter third number:"))#20,100

if a>b and a>c: #70>50 and 70>20 => T and T => T
    print(a,"is greater")

elif b>a and b>c: #50>70 and 50>20 => F and T => F
    print(b,"is greater")

elif c>a and c>b: #20>70 and 20>50 => F and F => F
    print(c,"is greater")


'''
if a>b and a>c: #70>50 and 70>20 => T and T => T
    print(a,"is greater")

else
    if b>a and b>c: #50>70 and 50>20 => F and T => F
        print(b,"is greater")

    else
        if c>a and c>b: #20>70 and 20>50 => F and F => F
            print(c,"is greater")
'''
