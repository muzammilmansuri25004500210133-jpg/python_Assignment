n=int(input("Enter number :"))
cnt=0
for i in range(1,n+1):
    if(n%i==0):
        cnt+=1
    if(cnt>2):
        break
print(cnt)
if(cnt==2):
    print(n,"is prime no")
else:
    print(n,"is not prime no")