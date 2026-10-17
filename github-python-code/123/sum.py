n=int(input("Enter number :"))
x=int(input("Enter number :"))
sun=0
flag=1
fact=1
for i in range(1,n+1):
    fact=1
    for k in range(1,i+1):
            fact=fact*k
            sum=sum+((x**i)*flag)
            flag=flag*-1
            print(sum)
            print(fact)
    print(sum)