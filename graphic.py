from tkinter import Label,Button,Entry,Tk,Image
from tkinter import *
from tkinter import ttk
from crawl import *
from PIL import ImageTk, Image

list_of_currencies = read_currencies()
def clicked():
    value = float(insert_value.get())
    curr_from = combo_box_from.get()
    curr_to = combo_box_to.get()
    if curr_to=="HUF" or curr_to=="JPY" or curr_to=="KRW":
        value = value*100
    if curr_from=="HUF" or curr_from=="JPY" or curr_from=="KRW":
        value = value/100
    for i in range(33):
        if list_of_currencies[i]==curr_from:
            t_from = read_value_of_currency(curr_from)
        if list_of_currencies[i]==curr_to:
            t_to = read_value_of_currency(curr_to)
    value = value/float(t_to)
    value = value*float(t_from)
    label_result.configure(text=str(value.__round__(3)))

root = Tk()
root.geometry("600x400")

C = Canvas(root, bg="white", height=250, width=300)
filename = PhotoImage(file = "background_money.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = Frame(root, bg='blue')
frame.pack_propagate(0)
frame.pack(fill='both', expand='True', padx=100, pady=100)

label_1 = Label(frame,text="Currency Converter")
label_1.config(bg='blue', fg='white')
label_1.place(x=0, y=0)
label_2 = Label(frame,text="amount")
label_2.config(bg='blue', fg='white')
label_2.place(x=70, y=30)
label_3 = Label(frame,text="from")
label_3.config(bg='blue', fg='white')
label_3.place(x=150, y=30)
label_4 = Label(frame,text="to")
label_4.config(bg='blue', fg='white')
label_4.place(x=250, y=30)

label_result = Label(frame,text="",bg='blue')
label_result.pack(fill='both', side='bottom', expand='True')
label_result.config(font=("Colibri", 40))
label_result.place(x=120, y=100)
insert_value = Entry(frame,width=10)
insert_value.place(x=70, y=50)

combo_box_from = ttk.Combobox(frame, width=10)
combo_box_from.place(x=150,y=50)
combo_box_to = ttk.Combobox(frame,width=10)
combo_box_to.place(x=250,y=50)
combo_box_to['values']=list_of_currencies
combo_box_from['values']=list_of_currencies
run_button = Button(frame,text=">",command=clicked, bg='#2F328D')
run_button.bind("<Return>")
run_button.place(x=350,y=48)

root.mainloop()