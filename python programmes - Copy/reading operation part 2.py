with open("C:/Users/HP/Downloads/python programmes/myfile0.txt","w")as file1:
    file1.write("Good day and how are you\n i hope you are fine\n Thank you")
file1.close()
with open("C:/Users/HP/Downloads/python programmes/myfile0.txt","r")as file1:
    data=file1.readlines()
    print("Words in the file are ")
    for line in data:
        word=line.split(" ")
        print(word)
file1.close()