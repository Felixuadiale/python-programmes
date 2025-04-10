
from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename


window = Tk()
window.title("Condingal's Text Editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)


def open_file():
    filepath = askopenfilename(filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    filetypes=[("Text Files", "*.txt"), ("All Files") ("*.*")]
    if not filepath:
        return txt_edit.delete(1.0,END)
    with open(filepath, "r") as input_file:
        text= input_file.read()

    txt_edit.insert(END, text)
    input_file.close()
    window.title(f"Condingal's Text Editor-{filepath}")





txt_edit = Text(window)

fr_buttons = Frame(window)
btn_open = Button(fr_buttons,text="Open", command=open_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

fr_buttons.grid(row=0,column=0,sticky="ns")
txt_edit.grid(row=0, column=1,sticky="nsew")



window.mainloop()