import crud as c1
while True:
    print("\n1.Add Product\n2.Display Product\n3.Search Product\n4.Sort Product\n5.Update Product\n6.Delete Product")
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        c1.add()
    elif choice==2:
        c1.display()
    elif choice==3:
        c1.search()
    elif choice==4:
        c1.sort()
    elif choice==5:
        c1.update()
    elif choice==6:
        c1.delete()
    else:
        print("Invalide Choice!")
        break