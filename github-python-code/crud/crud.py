l1=[]
#id=int(input("Enter The Product-ID:"))
#name=(input("Enter The Product-NME:"))
#price=int(input("Enter The Product-PRICE:"))

# Add Product :-
def add():
    id=int(input("Enter The Product-ID:"))
    name=(input("Enter The Product-NME:"))
    price=int(input("Enter The Product-PRICE:"))
    d1={
        "Pid":id,
        "Pname":name,
        "Pprice":price
    }
    l1.append(d1)
print("Product Added Successfully...")

# Display Product :-
def display():
    print("===========================================")
    print("PRODUCT ID   PRODUCT NAME   PRODUCT PRICE")
    print("===========================================")

    for d1 in l1:
        print(d1["Pid"],"         ",d1["Pname"],"           ",d1["Pprice"])
    print("===========================================")


# search by Product-ID :-
def search():
    flag=0
    sr=int(input("Enter The Product-ID For Searching:-"))
    for d1 in l1:
        if (d1["Pid"]==sr):
            print("===========================================")
            print("PRODUCT ID   PRODUCT NAME   PRODUCT PRICE")
            print("===========================================")
            print(d1["Pid"],"         ",d1["Pname"],"           ",d1["Pprice"])
            print("-------------------------------------------")
            flag=1
        if flag==0:
            print("Product Not Found...")
        else:
            print("Product Is Found.")
    print()

# search by Product-NAME :-
'''def search():
    flag=0
    nm=(input("Enter The Product-NAME For Searching:-"))
    for d1 in l1:
        if (d1["Pname"]==nm):
            print(d1["Pid"], d1["Pname"], d1["Pprice"])
            flag=1
        if flag==0:
            print("Product Not Found...")
        else:
            print("Product Is Found.")
    print()'''

# Sort Product By Pprice (product proice):- 

def sort():
    so = sorted(l1, key=lambda x: x["Pprice"])
    print("Products Sorted By Price:")
    for d1 in so:
        print("===========================================")
        print("PRODUCT ID   PRODUCT NAME   PRODUCT PRICE")
        print("===========================================")
        print(d1["Pid"],"         ",d1["Pname"],"           ",d1["Pprice"])
        print("-------------------------------------------")

# Sort Product By Pname (product name):- 

# Update Product By Pid (product id):-

def update():
    flag = 0
    sr = int(input("Enter The Product-ID For Updating:-"))
    for d1 in l1:
        if (d1["Pid"] == sr):
            print("Current Details -> ID:", d1["Pid"], "Name:", d1["Pname"], "Price:", d1["Pprice"])
            d1["Pid"] = int(input("Enter New Product-ID:"))
            d1["Pname"] = input("Enter New Product-NAME:")
            d1["Pprice"] = int(input("Enter New Product-PRICE:"))
            print("Product Updated Successfully...")
            flag = 1
            break
    if flag == 0:
        print("Product Not Found For Updating...")
    print()

# Delete Product By Pid (product id):-

def delete():
    flag = 0
    sr = int(input("Enter The Product-ID For Deleting:-"))
    for d1 in l1:
        if (d1["Pid"] == sr):
            l1.remove(d1)
            print("Product Deleted Successfully...")
            flag = 1
            break
    if flag == 0:
        print("Product Not Found For Deleting...")
    print()

