

n=int(input("enter the no:"))

for i in range(2,n,1):
    r=n%i 
    
    if r==0:
        print(n,"is non-prime number")
        break

else:
    print("It is prime number")

'''
n=5

i   i in[2,3,4]  r=5%i   r==0   i=i+1
2   2 in[]T      r=5%2=1 1==0F  i=2+1=3
3   3 in[]T      r=5%3=2 2==0F  i=3+1=4
4   4 in[]T      r=5%4=1 1==0F  i=4+1=5
5   5 in[]F => Completed all iterations

n=7
i   i in[2,3,4,5,6]  r=7%i   r==0   i=i+1
2   2 in[]T          r=7%2=1 1==0F  i=2+1=3
3   3 in[]T          r=7%3=2 2==0F  i=3+1=4
4   4 in[]T          r=7%4=3 3==0F  i=4+1=5
5   5 in[]T          r=7%5=2 2==0F  i=5+1=6
6   6 in[]T          r=7%6=1 1==0F  i=6+1=7
7   7 in[]F     ===> Completed all iterations
'''

