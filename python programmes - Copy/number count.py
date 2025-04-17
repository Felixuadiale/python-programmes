from tkinter import *
from tkinter import messagebox


root= Tk()


root.geometry("650x400")

def topwin():
    top= Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg="light blue")
    top.geometry("600x350+50+50")

    label =Label(top,text="Enter total amount")
    entry =Entry(top)
    lbl =Label(top,text="Here are number of notes for each denomination")

    l1=Label(top,text="2000")
    l2=Label(top,text="500")
    l3=Label(top,text="100")

    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)
    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note2000= amount // 2000
            amount %=2000

            note500= amount // 500
            amount %=500

            note100= amount // 500
            amount %=500

            t1.delete(0,END)
            t2.delete(0,END)
            t3 .delete(0,END)

            t1.insert(END,str(note2000))
            t2.insert(END,str(note500))
            t3.insert(END,str(note100))
        except ValueError:
         messagebox.showerror("Error","Please enter a valid number.")

    btn = Button(top,text="Claculate",command=calculator)

    label.place(x=230,y=50)
    entry.place(x=200,y=80)
    btn.place(x=240,y=120)
    lbl.place(x=140,y=170)

    l1.place(x=180,y=200)
    l2.place(x=180,y=230)
    l2.place(x=180,y=260)

    t1.place(x=270,y=200)
    t2.place(x=270,y=230)
    t3.place(x=270,y=260)

    top.mainloop()
button1=Button(root,text="Let's get started!", command=topwin)
button1.place(x=260,y=100)
root.mainloop()