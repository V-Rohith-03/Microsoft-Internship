M=int(input("Enter the Value of M:"))
N=int(input("Enter the Value of N:"))
sum = 0
if(M>N):
    print("As M is greater than N, it returns 0")
else:
    for i in range(M,N+1):
        sum=sum+(i**3);
    print("The Sum of the Cubes of Integers from",M,"to",N,"is",sum)
