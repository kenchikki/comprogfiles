import tkinter as tk
from tkinter import messagebox
import re
import csv


i = 1
x = 0
window2 = None
pid = None
ptype = None
pdesc = None
psup = None
pquantity = None
pcost = None
productdate = None
prodquantity = None
labelquantity,labelpdate,labelcost = None, None, None
orderindex = 0
myid = ""
lstindex = 0
newprodlstindex = 0
prodlstindex = 0
PRODUCTID,PRODUCTTYPE,PRODUCTDESCRIPTION,PRODUCTSUPPLIER,PRODUCTQUANTITY,PRODUCTCOST,PRODUCTDATE,TOTALCOST = '','','','','','','',''
CompareQuantity = 0
lst = [['ID','Email','Phone','Name','Address','Date','Gender']]
orders = [['CID','PID','PType','Description','Supplier','Quantity',"Cost","DateOrdered",'Total']]
prodlst = [['ID','Type','Description','Supplier','Quantity','Cost','Date']]
prodli=[]

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=	
def keyupdate(a) :

	CustBirth = cbirth.get()
	isValid = False

	if re.match(r"\d{2}/\d{2}/\d{4}", CustBirth):
   		isValid = True
	else:
		isValid = False

	if isValid and not re.match(r"\d{2}/\d{2}/\d{5}", CustBirth):
    		labeldate.config(text='Valid')
	else:
    		labeldate.config(text='Invalid')
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def msgbox2(msg,titlebar):
	result=messagebox.askokcancel(title=titlebar,message=msg)
	return result
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def products():

	global pid,ptype,pdesc,psup,pquantity,pcost,productdate,prodid,prodtype,proddesc,prodsup,prodquantity,prodcost,proddate,labelquantity,labelpdate,labelcost

	isValidDate = False
	isValidCost = False
	isValidQuantity = False
	global window2
	global prodlstindex

	window2 = tk.Tk()
	window2.title("Products Window")
	window2.geometry("1050x400")
	window2.configure(bg="pink")

	label2 = tk.Label(window2, text="Product Registration System", width = 30, height=1, bg="white", anchor="center")
	label2.config(font=("Courier",10))
	label2.grid(column=2,row=1)

	label2 = tk.Label(window2, text="Product ID:", width = 10, height=1, bg="white")
	label2.grid(column=1,row=2)

	pid=tk.StringVar(window2)
	prodid = tk.Entry(window2,textvariable=pid, state ='disabled')
	prodid.grid(column=2,row=2)

	label2 = tk.Label(window2, text="Product Type:", width = 10, height=1, bg="white")
	label2.grid(column=1,row=3)

	ptype=tk.StringVar(window2)
	prodtype = tk.Entry(window2,textvariable=ptype)
	prodtype.grid(column=2,row=3)

	label2 = tk.Label(window2, text="Product Description:", width = 15, height=1, bg="white")
	label2.grid(column=1,row=4)

	pdesc=tk.StringVar(window2)
	proddesc = tk.Entry(window2,textvariable=pdesc)
	proddesc.grid(column=2,row=4)

	label2 = tk.Label(window2, text="Supplier:", width = 10, height=1, bg="white")
	label2.grid(column=1,row=5)

	psup=tk.StringVar(window2)
	prodsup = tk.Entry(window2,textvariable=psup)
	prodsup.grid(column=2,row=5)

	label2 = tk.Label(window2, text="Quantity:", width = 10, height=1, bg="white")
	label2.grid(column=1,row=6)

	labelquantity = tk.Label(window2, text="ex.123123123", width = 10, height=1, bg="white")
	labelquantity.grid(column=3,row=6)

	pquantity=tk.StringVar(window2)
	prodquantity = tk.Entry(window2,textvariable=pquantity)
	prodquantity.grid(column=2,row=6)
	prodquantity.bind("<KeyRelease>", keyquantity)

	label2 = tk.Label(window2, text="Total Cost:", width = 10, height=1, bg="white")
	label2.grid(column=1,row=7)

	labelcost = tk.Label(window2, text="ex. 123123123", width = 10, height=1, bg="white")
	labelcost.grid(column=3,row=7)

	pcost=tk.StringVar(window2)
	prodcost = tk.Entry(window2,textvariable=pcost)
	prodcost.grid(column=2,row=7)
	prodcost.bind("<KeyRelease>",keypcost)

	label2 = tk.Label(window2, text="Date Received:", width = 10, height=1, bg="white")
	label2.grid(column=1,row=8)

	labelpdate = tk.Label(window2, text="MM/DD/YYYY", width = 11, height=1, bg="white")
	labelpdate.grid(column=3,row=8)

	productdate = tk.StringVar(window2)
	proddate = tk.Entry(window2, textvariable=productdate)
	proddate.grid(column=2, row=8)
	proddate.bind("<KeyRelease>",keynamedate)

	savebtn2 = tk.Button(window2, text = "Save", command=save2)
	savebtn2.grid(column=1,row=9)
	
	deletebtn2 = tk.Button(window2,text = "Delete", command=delete2)
	deletebtn2.grid(column=2,row=9)

	updatebtn2 = tk.Button(window2,text = "Update", command=update2)
	updatebtn2.grid(column=3,row=9)

	prodcreategrid(0)


def keynamedate(b):
	
	date=proddate.get()

	global isValidDate

	if re.match(r"\d{2}/\d{2}/\d{4}", date):
   		isValidDate = True
	else:
		isValidDate = False

	if isValidDate and not re.match(r"\d{2}/\d{2}/\d{5}", date):
    		labelpdate.config(text='Valid')
	else:
    		labelpdate.config(text='Invalid')

def keypcost(a):
	cost = prodcost.get()
	global isValidCost
	for char in cost:
		if char.isdigit():
			isValidCost = True
		if isValidCost:
			labelcost.config(text="Valid")
		else:
			labelcost.config(text="Invalid")
	
def keyquantity(a):
	quant = prodquantity.get()
	global isValidQuantity
	for char in quant:
		if char.isdigit():
			isValidQuantity = True
		if isValidQuantity:
			labelquantity.config(text="Valid")
		else:
			labelquantity.config(text="Invalid")

	
def prodcallback(event):
	
	global newprodlstindex
	global prodlstindex
	global myid
	global PRODUCTTYPE
	global PRODUCTDESCRIPTION
	global PRODUCTSUPPLIER
	global PRODUCTQUANTITY
	global PRODUCTCOST
	global PRODUCTDATE
	prodli=[]
	prodli=event.widget._values
	myid = prodlst[prodli[1]][0]
	prodlstindex = prodli[1]
	pid.set(prodlst[prodli[1]][0])
	ptype.set(prodlst[prodli[1]][1])
	pdesc.set(prodlst[prodli[1]][2])
	psup.set(prodlst[prodli[1]][3])
	pquantity.set(prodlst[prodli[1]][4])
	pcost.set(prodlst[prodli[1]][5])
	productdate.set(prodlst[prodli[1]][6])

	PRODUCTTYPE = prodlst[prodli[1]][1]
	PRODUCTDESCRIPTION = prodlst[prodli[1]][2]
	PRODUCTSUPPLIER = prodlst[prodli[1]][3]
	PRODUCTQUANTITY = prodlst[prodli[1]][4]
	PRODUCTCOST = prodlst[prodli[1]][5]
	PRODUCTDATE= prodlst[prodli[1]][6]
	
def save2():

	i = 1
	IDs = {int(row[0]) for row in prodlst if row[0].isdigit()}
	low = 1
	while low in IDs:
		low += 1

	pid.set(str(low))

	isValidQuantity = False
	isValidDate = False
	isValidCost = False
		
	date=proddate.get()
	if re.match(r"\d{2}/\d{2}/\d{4}", date):
   		isValidDate = True
	else:
		isValidDate = False

	cost = prodcost.get()
	for char in cost:
		if char.isdigit():
			isValidCost = True

	quant = prodquantity.get()
	for char in quant:
		if char.isdigit():
			isValidQuantity = True

	r=msgbox2("Save record?","record")
	if r == True:
		if isValidQuantity and isValidDate and isValidCost:
			prodlst.append([prodid.get(),prodtype.get(),proddesc.get(),prodsup.get(),prodquantity.get(),prodcost.get(),proddate.get()])
			prodcreategrid(0)
		else:
			r=msgbox2("WRONG", "Invalid")

def update2():
	global prodlstindex
	isValidQuantity = False
	isValidDate = False
	isValidCost = False
			
	date=proddate.get()
	if re.match(r"\d{2}/\d{2}/\d{4}", date):
   		isValidDate = True
	else:
		isValidDate = False

	cost = prodcost.get()
	for char in cost:
		if char.isdigit():
			isValidCost = True

	quant = prodquantity.get()
	for char in quant:
		if char.isdigit():
			isValidQuantity = True


	r=msgbox("Update?","record")
	if r == True:
		if isValidQuantity and isValidDate and isValidCost:
			prodlst[prodlstindex] = [prodid.get(),prodtype.get(),proddesc.get(),prodsup.get(),prodquantity.get(),prodcost.get(),proddate.get()]
			prodcreategrid(1)
			prodcreategrid(0)
		else:
			r=msgbox("Invalid Input", "Invalid")
	

def prodcreategrid(n):
	if n == 0:
		for i in range(len(prodlst)): #row
			for j in range(len(prodlst[0])): #column
				mgrid = tk.Entry(window2,width=10)
				mgrid.insert(tk.END, prodlst[i][j])
				mgrid._values = mgrid.get(), i
				mgrid.grid(row=i+11,column=j+8)
				mgrid.bind("<Button-1>", prodcallback)

	if n==1:
		for label2 in window2.grid_slaves():
			if int(label2.grid_info()["row"]) > 11:
				label2.grid_forget()
	
def delete2():
	global prodlstindex
	r = msgbox("Delete record?", "record")
	if r==True:
		del(prodlst[prodlstindex])
		prodcreategrid(1)
		prodcreategrid(0)


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def customers():
	r=msgbox("Customer Form","Form")
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def msgbox(msg,titlebar):
	result=messagebox.askokcancel(title=titlebar,message=msg)
	return result
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def keyupphone(a):
	phone = custphone.get()
	isValid = True
	if re.match(r"\d{4}-\d{7}", phone):
   		isValid = True
	else:
		isValid = False
	if isValid and not re.match(r"\d{4}-\d{8}", phone):
		labelphone.config(text='Valid')
	else:
		labelphone.config(text='Invalid')
		
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=		
def keyup(a) :
	global at
	global dotcom

	email=custemail.get()
	if "@" in email and "." in email and email.index("@") < email.index("."):
 		at = True
	else:
		at = False 
	if email. endswith(".com"):
		dotcom = True
	else:
		dotcom = False
	if at and dotcom:
		labelemail.config(text="Good")
	else:
		labelemail.config(text="Incorrect")
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def keyupname(a):
	cust_name = cname.get().strip()
	is_valid = re.match(r"^[A-Za-z\-\.\'ñÑ]+, [A-Za-z + A-Za-z]+ [A-Za-z]\.$", cust_name)

	if is_valid:
    		labelname.config(text="Valid")
	else:
    		labelname.config(text="Invalid")


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def callback(event):
	global lstindex
	li=[]
	li=event.widget._values
	lstindex = li[1]
	cid.set(lst[li[1]][0])
	cemail.set(lst[li[1]][1])
	cphone.set(lst[li[1]][2])
	custname.set(lst[li[1]][3])
	custaddress.set(lst[li[1]][4])
	custbirth.set(lst[li[1]][5])
	custgender.set(lst[li[1]][6])

	ordersgrid(1)
	ordersgrid(0)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def creategrid(n):
	if n == 0:
		for i in range(len(lst)): #row
			for j in range(len(lst[0])): #column
				mgrid = tk.Entry(window,width=10)
				mgrid.insert(tk.END,lst[i][j])
				mgrid._values = mgrid.get(), i
				mgrid.grid(row=i+11,column=j+8)
				mgrid.bind("<Button-1>", callback)
	if n==1:
		for label in window.grid_slaves():
			if int(label.grid_info()["row"]) > 11:
				label.grid_forget()

	AddOrder = tk.Button(text = "Add Order", command=addorder)
	AddOrder.grid(column=2,row=16+len(lst))

	DeleteOrder = tk.Button(text = "Delete Order", command=deleteorder)
	DeleteOrder.grid(column=3,row=16+len(lst))

	label = tk.Label(window, text="CID", width = 5, height=1, bg="pink")
	label.grid(column=8,row=16+len(lst))

	label = tk.Label(window, text="PID", width = 5, height=1, bg="pink")
	label.grid(column=9,row=16+len(lst))

	label = tk.Label(window, text="Ptype", width = 5, height=1, bg="pink")
	label.grid(column=10,row=16+len(lst))

	label = tk.Label(window, text="Description", width = 8, height=1, bg="pink")
	label.grid(column=11,row=16+len(lst))

	label = tk.Label(window, text="Supplier", width = 7, height=1, bg="pink")
	label.grid(column=12,row=16+len(lst))

	label = tk.Label(window, text="Quantity", width = 7, height=1, bg="pink")
	label.grid(column=13,row=16+len(lst))

	label = tk.Label(window, text="Cost", width = 5, height=1, bg="pink")
	label.grid(column=14,row=16+len(lst))

	label = tk.Label(window, text="Date", width = 5, height=1, bg="pink")
	label.grid(column=15,row=16+len(lst))

	label = tk.Label(window, text="Total", width = 4, height=1, bg="pink")
	label.grid(column=16,row=16+len(lst))


	ordersgrid(1)
	ordersgrid(0)

def save_customer_csv():
    with open('customers.csv', 'w', newline='') as csvfile:
        fieldnames = ['Customer ID', 'Email', 'Phone', 'Name', 'Address', 'Birthdate', 'Gender']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in lst:
            writer.writerow({'Customer ID': row[0], 'Email': row[1], 'Phone': row[2], 'Name': row[3], 'Address': row[4], 'Birthdate': row[5], 'Gender': row[6]})
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=	
def ordersgrid(n):
	if n == 0:
		for i in range(len(orders)): #row
			if lstindex == orders[i][0]:
				for j in range(len(orders[0])): #column
					mgrid = tk.Entry(window,width=10)
					mgrid.insert(tk.END,orders[i][j])
					mgrid._values = mgrid.get(), i
					mgrid.grid(row=i+16+len(lst),column=j+8)
					mgrid.bind("<Button-1>", ordercallback)
	if n==1:
		for label in window.grid_slaves():
			if int(label.grid_info()["row"]) >len(lst) + 16:
				label.grid_forget()

def save_order_csv():
    with open('orders.csv', 'w', newline='') as csvfile:
        fieldnames = ['Order ID', 'Customer ID', 'Product Type', 'Description', 'Supplier', 'Quantity', 'Cost', 'Date Ordered', 'Total Cost']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in orders:
            writer.writerow({'Order ID': row[0], 'Customer ID': row[1], 'Product Type': row[2], 'Description': row[3], 'Supplier': row[4], 'Quantity': row[5], 'Cost': row[6], 'Date Ordered': row[7], 'Total Cost': row[8]})
def save_product_csv():
    with open('products.csv', 'w', newline='') as csvfile:
        fieldnames = ['Product ID', 'Type', 'Description', 'Supplier', 'Quantity', 'Cost', 'Date Received']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in prodlst:
            writer.writerow({'Product ID': row[0], 'Type': row[1], 'Description': row[2], 'Supplier': row[3], 'Quantity': row[4], 'Cost': row[5], 'Date Received': row[6]})
#lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao lmao 
def addorder():
	global myid, lstindex
	global prodlst
	global PRODUCTQUANTITY
	TEMPQUANTITY = '1'
	CompareQuantity = int(TEMPQUANTITY)
	AnotherQuantity = int(PRODUCTQUANTITY)
	r=msgbox("Add Order?", "order")
	if r==True:
		if AnotherQuantity > 0:
			found = False
			for order in orders:
				if order[1] == myid and order[0] == lstindex:
					order[5] = str(int(order[5]) + 1)
					order[8] = str(int(order[5]) * int(order[6]))
					found = True
					DeleteQuantity()
					ordersgrid(1)
					ordersgrid(0)
					break
			if not found:
				selected_product = prodlst[prodlstindex]
				pid, ptype, pdesc, psup, pquantity, pcost, productdate = selected_product 
				TEMPQUANTITY = '1'
				TOTALCOST = str(int(PRODUCTCOST) * int(TEMPQUANTITY))
				orders.append([lstindex, myid, PRODUCTTYPE, PRODUCTDESCRIPTION, PRODUCTSUPPLIER, TEMPQUANTITY, PRODUCTCOST, PRODUCTDATE, TOTALCOST])
				DeleteQuantity()
				ordersgrid(1)
				ordersgrid(0)
		else:
			r=msgbox("Out of Stock", "Stock")

	
def deleteorder():
	global myid
	global orderindex
    
	if orderindex is not None:
		orders[orderindex][5] = str(int(orders[orderindex][5]) - 1)
		orders[orderindex][8] = str(int(orders[orderindex][5]) * int(orders[orderindex][6]))
		AddQuantity()
        
	if int(orders[orderindex][5]) == 0:
		del orders[orderindex]

	ordersgrid(1)
	ordersgrid(0)

def ordercallback(event):
	global orderindex
	li=[]
	li=event.widget._values
	orderindex = li[1]

def DeleteQuantity():
	global prodlst
	global prodlstindex
	global PRODUCTQUANTITY
	NEWQUANTITY = ''

	if prodlstindex is not None:
		TempQuantity = int(PRODUCTQUANTITY)
		NEWQUANTITY = str(TempQuantity - 1)
		prodlst[prodlstindex] = [prodid.get(), prodtype.get(), proddesc.get(), prodsup.get(),NEWQUANTITY, prodcost.get(), proddate.get()]
		prodcreategrid(1)
		prodcreategrid(0)
		PRODUCTQUANTITY = NEWQUANTITY

def AddQuantity():
	global prodlst
	global prodlstindex
	global PRODUCTQUANTITY
	NEWQUANTITY = ''

	if prodlstindex is not None:
		TempQuantity = int(PRODUCTQUANTITY)
		NEWQUANTITY = str(TempQuantity + 1)
		prodlst[prodlstindex] = [prodid.get(), prodtype.get(), proddesc.get(), prodsup.get(),NEWQUANTITY, prodcost.get(), proddate.get()]
		prodcreategrid(1)
		prodcreategrid(0)
		PRODUCTQUANTITY = NEWQUANTITY
	else:
		r=msgbox("No More Orders", "Orders")


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=	
def save():
	global lst
	global i
	global x

	IDs = {int(row[0]) for row in lst if row[0].isdigit()}
	low = 1
	while low in IDs:
		low += 1

	cid.set(str(low))

	i = max(i, low) + 1

	isValidBirthdate = False
	isValidPhone = False
	isValidName = False
	

	name = cname.get().strip()
	is_valid = re.match(r"^[A-Za-z\-\.\'ñÑ]+, [A-Za-z + A-Za-z]+ [A-Za-z]\.$", name)

	if is_valid:
    		isValidName = True
	else:
    		isValidName = False

	phone = custphone.get()
	if re.match(r"\d{4}-\d{7}", phone):
   		isValidPhone = True
	else:
		isValidPhone = False

	email = custemail.get()
	if "@" in email and "." in email and email.index("@") < email.index("."):
 		at = True
	else:
		at = False 
	if email. endswith(".com"):
		dotcom = True
	else:
		dotcom = False

	CustBirth = cbirth.get()

	if re.match(r"\d{2}/\d{2}/\d{4}", CustBirth):
   		isValidBirthdate = True
	else:
		isValidBirthdate = False


	if isValidBirthdate and isValidPhone and at and	dotcom and isValidName:
		r=msgbox("save record?","record")
		if r == True:
			lst.append([custid.get(),custemail.get(),custphone.get(),cname.get(),caddress.get(),cbirth.get(),custgender.get()])
			creategrid(1)
			creategrid(0)
	else:
		r=msgbox("Invalid Input", "Invalid")

def delete():
	global lstindex
	r = msgbox("Delete record?", "record")
	if r==True:
		del(lst[lstindex])
		creategrid(1)
		creategrid(0)


def update():
	isValidBirthdate = False
	isValidPhone = False
	isValidName = False
	

	name = cname.get().strip()
	is_valid = re.match(r"^[A-Za-z\-\.\'ñÑ]+, [A-Za-z + A-Za-z]+ [A-Za-z]\.$", name)

	if is_valid:
    		isValidName = True
	else:
    		isValidName = False

	phone = custphone.get()
	if re.match(r"\d{4}-\d{7}", phone):
   		isValidPhone = True
	else:
		isValidPhone = False

	email = custemail.get()
	if "@" in email and "." in email and email.index("@") < email.index("."):
 		at = True
	else:
		at = False 
	if email. endswith(".com"):
		dotcom = True
	else:
		dotcom = False

	CustBirth = cbirth.get()

	if re.match(r"\d{2}/\d{2}/\d{4}", CustBirth):
   		isValidBirthdate = True
	else:
		isValidBirthdate = False


	if isValidBirthdate and isValidPhone and at and	dotcom and isValidName:
		r=msgbox("Update?","record")
		if r == True:
			lst[lstindex] = [custid.get(),custemail.get(),custphone.get(),cname.get(),caddress.get(),cbirth.get(),custgender.get()]
			creategrid(1)
			creategrid(0)
	else:
		r=msgbox("Invalid Input", "Invalid")
	
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=	

window = tk.Tk()
window.title("Python Window")
window.geometry("1050x400")
window.configure(bg="grey") 	

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Products", command=products)
filemenu.add_command(label="Customer", command=customers)
filemenu.add_separator()
filemenu.add_command(label="Close", command=window.quit)
window.config(menu=menubar)

label = tk.Label(window, text="Customer Registration System", width = 30, height=1, bg="lightgrey", anchor="center")
label.config(font=("Courier",10))
label.grid(column=2,row=1)

label = tk.Label(window, text="Customer ID:", width = 10, height=1, bg="lightgrey")
label.grid(column=1,row=2)

cid=tk.StringVar()
custid = tk.Entry(window,textvariable=cid, state = 'disabled')
custid.grid(column=2,row=2)

label = tk.Label(window, text="Customer Email:", width = 12, height=1, bg="lightgrey")
label.grid(column=1,row=4)

cemail=tk.StringVar()
custemail=tk.Entry(window, textvariable=cemail)
custemail.grid(column=2,row=4)
custemail.bind("<KeyRelease>",keyup)

labelemail = tk.Label(window, text="[a-z]@[a-z].com", width = 15, height=1, bg="lightgrey")
labelemail.grid(column=3,row=4)

label = tk.Label(window, text="Customer Phone:", width = 12, height=1, bg="lightgrey")
label.grid(column=1,row=5)

cphone=tk.StringVar()
custphone=tk.Entry(window, textvariable=cphone)
custphone.grid(column=2,row=5)
custphone.bind("<KeyRelease>",keyupphone)

labelphone = tk.Label(window, text="ex. 0912-3456789", width = 15, height=1, bg="lightgrey")
labelphone.grid(column=3,row=5)

label = tk.Label(window, text="Customer Name:", width = 14, height=1, bg="lightgrey")
label.grid(column=1,row=7)

labelname = tk.Label(window, text="ex: Dela Cruz, Juan P.", width = 17, height=1, bg="lightgrey")
labelname.grid(column=3,row=7)

custname=tk.StringVar()
cname = tk.Entry(window,textvariable=custname)
cname.grid(column=2,row=7)
cname.bind("<KeyRelease>", keyupname)


label = tk.Label(window, text="Address:", width = 14, height=1, bg="lightgrey")
label.grid(column=1,row=8)

custaddress=tk.StringVar()
caddress = tk.Entry(window,textvariable=custaddress)
caddress.grid(column=2,row=8)

label = tk.Label(window, text="Customer Birthdate:", width = 14, height=1, bg="lightgrey")
label.grid(column=1,row=9)

labeldate = tk.Label(window, text="MM/DD/YYYY", width = 11, height=1, bg="lightgrey")
labeldate.grid(column=3,row=9)

custbirth=tk.StringVar()
cbirth = tk.Entry(window,textvariable=custbirth)
cbirth.grid(column=2,row=9)
cbirth.bind("<KeyRelease>",keyupdate)

label= tk.Label(window, text="Customer Gender:", width = 14, height=1, bg="lightgrey")
label.grid(column=1,row=10)

custgender=tk.StringVar()
cgender = tk.Entry(window,textvariable=custgender)
cgender.grid(column=2,row=10)

savebtn = tk.Button(text = "Save", command=save)
savebtn.grid(column=1,row=11)

Delete = tk.Button(text = "Delete", command=delete)
Delete.grid(column=2,row=11)

Update = tk.Button(text = "Update", command=update)
Update.grid(column=3,row=11)


ordersgrid(0)
creategrid(0)
save_customer_csv()
save_order_csv()
save_product_csv()

window.mainloop()