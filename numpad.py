import tkinter
from tkinter import *

btn_list = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3', '0']

my_value = ''


class NumPad(tkinter.simpledialog.Dialog):
    def body(self, root):
        frame1 = tkinter.Frame(root, relief="sunken", borderwidth=5)
        entry = tkinter.Entry(frame1)
        frame1.grid(row=0, column=0, columnspan=3)
        entry.pack()

        r = 1
        c = 0
        for b in btn_list:
            # if r > 3 :
            #     btn= tkinter.Button(root, text=b,width=3,command=lambda m=b: self.onNum(entry, m))
            #     btn.grid(row=r,column=0, columnspan=3)
            # else:
            #     print(int(b))
            #     btn= tkinter.Button(root, text=b,width=3,command=lambda m=b: self.onNum(entry, m))
            #     btn.grid(row=r,column=c)
            print(int(b))
            btn = tkinter.Button(root, text=b, width=3, command=lambda m=b: self.onNum(entry, m))
            btn.grid(row=r, column=c)
            # print(b)
            c += 1
            if c > 2:
                c = 0
                r += 1
        enter = tkinter.Button(root, text="Enter", width=3, command=lambda: self.onEnter(root, entry))
        enter.grid(row=r, column=c, columnspan=2, sticky="nesw", padx=3, pady=2)

    def onNum(self, entry, btn):
        entry.insert(len(entry.get()), btn)

    # override method ok from simpledialog to link this method to enter button
    def onEnter(self, root, entry):
        self.ok(root, entry)

    def ok(self, root, entry):
        if not self.validate():
            self.initial_focus.focus_set()  # put focus back
            return
        self.withdraw()
        self.update_idletasks()
        self.apply(root, entry)
        self.cancel()

    # override method buttonbox from simpleDialog so nothing is created
    def buttonbox(self):
        pass

    def apply(self, root, entry):
        global my_value
        my_value = entry.get()
        entry.delete(0, 'end')