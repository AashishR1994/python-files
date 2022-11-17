'''
A three digit number is entered by user. Write a program
to find whether number is armstrong number.

n=153

sum of cube of digits = original number

1**3+5**3+3**3 = 1+125+27 = 153

step1:start
step2:digit separation => %,// 10
step3:cube and add or summation.
step4:check summation is equal to number entered by user.
step5:if it found same then it is armstrong number
step6:otherwise it is not an armstrong number.
step7:stop.
'''

print("Enter three digit number:")
n=int(input()) #n=153
#digit separation
a=n%10 #a=153%10 = 3
b=n//10 #b=153//3 = 15
c=b%10 #c=15%10 = 5
d=b//10 #d=15//10 = 1

s=a**3+c**3+d**3 #cube and summation
#checking

if s==n:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number") 
