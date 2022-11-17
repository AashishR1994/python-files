'''
Need of Loop:
=============
To achieve reusability or to reduce code repetition,
there is need of loop.
'''

#display string "Hello World" 5/10/100 times on the console.
'''
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
'''

'''
In above approach of writing same instruction or statement
again and again, this led to code repetition.
Code repetition has following disadvantages.
============================================

1) length of program increases due to which debugging sometimes
   become difficult.
2) Memory increases.
3) Waste of compiler or interpreter  time as same code is executed.

In order to remove or discard disadvantage caused by code repetition
there is need of loop control instruction.
'''

'''
What is Loop control instruction?
=================================
The instruction which allows us to write code once and repeat
n number times or infinite number of time are called as
loop control instructions.

Types of loop control instructions
==================================

1)while loop
2)for   loop
'''

#while loop
'''
syntax:

initialization

while condition:
    body or code to be repeated
    increment or decrement

variable used in initialization is called as counter variable.
As it is used to store number of repetition or iterarion
performed by loop.

Working of loop:
================
step1:initialization {Done only once}
step2:Check condition
step3:If condition is True then execute code or loop body.
step4:increment or decrement
step5:repeat step2 to step4 till condition is True.
step6:Once condition is False, go to step7.
step7:stop.


                                        initialization
                                               |
                                               |     False
                                ---------->condition-------> Out of loop
                              |                 |
                              |                 | True
                              |                 |
                              |          code in loop (body)
                              |                 |
                              |                 |
                              |                 |
                              incre/decre<------         
'''

#printing Hello World 10 times

i=1

while i<=10:

    print("Hello World")

    i+=1  #i=i+1

'''
i    i<=10    print("Hello World")    i+=1 => i=i+1
1    1<=10  T Hello World             i=1+1=2
2    2<=10  T Hello World             i=2+1=3
3    3<=10  T Hello World             i=3+1=4
4    4<=10  T Hello World             i=4+1=5
5    5<=10  T Hello World             i=5+1=6
6
7
8
9
10   10<=10 T Hello World             i=10+1=11
11   11<=10 F Loop Stops
'''





















