import tkinter as tk
import re
from tkinter import messagebox


def product():
    import tkinter as tk
    import re
    from tkinter import messagebox


    window2 = tk.Tk()
    window2.title("Python window")
    window2.geometry("1050x400")
    window2.configure(bg="white")

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
            labeldr.config(text="Valid Date Format", bg="green")
        else:
            labeldr.config(text="Invalid Date Format", bg="red")

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

def customer():
    r=messagebox("Customer Form", "Form")



window = tk.Tk()
window.title("Python window")
window.geometry("1050x400")
window.configure(bg="lightgrey")


at = False
dotcom = False
valid_name = False
valid_phone = False
valid_date = False

lst = [['ID','Name','Email', 'Address', 'Phone', 'Birthday', 'Gender']]
lstindex=0

def callback(event):
    global lstindex
    li=[]
    li=event.widget._values
    lstindex=li[1]

    cid.set(lst[li[1]][0])
    cname.set(lst[li[1]][1])
    cemail.set(lst[li[1]][2])
    cad.set(lst[li[1]][3])
    cp.set(lst[li[1]][4])
    cbday.set(lst[li[1]][5])
    cgen.set(lst[li[1]][6])
    

def creategrid(n):
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            cgrid = tk.Entry(window, width=10)
            cgrid.insert(tk.END,lst[i][j])
            cgrid._values = cgrid.get(), i
            cgrid.grid(row=i+12,column=j+11)
            cgrid.bind("<Button-1>", callback)
    
    if n==1:
        for label in window.grid_slaves():
            if int(label.grid_info()["row"]) > 12:
                label.grid_forget()

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
        labelemail.config(text="Good Email", bg="green")
    else:
        labelemail.config(text="Bad Email", bg="red")

def keyupName(event):
    global valid_name
    
    name = event.widget.get()
    
    valid_name = False

    if not name:
        labelname.config(text="Enter your name")
        return
    
    name_parts = name.split(", ")
    if len(name_parts) != 2:
        labelname.config(text="Ex: Dela Cruz, Juan A.", bg="red")
        return

    last_name, first_name_mi = name_parts
    first_name_mi_parts = first_name_mi.split(" ")
    
    if len(first_name_mi_parts) < 2:
        labelname.config(text="Enter full first name and MI", bg="red")
        return

    first_name = first_name_mi_parts[0]
    middle_initial = " ".join(first_name_mi_parts[1:])
    
    if len(middle_initial) != 2 or not middle_initial[0].isalpha() or middle_initial[1] != '.':
        labelname.config(text="Enter valid middle initial", bg="red")
        return

    valid_name = True
    labelname.config(text="Good Name", bg="green")


def keyupPhoneNumber(a):
    global valid_phone

    phone_number = custp.get()

    pattern = r'^\d{4}-\d{7}$'

    if re.match(pattern, phone_number):
        valid_phone = True
    else:
        valid_phone = False

    if valid_phone:
        labelphone.config(text="Valid Phone Number", bg="green")
    else:
        labelphone.config(text="Invalid Phone Number", bg="red")

def keyupDate(a):
    global valid_date

    date_str = custb.get()

    pattern = r'^(0[1-9]|1[0-2])/(0[1-9]|1\d|2\d|3[01])/\d{4}$'

    if re.match(pattern, date_str):
        valid_date = True
    else:
        valid_date = False

    if valid_date:
        labelbday.config(text="Valid Date", bg="green")
    else:
        labelbday.config(text="Invalid Date", bg="red")

def save_file():
    global Id
    confirm = messagebox.askyesno("Save", "Do you want to save?")
    if confirm:
        
        if (
            at
            and dotcom
            and valid_name
            and valid_phone
            and valid_date
            and cad.get() != ""
            and cgen.get() != ""
        ):
            existing_ids = []
            for record in lst:
                try:
                    existing_ids.append(int(record[0]))
                except ValueError:
                    pass 
        
            max_existing_id = max(existing_ids) if existing_ids else 0

            deleted_ids = set(range(1, max_existing_id + 1)) - set(existing_ids)

            new_id = min(deleted_ids) if deleted_ids else max_existing_id + 1

            lst.append([new_id, cname.get(), cemail.get(), cad.get(), cp.get(), cbday.get(), cgen.get()])
            messagebox.showinfo("Save Message", "File saved successfully!")

            Id = new_id + 1
            creategrid(0)
        else:
            messagebox.showwarning(
                "Invalid Data", "Some data is invalid or missing. Cannot save."
            )
    else:
        messagebox.showinfo("Cancelled", "Save operation cancelled.")

def delete():
    r = messagebox.askquestion("Delete Record?", "Do you want to delete record?")

    if r:
        del lst[lstindex]
        creategrid(1)
        creategrid(0)

def update():
    global lst
    r = messagebox.askyesno("Information Updated", "Information Updated")
    Id = lst[lstindex][0]
    if r:
        lst[lstindex] = [Id, cname.get(), cemail.get(), cad.get(), cp.get(), cbday.get(), cgen.get()]
        creategrid(1)
        creategrid(0)

label = tk.Label(window, text="Customer Registration System", width=30, height=1, bg="grey", anchor="center")
label.config(font=('Courter',10))
label.grid(column=2,row=1)

label = tk.Label(window, text="Customer ID:", width=15, height=1,bg="grey")
label.grid(column=1,row=2)

cid=tk.StringVar()
custid = tk.Entry(window, state="disabled")
custid.grid(column=2,row=2)

label = tk.Label(window, text="Customer Name:", width=15, height=1,bg="grey")
label.grid(column=1, row=3)

labelname = tk.Label(window, text="Last name, First name, MI.", width=20, height=1,bg="grey")
labelname.grid(column=3,row=3)

cname=tk.StringVar()
custname=tk.Entry(window, textvariable=cname)
custname.grid(column=2,row=3)
custname.bind("<KeyRelease>",keyupName)

label = tk.Label(window, text="Customer Email:", width=15, height=1,bg="grey")
label.grid(column=1,row=6)

labelemail = tk.Label(window, text="[a-z]@[a-z.com]", width=15, height=1,bg="grey")
labelemail.grid(column=3,row=6)

cemail=tk.StringVar()
custem= tk.Entry(window, textvariable=cemail)
custem.grid(column=2, row=6)
custem.bind("<KeyRelease>",keyupEmail)

label = tk.Label(window, text="Customer Address:", width=15, height=1,bg="grey")
label.grid(column=1,row=7)

cad=tk.StringVar()
custad = tk.Entry(window, textvariable=cad)
custad.grid(column=2, row=7)

label = tk.Label(window, text="Customer Phone:", width=15, height=1,bg="grey")
label.grid(column=1,row=8)

cp = tk.StringVar()
custp = tk.Entry(window, textvariable=cp)
custp.grid(column=2, row=8)
custp.bind("<KeyRelease>",keyupPhoneNumber)

labelphone =  tk.Label(window, text="0912-1234567", width=20, height=1,bg="grey")
labelphone.grid(column=3,row=8)

label = tk.Label(window, text="Customer Birthday:", width=15, height=1,bg="grey")
label.grid(column=1,row=9)

cbday = tk.StringVar()
custb = tk.Entry(window, textvariable=cbday)
custb.grid(column=2, row=9)
custb.bind("<KeyRelease>",keyupDate)

labelbday = tk.Label(window, text="mm/dd/yyyy", width=15, height=1,bg="grey")
labelbday.grid(column=3,row=9)

label = tk.Label(window, text="Customer Gender:", width=15, height=1,bg="grey")
label.grid(column=1,row=10)

cgen = tk.StringVar()
custg = tk.Entry(window, textvariable=cgen)
custg.grid(column=2, row=10)

save_button = tk.Button(window, text="Save", command=save_file)
save_button.grid(column=1, row=11)

delete_button = tk.Button(window, text="Delete", command=delete)
delete_button.grid(column=2, row=11)

update_button = tk.Button(window, text="Update", command=update)
update_button.grid(column=3, row=11)

menubar= tk.Menu(window)
filemenu= tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label="Products", command=product)
filemenu.add_command(label="Customers", command=customer)
filemenu.add_separator()
filemenu.add_command(label="Close", command=window.quit)
window.config(menu=menubar)

creategrid(0)

window.mainloop()
