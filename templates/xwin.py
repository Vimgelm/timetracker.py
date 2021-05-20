from tkinter import *

window = Tk()
window.title("time_tracker")
window.geometry('400x500')
window["bg"] = "grey25"

#строка
lbl = Label(window, text="Привет")
lbl.grid(column=0, row=0)
#кнопка
btn = Button(window, text="Не нажимать!")
btn.grid(column=0, row=1)

window.mainloop()