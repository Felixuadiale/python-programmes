import matplotlib.pyplot as plt

students_names=["sanjay","Rahul","Karan","Wasim","Ajay","Sartaj","Priya","Marias"]
students_marks=[35,50,20,40,50,30,90,10]

marks_perc=[]

for x in students_marks:
    res = (x/50)*100
    marks_perc.append(res)

print(marks_perc)

def marks_line_chart():
    plt.plot(students_names,students_marks)
    plt.title("Students""Percentage Graph")
    plt.xlabel("Stundents Names")
    plt.ylabel("Students Mark")
    plt.show()
marks_line_chart()


def marks_bar_chart():
    plt.bar(students_names,marks_perc)
    plt.title("Students""Percentage Graph")
    plt.xlabel("Stundents Names")
    plt.ylabel("Students Mark")
    plt.show()
marks_bar_chart()
