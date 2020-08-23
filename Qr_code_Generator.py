from qrcode import *
from tkinter import *
from PIL import Image


def qr_generator():
    qr = QRCode(
        version=1,
        box_size=10,
        border=4
    )
    if 0 < len(ent1.get()) <120:
        qr.add_data(ent1.get())
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="#fffffc")
        img.save('QrCode.png')
        lbl3.pack()
        btn2.pack()
    else:
        pass


def clr():
    ent1.delete(0, END)


def display():
    window = Toplevel()
    canvas1 = Canvas(window, width = 500, height =500)
    canvas1.pack()
    photo = PhotoImage(file="C://Users//DELL//Desktop//Python Code//Python VS Code//QrCode.png")
    canvas1.create_image(0, 0, image=photo, anchor=NW)
    window.mainloop(0)



root = Tk()
root.title("QrCode Generator")
root.geometry('550x500')
root.config(bg="white")

fr1 = Frame(root, bg="white")
fr1.pack()

lbl1 = Label(fr1, text="Qr Code Generator",fg="#2d00f7", bg="#fffffc", font=("Ubuntu", 30), bd=10)
lbl2 = Label(fr1, text=" Enter Your text:",fg="black", bg="#fffffc", font=("Helvetica", 13), bd=10)
ent1 = Entry(fr1, bg="white", bd=2, width=33)

fr2 = Frame(root, bg='yellow', width=50)
fr2.pack(side=TOP)

btn = Button(fr2, text="Generate Qr Code", command=qr_generator, bg="white", padx=10)
btn1 = Button(fr1, text="Clear Entry", command=clr, bg="white",bd=1, font=("Helvetica", 9), padx=10)

fr3 = Frame(root, bg="white")
fr3.pack()

lbl3 = Label(fr3, text="QR Code Generated", pady=20, bg="white", font=("Arial", 15), fg="#ff5400")
btn2 = Button(fr3, text="View Your QR Code", command=display, bg="white")





lbl1.pack()
lbl2.pack(side=LEFT)
ent1.pack(side=LEFT)

btn.pack(side=LEFT, fill=BOTH)
btn1.pack(side=RIGHT)



root.mainloop()
