with open("story.txt", "r") as file:
    data = file.read()  
    print("File Content:")
    print(data)
    
    ccount = 0
    digcnt = 0 
    spccnt = 0 
    symcnt = 0 
    
    for ch in data:
        if ch.isalpha():
            ccount = ccount + 1
        elif ch.isdigit():
            digcnt = digcnt + 1
        elif ch.isspace():
            spccnt = spccnt + 1
        else:
            symcnt = symcnt + 1

    # Print the final counts
    print("Total characters are:", ccount)
    print("Total digits used:", digcnt)
    print("Total spaces are:", spccnt)
    print("Total symbols are:", symcnt)