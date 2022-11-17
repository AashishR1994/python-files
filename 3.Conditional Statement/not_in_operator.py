'''
user enter number between 1 and 10. If user entered number
as 8,9 then program must print invalid number otherwise it
must print valid number
'''

n=int(input("Enter a number:"))
'''
if n in (1,2,3,4,5,6,7,10):
      print("Number is valid")

else:
    print("Number is not valid")    
'''

if n not in(8,9):
    print("Number is valid")

else:
    print("Number is invalid")
