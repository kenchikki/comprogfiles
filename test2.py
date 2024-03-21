import tkinter as tk

window = tk.Tk()
window.title("Python window")
window.geometry("1050x400")
window.configure(bg="red")

label = tk.Label(window, text="Products System", width=30, height=1, bg="orange", anchor="center")
label.config(font=('Courter',10))
label.grid(column=2,row=1)

label = tk.Label(window, text="Product ID:", width=15, height=1,bg="orange")
label.grid(column=1,row=2)

pid=tk.StringVar()
prodid = tk.Entry(window, textvariable=pid)
prodid.grid(column=2,row=2)

label = tk.Label(window, text="Product Type:", width=15, height=1,bg="orange")
label.grid(column=1, row=3)

prot = tk.StringVar()
prodtype =tk.Entry(window, textvariable=prot)
prodtype.grid(column=2,row=3)


label = tk.Label(window, text="Product Description:", width=15, height=1,bg="orange")
label.grid(column=1,row=6)

pdesc =tk.StringVar()
prodesc = tk.Entry(window, textvariable=pdesc)
prodesc.grid(column=2, row=6)

label = tk.Label(window, text="Supplier:", width=15, height=1,bg="orange")
label.grid(column=1,row=7)

sup=tk.StringVar()
prodsup = tk.Entry(window, textvariable=sup)
prodsup.grid(column=2, row=7)

label = tk.Label(window, text="Quantity:", width=15, height=1,bg="orange")
label.grid(column=1,row=8)

quan = tk.StringVar()
prodquan = tk.Entry(window, textvariable=quan)
prodquan.grid(column=2, row=8)

labelquan =  tk.Label(window, text="must be a number", width=15, height=1,bg="orange")
labelquan.grid(column=3,row=8)

label = tk.Label(window, text="Total Cost:", width=15, height=1,bg="orange")
label.grid(column=1,row=9)

ptc = tk.StringVar()
prodtc = tk.Entry(window, textvariable=ptc)
prodtc.grid(column=2, row=9)

labeltc = tk.Label(window, text="must be a number:", width=15, height=1,bg="orange")
labeltc.grid(column=3,row=9)

label = tk.Label(window, text="Date Received:", width=15, height=1,bg="orange")
label.grid(column=1,row=10)

pdr = tk.StringVar()
proddr = tk.Entry(window, textvariable=pdr)
proddr.grid(column=2, row=10)

labeldr = tk.Label(window, text="mm/dd/yyyy", width=15, height=1,bg="orange")
labeldr.grid(column=3,row=10)





window.mainloop()
