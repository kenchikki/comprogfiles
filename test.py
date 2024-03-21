import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Python window")
window.geometry("1050x400")
window.configure(bg="orange")

def keyupEmail(a):
    global at
    global dotcom

    email = custem.get()
    
    if "@" in email and "." in email and email.index("@") < email.index("."):
        at = True
    else:
        at = False
    
    if email.endswith(".com"):
        dotcom = True
    else:
        dotcom = False

    if at and dotcom:
        labelemail.config(text="Good Email")
    else:
        labelemail.config(text="Bad Email")


def keyupName(event):
    global valid_name
    
    name = event.widget.get()
    
    name_parts = name.split(", ")
    if len(name_parts) == 2:
        last_name, first_name_mi = name_parts
        
        first_name_mi_parts = first_name_mi.split(" ")
        
        if len(first_name_mi_parts) >= 1:
            first_name = first_name_mi_parts[0]
            middle_initial = " ".join(first_name_mi_parts[1:])
            
            if len(middle_initial) >= 2 and middle_initial[-1] == '.':
                valid_name = True
            else:
                valid_name = False
        else:
            valid_name = False
    else:
        valid_name = False
    
    if valid_name:
        labelname.config(text="Good Name")
    else:
        labelname.config(text="Bad Name")




label = tk.Label(window, text="Customer Registration System", width=30, height=1, bg="yellow", anchor="center")
label.config(font=('Courter',10))
label.grid(column=2,row=1)

label = tk.Label(window, text="Customer ID:", width=15, height=1,bg="yellow")
label.grid(column=1,row=2)

cid=tk.StringVar()
custid = tk.Entry(window, textvariable=cid)
custid.grid(column=2,row=2)

label = tk.Label(window, text="Customer Name:", width=15, height=1,bg="yellow")
label.grid(column=1, row=3)

labelname = tk.Label(window, text="Last name, First name, MI.", width=20, height=1,bg="yellow")
labelname.grid(column=3,row=3)

cname=tk.StringVar()
custname=tk.Entry(window, textvariable=cname)
custname.grid(column=2,row=3)
custname.bind("<KeyRelease>",keyupName)

label = tk.Label(window, text="Customer Email:", width=15, height=1,bg="yellow")
label.grid(column=1,row=6)

labelemail = tk.Label(window, text="[a-z]@[a-z.com]", width=15, height=1,bg="yellow")
labelemail.grid(column=3,row=6)

cemail=tk.StringVar()
custem= tk.Entry(window, textvariable=cemail)
custem.grid(column=2, row=6)
custem.bind("<KeyRelease>",keyupEmail)

label = tk.Label(window, text="Customer Address:", width=15, height=1,bg="yellow")
label.grid(column=1,row=7)

cad=tk.StringVar()
custad = tk.Entry(window, textvariable=cad)
custad.grid(column=2, row=7)

label = tk.Label(window, text="Customer Phone:", width=15, height=1,bg="yellow")
label.grid(column=1,row=8)

cp = tk.StringVar()
custp = tk.Entry(window, textvariable=cp)
custp.grid(column=2, row=8)

labelphone =  tk.Label(window, text="0912-1234567", width=15, height=1,bg="yellow")
labelphone.grid(column=3,row=8)

label = tk.Label(window, text="Customer Birthday:", width=15, height=1,bg="yellow")
label.grid(column=1,row=9)

cbday = tk.StringVar()
custb = tk.Entry(window, textvariable=cbday)
custb.grid(column=2, row=9)

labelbday = tk.Label(window, text="mm/dd/yyyy", width=15, height=1,bg="yellow")
labelbday.grid(column=3,row=9)

label = tk.Label(window, text="Customer Gender:", width=15, height=1,bg="yellow")
label.grid(column=1,row=10)

cgen = tk.StringVar()
custg = tk.Entry(window, textvariable=cgen)
custg.grid(column=2, row=10)

savelabel = tk.Label(window, text="Save", width=10, height=1,bg="white")
savelabel.grid(column=3,row=12)




window.mainloop()
