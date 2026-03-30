from tkinter import *
window=Tk()
window.title("intoroduction to Tkinter")
window.geometry("300x300")

greeting=Label(text="Hello User", fg="black", bg="white")
button=Button(text="click me", bg="black", fg="white")
entry=Entry(fg="pink", bg="blue")
greeting.pack()
button.pack()
entry.pack()

frame=Frame(master=window,relief=RAISED,borderwidth=5)
frame.pack()
label=Label(master=frame,text="sample Frame")

text_box=Text(fg="green", bg="pink")
text_box.pack()
window.mainloop()