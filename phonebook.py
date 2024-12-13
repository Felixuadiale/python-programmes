import sys 
def initialphone_book():
    rows,cols = int (input("Please enter intial number of contacts")),2
    phone_book=[]
    print(phone_book)
    for i in range(rows):
        print("Enter the details in following order")
        temp=[]
        for j in range(cols):
            if j==0:
                temp.append (str(input("Enter name")))
                if temp[j]==""or temp[j]==" ":
                    sys.exit("Name is mandatory , Procees exiting due to blank value")
            if j==1:
                temp.append(int(input("Enter phone number")))
        phone_book.append(temp)
    print( phone_book )
    return phone_book
def addcontext(pb):
    dip=[]
    for i in range(len(pb[0])):
        if i==0:
            dip.append(str(input("Enter name"))) 
        if i==1:
            dip.append(int(input("Enter number")))
        pb.append(dip)
    return pb
        
pb=initialphone_book()
add=input("Do you want to add a new contact(y/n)")
if add=="y":
    
    pb=addcontext(pb)
    print(pb)
