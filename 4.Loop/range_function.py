'''
range(): This function generate list of numbers in a sequence.
syntax:

    range(start,stop,step)

    start=>initialization
    stop =>condition
    step =>increment/decrement (positive or negative)
'''

'''
x=list(range(1,15,1)) #start=1, stop=10 and step=1 (increment in step of 1)
print(x)
'''
'''
x=list(range(2,20,2))
print(x)
'''
'''
x=list(range(2,20)) #default step is 1
print(x)
'''
'''
#No step and start
x=list(range(20)) #default start is 0
print(x)
'''
'''
x=list(range()) #error as range() require atleast 1 argument
print(x)
'''
x=list(range(15,5,-2)) #15,15-2,13-2,11-2,9-2
print(x)


