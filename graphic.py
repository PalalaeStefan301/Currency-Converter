from tkinter import Label,Button,Entry,Tk
import tkinter as tk 
from tkinter import ttk
from crawl import *

list_of_currencies = read_currencies()

def clicked():
    value = float(insert_value.get())
    curr_from = combo_box_from.get()
    curr_to = combo_box_to.get()
    #print(curr_from+" "+curr_to+"\n")
    if curr_from=="HUF" or curr_from=="JPY" or curr_from=="KRW":
        value = value/100
    for i in range(33):
        if list_of_currencies[i]==curr_from:
            t_from = read_value_of_currency(curr_from)
        if list_of_currencies[i]==curr_to:
            t_to = read_value_of_currency(curr_to)
    value = value/float(t_to)
    value = value*float(t_from)
    label_result.configure(text="Result: "+str(value.__round__(3)))

window = Tk()
window.title("GUI")
window.geometry('350x200')
label_1 = Label(window,text="Currency")
label_2 = Label(window,text="from")
label_3 = Label(window,text="to")
label_result = Label(window,text="Result: ")
insert_value = Entry(window,width=10)
combo_box_from = ttk.Combobox(window)
combo_box_to = ttk.Combobox(window)
combo_box_to['values']=list_of_currencies
combo_box_from['values']=list_of_currencies
run_button = Button(window,text="Run",command=clicked)
label_1.grid(column=0,row=0)
label_2.grid(column=0,row=1)
label_3.grid(column=0,row=2)
insert_value.grid(column=1,row=0)
combo_box_from.grid(column=1,row=1)
combo_box_to.grid(column=1,row=2)
run_button.grid(column=0,row=3)
label_result.grid(column=1,row=3)
window.mainloop()
