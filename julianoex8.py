import tkinter as tk
from tkinter import messagebox
import re
import time
import csv
import random
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Canvas
from io import BytesIO
import os
import subprocess
import random
from PyPDF2 import PdfReader, PdfWriter

lst = [['ID', 'Name', 'Address', 'Phone', 'Email', 'Bday', 'Gender']]
prods = [['Prod ID', 'Type', 'Description', 'Supplier', 'Quantity', 'Total Cost', 'Received']]
orders = [['CID', 'PID', 'Ptype', 'Pdesc', 'Quantity', 'Price', 'DateOrdered', 'Total']]
lstindex=0
prod_deleted_ids = set()
orderindex = 0
prodindex = 0
window2 = None
pid2 = None
ptype2 = None
pdesc2 = None
last_customer_id = 0
deleted_ids = set()
last_product_id = 0 
supp2 = None
quant2 = None
tcost2 = None
dreceived2 = None


def print_to_pdf():
    global lstindex, orders

    if lstindex is None or len(orders) == 0:
        messagebox.showerror("Error", "Please select a customer with orders.")
        return

    selected_customer_orders = [order for order in orders if order[0] == str(lst[lstindex][0])]

    if len(selected_customer_orders) == 0:
        messagebox.showerror("Error", "No orders found for the selected customer.")
        return

    if not os.path.exists("C:\\docs"):
        os.makedirs("C:\\docs")

    invoice_number = random.randint(1000, 9999)

    buffer = BytesIO()
    doc = SimpleDocTemplate("C:\\docs\\sales_invoice.pdf", pagesize=letter)
    styles = getSampleStyleSheet()

    # Store Information
    store_name = "Kenchikki's Tech Emporium Inc."
    store_address = "#7, East Block, Davao Global Township, Davao City."
    store_contact = "0942-035-6709"
    store_email = "shop@kenchikkitech.com"

    # Store Information Paragraph
    store_info_text = f"<b>{store_name}</b><br/>{store_address}<br/>Contact: {store_contact}<br/>Email: {store_email}<br/><br/>"
    store_info = Paragraph(store_info_text, styles["Normal"])

    # Invoice Title
    title_text = "SALES INVOICE"
    title = Paragraph(title_text, styles["title"])

    # Customer Information
    customer_name = lst[lstindex][1]
    customer_address = lst[lstindex][2]
    customer_phone = lst[lstindex][3]

    # Customer Information Paragraph
    customer_info_text = f"Sold To <br/>Customer Name: {customer_name}<br/>Customer Address: {customer_address}<br/>Customer Phone: {customer_phone}<br/><br/>"
    customer_info = Paragraph(customer_info_text, styles["Normal"])

    # Order Summary Title
    order_summary_title = "ORDER SUMMARY"
    order_summary_title = Paragraph(order_summary_title, styles["Heading2"])

    # Order Summary Table
    table_data = [["Product Type", "Description", "Quantity", "Unit Price", "Total"]]
    for order in selected_customer_orders:
        product_type = order[2]
        description = order[3]
        quantity = int(order[4])
        price = float(order[5])
        total = quantity * price
        table_data.append([product_type, description, quantity, f"PHP {price:.2f}", f"PHP {total:.2f}"])

    # Define table style
    table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black)]

    # Create the table
    order_summary_table = Table(table_data)
    order_summary_table.setStyle(TableStyle(table_style))

    # Sub-total
    sub_total = sum(float(order[5]) * int(order[4]) for order in selected_customer_orders)
    sub_total_text = f"Sub-total: PHP {sub_total:.2f}"
    sub_total_para = Paragraph(sub_total_text, styles["Normal"])

    # VAT
    vat_rate = 0.12
    total_vat = sub_total * vat_rate
    vat_text = f"VAT (12%): PHP {total_vat:.2f}"
    vat_para = Paragraph(vat_text, styles["Normal"])

    # Total
    total = sub_total + total_vat
    total_text = f"<b>Total: PHP {total:.2f}</b>"
    total_para = Paragraph(total_text, styles["Normal"])

    # Footer
    footer_text = "Our products are backed by a 30-day return policy and a comprehensive 2-year warranty for your peace of mind. For any inquiries or assistance, please keep this invoice contact us at 0942-035-6709."
    footer = Paragraph(footer_text, styles["Normal"])

    elements = [store_info, Spacer(1, 20), title, Spacer(1, 20), customer_info, Spacer(1, 20),
                order_summary_title, order_summary_table, Spacer(1, 20),
                sub_total_para, vat_para, total_para, Spacer(1, 20), footer]

    doc.build(elements)

    # Add the invoice number to the PDF
    packet = BytesIO()
    can = Canvas(packet, pagesize=letter)
    invoice_number_text = f"Invoice Number: {invoice_number}"
    can.drawString(450, 800, invoice_number_text)
    can.save()

    # Move to the beginning of the StringIO buffer
    packet.seek(0)

    new_pdf = PdfReader(packet)
    existing_pdf = PdfReader(open("C:\\docs\\sales_invoice.pdf", "rb"))
    output = PdfWriter()

    # Add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.pages[0]
    page.merge_page(new_pdf.pages[0])
    output.add_page(page)

    # Finally, write "output" to a real file
    outputStream = open("C:\\docs\\sales_invoice.pdf", "wb")
    output.write(outputStream)
    outputStream.close()

    # Open the PDF file
    subprocess.Popen(['start', 'C:\\docs\\sales_invoice.pdf'], shell=True)



def products():
    global prodindex
    prodindex = 0
    global prod_deleted_ids
    global prods
    prod_deleted_ids = set()
    global window2
    global pid2,ptype2,pdesc2,supp2,quant2,tcost2,dreceived2
    
    def products2():
        pass

    def customers2():
        pass

    def validate_product_inputs():
        return (prod_validate_field(quantity2.get(), r'^\d+$') and
                prod_validate_field(totalcost2.get(), r'^\d+(\.\d+)?$') and
                prod_validate_field(datereceived2.get(), r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$'))

    def prod_validate_field(value, pattern):
        if re.match(pattern, value):
            return True
        else:
            return False

    def get_next_product_id():
        global last_product_id
        global prod_deleted_ids
        try:
            if isinstance(last_product_id, str):
                last_product_id = int(last_product_id)
        except ValueError:
            pass  

        if prod_deleted_ids:
            next_id = min(prod_deleted_ids)
            prod_deleted_ids.remove(next_id)
        else:
            next_id = last_product_id + 1

        if not validate_product_inputs():
            return None
    
        last_product_id = max(last_product_id, next_id)
        return next_id

    def save_product():
        global last_product_id
        global prod_deleted_ids
    

        if not validate_product_inputs():
            messagebox.showerror("Error", "Please fill all fields correctly.")
            return
    
        prod_next_id = get_next_product_id()
        if prod_next_id is None:
            messagebox.showerror("Error", "Error occurred while saving. Please try again.")
            return
    
        new_product = [prod_next_id, prodtype2.get(), proddesc2.get(), supplier2.get(), quantity2.get(), totalcost2.get(), datereceived2.get()]

        confirmation = prod_msgbox("Save record?", "Record")
        if confirmation:
            prods.append(new_product)
        
        file_path = "C:\\docs\\products.csv"
        with open(file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(new_product)
        
        create_product_grid(1)
        create_product_grid(0)

    def load_product_data():
        try:
                with open("C:\\docs\\products.csv", newline='') as csvfile:
                        reader = csv.reader(csvfile)
                        for row in reader:
                                prods.append(row)
        except FileNotFoundError:
                pass

    def delete_product():
        global prod_deleted_ids
        r = prod_msgbox("Delete record?", "Record")
        if r == True:
                product_id = int(prodid2.get())
                prod_deleted_ids.add(product_id)
                del(prods[prodindex])
                

                file_path = "C:\\docs\\products.csv"
                with open(file_path, 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        
                        for product in prods[1:]: 
                                writer.writerow(product)
               
                create_product_grid(1)
                create_product_grid(0)

                if len(prods) > 0 and prods[-1][0] in prod_deleted_ids:
                        prod_deleted_ids.remove(prods[-1][0])

    def update_product():
        r = prod_msgbox("Update?", "record")
        if r == True:
                if not validate_product_inputs():
                        messagebox.showerror("Error", "Please fill all fields correctly.")
                        return
        
 
                prods[prodindex] = [prodid2.get(), prodtype2.get(), proddesc2.get(), supplier2.get(), quantity2.get(), totalcost2.get(), datereceived2.get()]

                file_path = "C:\\docs\\products.csv"           
                with open(file_path, 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        
                        for product in prods[1:]: 
                                writer.writerow(product)
                
                create_product_grid(1)
                create_product_grid(0)

    def prod_msgbox(msg, titlebar):
        result = messagebox.askokcancel(title=titlebar, message=msg)
        return result

    def keyupquantity_product(event):
        try:
            quantity_value = float(quantity2.get())
            labelquantity.config(text="Valid Quantity")
        except ValueError:
            labelquantity.config(text="Must be a number")

    def keyuptotalcost_product(event):
        try:
            totalcost_value = float(totalcost2.get())
            labelcost.config(text="Valid Total Cost")
        except ValueError:
            labelcost.config(text="Must be a number")

    def keyupdatereceived_product(event):
        datereceived_format = re.compile(r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$')
        date_received = datereceived2.get()
    
        if datereceived_format.match(date_received):
            labelreceived.config(text="Good Format")
        else:
            labelreceived.config(text="Bad Format")


    window2 = tk.Tk()
    window2.title("Products Window")
    window2.geometry("1050x400")
    window2.configure(bg="grey")

    menubar = tk.Menu(window2)
    filemenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Products", command=products2)
    filemenu.add_command(label="Customers", command=customers2)
    filemenu.add_separator()
    filemenu.add_command(label="Close", command=window2.quit)
    window2.config(menu=menubar)
    load_product_data()

    label = tk.Label(window2, text="Product Registration System", width=30, height=1, bg="lightgrey", anchor="center")
    label.config(font=("Courier", 10))
    label.grid(column=2, row=1)

    label = tk.Label(window2, text="Product ID (SKU):", width=15, height=1, bg="lightgrey")
    label.grid(column=1, row=2)

    pid2= tk.StringVar(window2)
    prodid2= tk.Entry(window2, textvariable=pid2, state="disabled")
    prodid2.grid(column=2, row=2)

    label = tk.Label(window2, text="Product Type:", width=15, height=1, bg="lightgrey")
    label.grid(column=1, row=4)

    ptype2 = tk.StringVar(window2)
    prodtype2 = tk.Entry(window2, textvariable=ptype2)
    prodtype2.grid(column=2, row=4)

    label = tk.Label(window2, text="Description:", width=15, height=1, bg="lightgrey")
    label.grid(column=1, row=5)

    pdesc2 = tk.StringVar(window2)
    proddesc2 = tk.Entry(window2, textvariable=pdesc2)
    proddesc2.grid(column=2, row=5)

    label = tk.Label(window2, text="Supplier:", width=15, height=1, bg="lightgrey")
    label.grid(column=1, row=6)

    supp2 = tk.StringVar(window2)
    supplier2 = tk.Entry(window2, textvariable=supp2)
    supplier2.grid(column=2, row=6)

    label = tk.Label(window2, text="Quantity:", width=15, height=1, bg="lightgrey")
    label.grid(column=1, row=7)

    quant2 = tk.StringVar(window2)
    quantity2 = tk.Entry(window2, textvariable=quant2)
    quantity2.grid(column=2, row=7)
    quantity2.bind("<KeyRelease>", keyupquantity_product)

    labelquantity = tk.Label(window2, text="in cases", width=15, height=1, bg="lightgrey")
    labelquantity.grid(column=3, row=7)

    label = tk.Label(window2, text="Total Cost:", width=15, height=1, bg="lightgrey")
    label.grid(column=1, row=8)

    tcost2 = tk.StringVar(window2)
    totalcost2 = tk.Entry(window2, textvariable=tcost2)
    totalcost2.grid(column=2, row=8)
    totalcost2.bind("<KeyRelease>", keyuptotalcost_product)

    labelcost = tk.Label(window2, text="in pesos", width=15, height=1, bg="lightgrey")
    labelcost.grid(column=3, row=8)

    label = tk.Label(window2, text="Date Received:", width=15, height=1, bg="lightgrey")
    label.grid(column=1, row=9)

    dreceived2 = tk.StringVar(window2)
    datereceived2 = tk.Entry(window2, textvariable=dreceived2)
    datereceived2.grid(column=2, row=9)
    datereceived2.bind("<KeyRelease>", keyupdatereceived_product)

    labelreceived = tk.Label(window2, text="MM/DD/YYYY", width=15, height=1, bg="lightgrey")
    labelreceived.grid(column=3, row=9)


    savebtn_product = tk.Button(window2, text="Save", command=save_product)
    savebtn_product.grid(column=1, row=10)

    delbtn_product = tk.Button(window2, text="Delete", command=delete_product)
    delbtn_product.grid(column=2, row=10)

    updbtn_product = tk.Button(window2, text="Update", command=update_product)
    updbtn_product.grid(column=3, row=10)
    
    create_product_grid(0)

    window2.mainloop()

def callback2(event):
    global prodindex
    prodli=[]
    prodli=event.widget._values
    prodindex=prodli[1]
    pid2.set(prods[prodli[1]][0])
    ptype2.set(prods[prodli[1]][1])
    pdesc2.set(prods[prodli[1]][2])
    supp2.set(prods[prodli[1]][3])
    quant2.set(prods[prodli[1]][4])
    tcost2.set(prods[prodli[1]][5])
    dreceived2.set(prods[prodli[1]][6])


def create_product_grid(n):
    if n == 0:
        for a in range(len(prods)):
            for b in range(len(prods[0])):
                mgrid = tk.Entry(window2, width=10)
                mgrid.insert(tk.END, prods[a][b])
                mgrid._values = mgrid.get(), a
                mgrid.grid(row=a + 13, column=b + 13) 
                mgrid.bind("<Button-1>", callback2)

    if n == 1:
        for label in window2.grid_slaves():
            if int(label.grid_info()["row"]) > 13:
                label.grid_forget()

def customers():

    r = msgbox("Customer form", "Form")
    decrease_quantity = products()


def validate_inputs():
    return (validate_field(custemail.get(), r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$') and 
            validate_field(custname.get(), r'^[A-Za-z]+,\s[A-Za-z]+\s[A-Za-z]\.$') and
            validate_field(custphone.get(), r'^\d{4}-\d{7}$') and
            validate_field(custbday.get(), r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$'))

def validate_field(value, pattern):
    if re.match(pattern, value):
        return True
    else:
        return False

def get_next_customer_id():
    global last_customer_id
    global deleted_ids
    try:
        if isinstance(last_customer_id, str):
            last_customer_id = int(last_customer_id)
    except ValueError:
        pass  

    if deleted_ids:
        next_id = min(deleted_ids)
        deleted_ids.remove(next_id)
    else:
        next_id = last_customer_id + 1

    if not validate_inputs():
        return None
    
    last_customer_id = max(last_customer_id, next_id)
    return next_id

def save():
    global last_customer_id
    r = msgbox("Save record?", "Customer Record")
    if r == True:
        if not validate_inputs():
            messagebox.showerror("Error", "Please fill all fields correctly.")
            return
        
        next_id = get_next_customer_id()
        if next_id is None:
            messagebox.showerror("Error", "Error occurred while saving. Please try again.")
            return

        customer_data = [next_id, custname.get(), custaddress.get(), custphone.get(), custemail.get(), custbday.get(), custgender.get()]
        lst.append(customer_data)
        creategrid(1)
        creategrid(0)

        file_path = "C:\\docs\\customer.csv"
        with open(file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(customer_data)

def delete():
    global deleted_ids
    r = msgbox("Delete record?", "Record")
    if r == True:
        customer_id = int(cid.get())

        del(lst[lstindex])
        creategrid(1)
        creategrid(0)

        file_path = "C:\\docs\\customer.csv"
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            

            for customer in lst[1:]:
                writer.writerow(customer)

        deleted_ids.add(customer_id)
        if len(lst) > 1 and lst[-1][0] in deleted_ids:
            deleted_ids.remove(lst[-1][0])

def update():
    global lstindex
    r = msgbox("Update?", "record")
    if r == True:
        if not validate_inputs():
            messagebox.showerror("Error", "Please fill all fields correctly.")
            return

        lst[lstindex] = [custid.get(), custname.get(), custaddress.get(), custphone.get(), custemail.get(), custbday.get(), custgender.get()]
        creategrid(1)
        creategrid(0)

        file_path = "C:\\docs\\customer.csv"
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            for customer in lst[1:]:
                writer.writerow(customer)

def msgbox(msg, titlebar):
    result = messagebox.askokcancel(title=titlebar, message=msg)
    return result

def keyupemail(a):
    global at
    global dotcom
    email = custemail.get()
    if "@" in email and "." in email and email.index("@") < email.index("."):
        at = True
    else:
        at = False
    if email.endswith(".com"):
        dotcom = True
    else:
        dotcom = False

    if at and dotcom:
        labelemail.config(text="Good email")
    else:
        labelemail.config(text="Bad email")

def keyupphone(a):
    phone = custphone.get()
    if re.match(r'^\d{4}-\d{7}$', phone):
        labelphone.config(text="Good number")
    else:
        labelphone.config(text="Bad number")

def keyupname(a):
    name_format = re.compile(r'^[A-Za-z]+,\s[A-Za-z]+\s[A-Za-z]\.$')
    customer_name = custname.get()

    if name_format.match(customer_name):
        labelname.config(text="Good Format")
    else:
        labelname.config(text="Bad Format")

def keyupbday(a):
    bday_format = re.compile(r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$')
    customer_bday = custbday.get()

    if bday_format.match(customer_bday):
        labelbday.config(text="Good Format")
    else:
        labelbday.config(text="Bad Format")


def callback(event):
    global lstindex
    li=[]
    li=event.widget._values
    lstindex=li[1]
    cid.set(lst[li[1]][0])
    cname.set(lst[li[1]][1])
    caddress.set(lst[li[1]][2])
    cphone.set(lst[li[1]][3])
    cemail.set(lst[li[1]][4])
    cbday.set(lst[li[1]][5])
    cgender.set(lst[li[1]][6])

    ordersgrid(1) 
    ordersgrid(0)

def load_customer_data():
    try:
        with open("C:\\docs\\customer.csv", newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                lst.append(row)
    except FileNotFoundError:
        pass

def creategrid(n):
    for x in range(len(lst)):
            for y in range(len(lst[0])):
                    mgrid = tk.Entry(window, width=10)
                    mgrid.insert(tk.END,lst[x][y])
                    mgrid._values = mgrid.get(), x
                    mgrid.grid(row=x+11, column=y+11)
                    mgrid.bind("<Button-1>", callback)

    if n==1:
            for label in window.grid_slaves():
                    if int(label.grid_info()["row"]) > 10:
                            label.grid_forget()



    label = tk.Label(window, text="CID", height=1, bg="lightgrey", anchor="center")
    label.config(font=("Courier", 10))
    label.grid(column=11, row=len(lst)+11)

    label = tk.Label(window, text="PID", height=1, bg="lightgrey", anchor="center")
    label.config(font=("Courier", 10))
    label.grid(column=12, row=len(lst)+11)

    label = tk.Label(window, text="PType", height=1, bg="lightgrey", anchor="center")
    label.config(font=("Courier", 10))
    label.grid(column=13, row=len(lst)+11)

    label = tk.Label(window, text="PDesc", height=1, bg="lightgrey", anchor="center")
    label.config(font=("Courier", 10))
    label.grid(column=14, row=len(lst)+11)

    label = tk.Label(window, text="Quant", height=1, bg="lightgrey", anchor="center")
    label.config(font=("Courier", 10))
    label.grid(column=15, row=len(lst)+11)

    label = tk.Label(window, text="Price", height=1, bg="lightgrey", anchor="center")
    label.config(font=("Courier", 10))
    label.grid(column=16, row=len(lst)+11)

    label = tk.Label(window, text="Date", height=1, bg="lightgrey", anchor="center")
    label.config(font=("Courier", 10))
    label.grid(column=17, row=len(lst)+11)

    label = tk.Label(window, text="Total", height=1, bg="lightgrey", anchor="center")
    label.config(font=("Courier", 10))
    label.grid(column=18, row=len(lst)+11)


    
    orderbtn = tk.Button(text="Add Order", command=addorder)
    orderbtn.grid(column=2, row=len(lst)+11)
    delbtn = tk.Button(text="Delete Order", command=deleteorder)
    delbtn.grid(column=3, row=len(lst)+11)

    ordersgrid(1)
    ordersgrid(0)


def addorder():
    global lstindex
    global prodindex
    global orders

    if lstindex is None:
        messagebox.showerror("Error", "Please select a customer.")
        return
    if prodindex is None:
        messagebox.showerror("Error", "Please select a product.")
        return

    product_type = prods[prodindex][1]
    product_desc = prods[prodindex][2]
    price = prods[prodindex][5]

    current_quantity = int(prods[prodindex][4])
    if current_quantity == 0:
        messagebox.showerror("Error", "Out of Stock!")
        return

    decrease_product_quantity(prodindex, 1)

    for order in orders:
        if order[0] == str(lstindex) and order[1] == str(prodindex):
            order[4] = str(int(order[4]) + 1)
            order[7] = str(int(order[4]) * int(order[5]))
            create_order_csv()
            ordersgrid(1)
            ordersgrid(0)
            break
    else:
        current_date = time.strftime("%m/%d/%Y")
        total_cost = str(float(price))
        new_order = [str(lstindex), str(prodindex), product_type, product_desc, '1', price, current_date, total_cost]
        orders.append(new_order)
        create_order_csv()
        ordersgrid(1)
        ordersgrid(0)

def deleteorder():
    global orderindex
    global orders
    
    if orderindex is None:
        messagebox.showerror("Error", "Please select an order to delete.")
        return

    try:
        quantity_index = orders[0].index("Quantity")
        prodindex = int(orders[orderindex + 1][1])  
    except (ValueError, IndexError):
        messagebox.showerror("Error", "Invalid order data.")
        return

       
    increase_product_quantity(prodindex, 1)
    
    orders[orderindex + 1][quantity_index] = str(int(orders[orderindex + 1][quantity_index]) - 1)
    orders[orderindex][7] = str(int(orders[orderindex + 1][quantity_index]) * int(orders[orderindex + 1][5]))
    
    if int(orders[orderindex + 1][quantity_index]) == 0:
        del orders[orderindex + 1]
    
    create_order_csv() 
    
    ordersgrid(1)
    ordersgrid(0)

def ordercallback(event):
   global orderindex

   li=[]
   li=event.widget._values
   orderindex = li[1]


def load_order_data():
    try:
        with open("C:\\docs\\orders.csv", newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                orders.append(row)
    except FileNotFoundError:
        pass

def create_order_csv():
    with open("C:\\docs\\orders.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for order in orders[1:]:
            writer.writerow(order)

def ordersgrid(n):
    global lstindex
    global orders

    for label in window.grid_slaves():
        if int(label.grid_info()["row"]) > len(lst) + 16:
            label.grid_forget()

    selected_customer_orders = [order for order in orders if order[0] == str(lst[lstindex][0])]

    for i, order in enumerate(selected_customer_orders):
        for j, value in enumerate(order):
            mgrid = tk.Entry(window, width=10)
            mgrid.insert(tk.END, value)
            mgrid.grid(row=i + 17 + len(lst), column=j + 11)

    if n == 1:
        for label in window.grid_slaves():
            if int(label.grid_info()["row"]) > len(lst) + 16:
                label.grid_forget()

def decrease_product_quantity(prodindex, quantity):
    global prods
    
    current_quantity = int(prods[prodindex][4])  
    new_quantity = current_quantity - 1
    if new_quantity < 0:
        new_quantity = 0
    prods[prodindex][4] = str(new_quantity)
    
    file_path = "C:\\docs\\products.csv"  
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for product in prods[1:]:
            writer.writerow(product)

    create_product_grid(1)
    create_product_grid(0)

def increase_product_quantity(prodindex, quantity):
    global prods
    
    try:
        prodindex = int(prodindex)
    except ValueError:
        print("Invalid product index:", prodindex)
        return
    
    current_quantity = int(prods[prodindex][4])  
    new_quantity = current_quantity + quantity
    prods[prodindex][4] = str(new_quantity)
    
    file_path = "C:\\docs\\products.csv"  
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for product in prods[1:]:
            writer.writerow(product)
    
    create_product_grid(1)
    create_product_grid(0)


window = tk.Tk()
window.title("Python Window")
window.geometry("1050x400")
window.configure(bg="grey")


menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Products", command=products)
filemenu.add_command(label="Customers", command=customers)
filemenu.add_separator()
filemenu.add_command(label="Close", command=window.quit)
window.config(menu=menubar)
load_customer_data()
load_order_data()


label = tk.Label(window, text="Customer Registration System", width=30, height=1, bg="lightgrey", anchor="center")
label.config(font=("Courier", 10))
label.grid(column=2, row=1)

label = tk.Label(window, text="ID:", width=15, height=1, bg="lightgrey")
label.grid(column=1, row=2)

cid = tk.StringVar()
custid = tk.Entry(window, textvariable=cid, state="disabled")
custid.grid(column=2, row=2)

label = tk.Label(window, text="Name:", width=15, height=1, bg="lightgrey")
label.grid(column=1, row=4)

cname = tk.StringVar()
custname = tk.Entry(window, textvariable=cname)
custname.grid(column=2, row=4)
custname.bind("<KeyRelease>", keyupname)

labelname = tk.Label(window, text="Santos, Pedro C.", width=15, height=1, bg="lightgrey")
labelname.grid(column=3, row=4)

label = tk.Label(window, text="Address:", width=15, height=1, bg="lightgrey")
label.grid(column=1, row=5)

caddress = tk.StringVar()
custaddress = tk.Entry(window, textvariable=caddress)
custaddress.grid(column=2, row=5)

label = tk.Label(window, text="Phone no.:", width=15, height=1, bg="lightgrey")
label.grid(column=1, row=6)

cphone = tk.StringVar()
custphone = tk.Entry(window, textvariable=cphone)
custphone.grid(column=2, row=6)
custphone.bind("<KeyRelease>", keyupphone)

labelphone = tk.Label(window, text="ex. 0912-456789", width=15, height=1, bg="lightgrey")
labelphone.grid(column=3, row=6)

label = tk.Label(window, text="Email:", width=15, height=1, bg="lightgrey")
label.grid(column=1, row=7)

cemail = tk.StringVar()
custemail = tk.Entry(window, textvariable=cemail)
custemail.grid(column=2, row=7)
custemail.bind("<KeyRelease>", keyupemail)

labelemail = tk.Label(window, text="name@mail.com", width=15, height=1, bg="lightgrey")
labelemail.grid(column=3, row=7)

label = tk.Label(window, text="Birthdate:", width=15, height=1, bg="lightgrey")
label.grid(column=1, row=8)

cbday = tk.StringVar()
custbday = tk.Entry(window, textvariable=cbday)
custbday.grid(column=2, row=8)
custbday.bind("<KeyRelease>", keyupbday)

labelbday = tk.Label(window, text="ex. MM/DD/YY", width=15, height=1, bg="lightgrey")
labelbday.grid(column=3, row=8)

label = tk.Label(window, text="Gender:", width=15, height=1, bg="lightgrey")
label.grid(column=1, row=9)

cgender = tk.StringVar()
custgender = tk.Entry(window, textvariable=cgender)
custgender.grid(column=2, row=9)

savebtn = tk.Button(text="Save", command=save)
savebtn.grid(column=1, row=10)

delbtn = tk.Button(text="Delete", command=delete)
delbtn.grid(column=2, row=10)

updbtn = tk.Button(text="Update", command=update)
updbtn.grid(column=3, row=10)

printbtn = tk.Button(window, text="Print to PDF", command=print_to_pdf)
printbtn.grid(column=4, row=10)

ordersgrid(0)
creategrid(0)

window.mainloop()