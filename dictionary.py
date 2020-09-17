from tkinter import *
from PyDictionary import PyDictionary
from PIL import Image, ImageTk


def exit1():
    root.destroy()


def clear():
    entry.delete(0, END)
    t1.delete("1.0", "end")
    t2.delete("1.0", "end")
    t3.delete("1.0", "end")
    t4.delete("1.0", "end")


def search():
    t1.delete("1.0", "end")
    t2.delete("1.0", "end")
    t3.delete("1.0", "end")
    t4.delete("1.0", "end")
    dictionary = PyDictionary()
    ip = entry.get()
    try:
        a = dictionary.meaning(ip)
        pos = a.keys()
        meaning = a.values()
        n = 0
        try:
            for i in meaning:
                t1.insert(END, i[0] + '\n')
                n += 1
                if n > 2:
                    break
        except:
            pass
        try:
            for j in pos:
                t2.insert(END, j + ', ')
        except:
            pass
    except:
        t1.delete("1.0", "end")
        t1.insert(INSERT, 'Not Found.....')
        return

    try:
        n = 0
        synonyms = dictionary.synonym(ip)
        for i in synonyms:
            t3.insert(END, i + '\n')
            n += 1
            if n > 5:
                break
    except:
        pass

    try:
        n = 0
        antonyms = dictionary.antonym(ip)
        for i in antonyms:
            t4.insert(END, i + '\n')
            n += 1
            if n > 5:
                break
    except:
        pass


root = Tk()
root.title("The Dictionary App")
root.geometry("700x525")
root.config(background="#dee2e6")
root.resizable(0, 0)

load = Image.open("l1.png")
render = ImageTk.PhotoImage(load)
label1 = Label(root, image=render)
label1.image = render
label1.place(x=-2, y=0)

l11 = Label(root, text="Enter Your Word: ", font=("Arial", 10, 'bold'), bg="#dee2e6")
l11.place(x=150, y=75)

entry = Entry(root, width=40, bd=2)
entry.place(x=275, y=75)

button = Button(root, text="Search", font=("Arial", 10, 'bold'), command=search, relief=GROOVE, bg="#e9ecef",
                activebackground="#053c5e", activeforeground="white")
button.place(x=330, y=105)

button1 = Button(root, text="Clear", font=("Arial", 10, 'bold'), command=clear, relief=GROOVE, bg="#e9ecef",
                 activebackground="#053c5e", activeforeground="white")
button1.place(x=395, y=105)


label2 = Label(root, text="Meaning: ", font=("Arial", 10, 'bold'), bg="#dee2e6")
label2.place(x=50, y=155)

t1 = Text(root, bg="#f8f9fa", height=4, width=85, fg="black", font=('Arial', 10))
t1.place(x=50, y=180)

l2 = Label(root, text="Parts of Speech: ", font=("Arial", 9, 'bold'), bg="#dee2e6")
l2.place(x=50, y=280)

t2 = Text(root, bg="#f8f9fa", height=1, width=70, font=('Arial', 10))
t2.place(x=155, y=280)

l3 = Label(root, text="Synonyms: ", font=('Arial', 10, 'bold'), bg="#dee2e6")
l4 = Label(root, text="Antonyms: ", font=('Arial', 10, 'bold'), bg="#dee2e6")
t3 = Text(root, bg='#f8f9fa', height=5, width=38, font=('Arial', 10))
t4 = Text(root, bg='#f8f9fa', height=5, width=38, font=('Arial', 10))

l3.place(x=50, y=325)
t3.place(x=50, y=350)
l4.place(x=380, y=325)
t4.place(x=380, y=350)

button3 = Button(root, text="Exit", font=("Arial", 10, 'bold'), width=10, command=exit1, relief=GROOVE, bg="#e9ecef",
                 activebackground="red", activeforeground="white"
                 )
button3.place(x=600, y=490)
root.mainloop()
