n=int(input("Enetr row number :"))
m=int(input("Enter column number :"))
a=[]
for i in range(n):
    row=[]
    for j in range(m):
        x=int(input("Enter number :"))
        row.append(x)
    a.append(x)
print(row)
print(a)