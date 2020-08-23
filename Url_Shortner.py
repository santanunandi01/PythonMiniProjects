import tkinter as tk
import pyshorteners


def url_shorter():
    shorter_url = pyshorteners.Shortener().tinyurl.short(entry1.get())
    txt.delete("1.0", "end")
    txt.insert(0.0, str(shorter_url))


def clc():
    entry1.delete(0, 1000)


def copy():
    txt.clipboard_clear()
    t2 = txt.get(0.0, 100.0)
    txt.clipboard_append(t2)


root = tk.Tk()
root.title('url shortner')
root.geometry("600x350")
root.configure(bg="#ffffff")
root.resizable(0, 0)

t1 = "Your One Click url Shortner"

frame_one = tk.Frame(root, bg='#e5e5e5', width='650', height='180')
frame_one.grid(row=0, column=0, padx=1, pady=20)

label_one = tk.Label(frame_one, bg='#e5e5e5', fg='black', width='0', height='1', text=t1)
label_one.config(font=("Calibre", 15))
label_one.pack(side='top')

label_two = tk.Label(frame_one, bg='#e5e5e5', width='0', height='1', text="Insert Your Url ")
label_two.config(font=("Calibre", 15))
label_two.pack(side='bottom')

frame_two = tk.Frame(root, bg='white', width='630', height='145')
frame_two.grid(row=1, column=0, padx=10, pady=20)

link = tk.Label(frame_two, text=" Url:  ")
link.config(font=("Calibre", 10))
entry1 = tk.Entry(frame_two, bd=2, width=50)
link.grid(row=0, column=0)
entry1.grid(row=0, column=1)
url = entry1.get()


button1 = tk.Button(frame_two, text="Short Your Url", bg="#ffffff", command=url_shorter, activeforeground="blue")
button1.grid(row=1, column=1)


button2 = tk.Button(frame_two, text="clear", bg="#ffffff", width=7, height=1, command=clc, activeforeground="blue")
button2.grid(row=0, column=2)

frame_three = tk.Frame(root, bg='#ffffff', width='630', height='10')
frame_three.grid(row=3, column=0, padx=10, pady=20)

label_three = tk.Label(frame_three, text='Your Shorted url is: ', fg= 'black', bg='yellow', font=("Calibre", 10))
label_three.grid(row=0, column=0,)
txt = tk.Text(frame_three, bg="white", fg='blue', height=1, width=56)
txt.grid(row=0, column=1, sticky="wes")
button3 = tk.Button(frame_three, text="copy", bg='white', command=copy, width=20, height=1, activeforeground="blue")
button3.grid(row=1, column=1, sticky='w')

button4 = tk.Button(frame_three, text="Quit", bg='white', command=root.destroy, width=20, height=1,
                    activeforeground="red")
button4.grid(row=1, column=1)


root.mainloop()

