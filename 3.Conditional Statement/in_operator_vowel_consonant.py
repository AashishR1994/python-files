'''
Write a program to check whether character entered
by user is vowel pr consonent.

vowels=> a,e,i,o,u,A,E,I,O,U
consonant=> Other than vowels are consonants.

in and not in are called as membership operators.
'''

ch=input("Enter character:") #i,T

if ch in('a','e','i','o','u','A','E','I','O','U'):
    print("It is vowel")

else:
    print("It is consonant")
