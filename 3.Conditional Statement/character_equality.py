'''
A character is entered by user, write a program to check
whether that character is equal to a or b or c.
'''

ch=input("Enter a character:") #b,q,A

if ch=='a' or ch=='b' or ch=='c': #b==a or b==b or b==c => F or T or F
    print("Character found!!!")

else:
    print("Character not found")


#q==a or q==b or q==c => F or F or F => F
#A==a or A==b or A==c => F or F or F => F
