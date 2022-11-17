'''
Need of conditional statement
=============================
In a program when there is need to take decision based
on certain condition, then there is need of conditional
statement.

What is conditional statement?
==============================
The statement or instruction which helps to give decision
based on certain in a program are called as conditional
statements or conditional instructions or decision control
instruction.

Types of conditional statement
==============================
1) if statement
2) if else statement
3)nested if else
4)logical operators
5)elif

if statement
============
syntax

if condition:

    code in if block

Working:

if the condition is true then it executes if block or
program control enter in if block and execute code inside
if block.

if condition is false then it wont execute if block.

if..else
========

syntax:

if condition:

    code in if block

else:

    code in else block

Working:

if the condition is true then it executes if block or
program control enter in if block and execute code inside
if block.
If the condition is false it executes else block.
    
'''

#Two number entered by user. WAP to find greatest of two numbers.

print("Enter a number:")
#x=input()
#a=int(x)
a=int(input()) 
print("Enter a number:")
b=int(input())

if a>b:
    print("In if block")
    print("Greater is:",a)

else:
    print("In else block")
    print("Greater is:",b)















