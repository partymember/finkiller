import tkinter as tk


def fill_expense_label_frame(master_frame):
    lbl_date = tk.Label(text="Date", master=master_frame)
    lbl_name = tk.Label(text="Name", master=master_frame)
    lbl_product = tk.Label(text="Product", master=master_frame)
    lbl_cat = tk.Label(text="Category", master=master_frame)
    lbl_price = tk.Label(text="Price", master=master_frame)
    lbl_date.pack()
    lbl_name.pack()
    lbl_product.pack()
    lbl_cat.pack()
    lbl_price.pack()


def fill_expense_entry_frame(master_frame):
    ent_date = tk.Entry(master=master_frame)
    ent_name = tk.Entry(master=master_frame)
    ent_product = tk.Entry(master=master_frame)
    ent_cat = tk.Entry(master=master_frame)
    ent_price = tk.Entry(master=master_frame)
    ent_date.pack()
    ent_name.pack()
    ent_product.pack()
    ent_cat.pack()
    ent_price.pack()


def window_create():
    window = tk.Tk(screenName="Finkiller v6.6.6")
    frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
    frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    fill_expense_entry_frame(frame1)

    frame2 = tk.Frame(master=window, width=200, bg="yellow")
    frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    fill_expense_label_frame(frame2)

    frame3 = tk.Frame(master=window, width=200, bg="blue")
    frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    # btn_print = tk.Button(text="Hello")
    # btn_print.pack()
    # btn_print.bind("<Button-1>", printbtn)
    return window
