
import tkinter as tk
from tkinter import ttk,messagebox



class RestaurntOrderManagement:

    def __init__(self,root):
        self.root = root
        self.root.title("Restaurant")

        self.menu_items ={
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 2,
            "PIZZA MEAL": 2,
            "CHESE BURGER": 2.5
        }






        ttk.Label(frame, text="Restaurant")



        self.menu_labels ={}

        self.menu_quantities={}

        for i, (item,price) in enumerate(self.menu.items(), start=1):
            label=ttk.Label(frame, text=f"{item} ()")

            

            self.menu_labels[item] = label

            quantity_entry = ttk.Button(frame,text="Place Order",command=self.place_order)



order_button.grid(row=len(self.menu_items)+2, columnspan=3)


