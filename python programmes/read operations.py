f1=open("C:/Users/HP/Downloads/python programmes/myfile0.txt")
print(f1.read(12))
f1.close()
f1=open("C:/Users/HP/Downloads/python programmes/myfile0.txt","a")
f1.write("  and thank you")
f1.close()
f2=open("C:/Users\HP\Downloads\python programmes\newfile.txt","w")
f2.write("This is just created")
f2.close()
f2=open("C:/Users/HP/Downloads/python programmes/newfile.txt","r")
print(f2.readline())
f2.close()