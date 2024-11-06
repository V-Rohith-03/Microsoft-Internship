arr=[]
N=int(input("Enter the Number of Elements:"))
Switches=0;
for i in range(0,N):
    E=int(input());
    #append the array
    arr.append(E);    
for j in range(1,len(arr)):
    if(arr[j]%2!=0):
        Switches=Switches+1;
print("The Number of Switches from Green Pen to Red Pen:",Switches)


