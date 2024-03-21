import tkinter as tk
import re
from tkinter import messagebox


window2 = tk.Tk()
window2.title("Python window")
window2.geometry("1050x400")
window2.configure(bg="red")

valid_quan = False
valid_digit = False
valid_date = False

def keyupQuan(a):
    global valid_quan

    dquan = prodquan.get()

    if dquan.isdigit():
        valid_quan = True
    else:
        valid_quan = False

    if valid_quan:
        labelquan.config(text="Valid Digit")
    else:
        labelquan.config(text="Invalid Digit")

def keyupProdtc(a):
    
    global valid_digit

    totalcost = prodtc.get()

    if totalcost.isdigit():
        valid_digit = True
    else:
        valid_digit = False

    if valid_digit:
        labeltc.config(text="Valid Digit")
    else:
        labeltc.config(text="Invalid Digit")

def keyupDate(a):
    global valid_date

    date = proddr.get()

    pattern = r'^(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/\d{4}$'

    if re.match(pattern, date):
        valid_date = True
    else:
        valid_date = False

    if valid_date:
        labeldr.config(text="Valid Date Format")
    else:
        labeldr.config(text="Invalid Date Format")

def save_file2():
    confirm = messagebox.askyesno("Save", "Do you want to save?")
    if confirm:
        if (
            valid_digit
            and valid_date
            and valid_quan
            and prodid.get() != ""
            and prodtype.get() != ""
            and prodesc.get() != ""
            and prodsup.get() != ""
            and proddr.get() != ""
        ):
            # Write your save logic here
            messagebox.showinfo("Success", "Data saved successfully!")
        else:
            messagebox.showwarning(
                "Invalid Data", "Some data is invalid or missing. Cannot save."
            )
    else:
        messagebox.showinfo("Cancelled", "Save operation cancelled.")


label = tk.Label(window2, text="Products System", width=30, height=1, bg="orange", anchor="center")
label.config(font=('Courter',10))
label.grid(column=2,row=1)

label = tk.Label(window2, text="Product ID:", width=15, height=1,bg="orange")
label.grid(column=1,row=2)

pid=tk.StringVar()
prodid = tk.Entry(window2, textvariable=pid)
prodid.grid(column=2,row=2)

label = tk.Label(window2, text="Product Type:", width=15, height=1,bg="orange")
label.grid(column=1, row=3)

prot = tk.StringVar()
prodtype =tk.Entry(window2, textvariable=prot)
prodtype.grid(column=2,row=3)


label = tk.Label(window2, text="Product Description:", width=15, height=1,bg="orange")
label.grid(column=1,row=6)

pdesc =tk.StringVar()
prodesc = tk.Entry(window2, textvariable=pdesc)
prodesc.grid(column=2, row=6)

label = tk.Label(window2, text="Supplier:", width=15, height=1,bg="orange")
label.grid(column=1,row=7)

sup=tk.StringVar()
prodsup = tk.Entry(window2, textvariable=sup)
prodsup.grid(column=2, row=7)

label = tk.Label(window2, text="Quantity:", width=15, height=1,bg="orange")
label.grid(column=1,row=8)

quan = tk.StringVar()
prodquan = tk.Entry(window2, textvariable=quan)
prodquan.grid(column=2, row=8)
prodquan.bind("<KeyRelease>", keyupQuan)

labelquan =  tk.Label(window2, text="must be a number", width=15, height=1,bg="orange")
labelquan.grid(column=3,row=8)

label = tk.Label(window2, text="Total Cost:", width=15, height=1,bg="orange")
label.grid(column=1,row=9)

ptc = tk.StringVar()
prodtc = tk.Entry(window2, textvariable=ptc)
prodtc.grid(column=2, row=9)
prodtc.bind("<KeyRelease>", keyupProdtc)

labeltc = tk.Label(window2, text="must be a number:", width=15, height=1,bg="orange")
labeltc.grid(column=3,row=9)

label = tk.Label(window2, text="Date Received:", width=15, height=1,bg="orange")
label.grid(column=1,row=10)

pdr = tk.StringVar()
proddr = tk.Entry(window2, textvariable=pdr)
proddr.grid(column=2, row=10)
proddr.bind("<KeyRelease>", keyupDate)

labeldr = tk.Label(window2, text="mm/dd/yyyy", width=15, height=1,bg="orange")
labeldr.grid(column=3,row=10)

save_button2 = tk.Button(window2, text="Save", command=save_file2)
save_button2.grid(column=2, row=11)



window2.mainloop()