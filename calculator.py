from tkinter import *
root = Tk()
display = ""


def cancel():
    global display
    display = display[:-1]
    cal_disp.config(text=display)


def eval1(value):
    global display
    display + = value
    cal_disp.config(text=display)


def total():
    try:
        global display
        display1 = eval(display)
        cal_disp.config(text=display1)
        display = " "
    except BaseException:
        display = "error"
        cal_disp.config(text=display)
        display = " "


root.title("calculator")

if __name__ == "__main__":
    frame1 = Frame(root)
    frame1.grid(row=1, column=0)
    frame2 = Frame(root, width=8)
    frame2.grid(row=2, column=0)
    frame3 = Frame(root, width=8)
    frame3.grid(row=3, column=0)

    cal_disp = Label(root, width=17, border=1)
    cal_disp.grid(row=0, column=0)

    cancelbt = Button(frame1, text="c", command=lambda: cancel(), width=10)
    cancelbt.grid(row=1, column=0)

    bt_div = Button(frame1, text="/", command=lambda: eval1("/"), width=5)
    bt_div.grid(row=1, column=1)

    bt_1 = Button(frame2, text="1", command=lambda: eval1("1"), width=3)
    bt_1.grid(row=0, column=0)

    bt_2 = Button(frame2, text="2", command=lambda: eval1("2"), width=3)
    bt_2.grid(row=0, column=1)

    bt_3 = Button(frame2, text="3", command=lambda: eval1("3"), width=3)
    bt_3.grid(row=0, column=2)

    bt_4 = Button(frame2, text="4", command=lambda: eval1("4"), width=3)
    bt_4.grid(row=1, column=0)

    bt_5 = Button(frame2, text="5", command=lambda: eval1("5"), width=3)
    bt_5.grid(row=1, column=1)

    bt_6 = Button(frame2, text="6", command=lambda: eval1("6"), width=3)
    bt_6.grid(row=1, column=2)

    bt_7 = Button(frame2, text="7", command=lambda: eval1("7"), width=3)
    bt_7.grid(row=2, column=0)

    bt_8 = Button(frame2, text="8", command=lambda: eval1("8"), width=3)
    bt_8.grid(row=2, column=1)

    bt_9 = Button(frame2, text="9", command=lambda: eval1("9"), width=3)
    bt_9.grid(row=2, column=2)

    bt_mult = Button(frame2, text="*", command=lambda: eval1("*"), width=3)
    bt_mult.grid(row=0, column=3)

    bt_sub = Button(frame2, text="-", command=lambda: eval1("-"), width=3)
    bt_sub.grid(row=1, column=3)

    bt_add = Button(frame2, text="+", command=lambda: eval1("+"), width=3)
    bt_add.grid(row=2, column=3)

    bt_0 = Button(frame3, text="0", command=lambda: eval1("0"), width=3)
    bt_0.grid(row=0, column=0)

    bt_dot = Button(frame3, text=".", command=lambda: eval1("."), width=9)
    bt_dot.grid(row=0, column=1)

    bt_eval = Button(frame3, text="=", command=lambda: total(), width=3)
    bt_eval.grid(row=0, column=2)

root.mainloop()
