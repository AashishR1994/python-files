'''
Nested if else
==============
When there is a need to give decision based on more than
one condition.

syntax:

if condition1: T | T | F

    if condition2: T | F

        execute if block.
    else:

        execute else block.
else:

        if condition3: T | F
            execute if block.

        else:
            execute else block.

checking:
=========
step1: first check for zero or non zero
step2: if zero display neither positive nor negative.
step3: if non-zero, then further check for positive and negative

'''

print("Enter number:")
n=int(input())

if n==0:
    print("Number is neither positive nor neagtive")
else:
    if n>0:
        print("Positive number")

    else:
        print("Negative number")

    

