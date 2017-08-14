from tkinter import *
from tkinter import font
import tkinter.simpledialog
import numpad
import time

txt1 = ''
blink_clicked = False
# tag:GPIO import RPi.GPIO as GPIO

# tag:GPIO GPIO.setmode(GPIO.BOARD)
# tag:GPIO GPIO.setup(40, GPIO.OUT)
# tag:GPIO GPIO.output(40, GPIO.LOW)

class Main_gui:
    def __init__(self, win):
        self.win = win

        self.myFontL = font.Font(family='Helvetica', size=12, weight='bold')
        self.myFontM = font.Font(family='Helvetica', size=16, weight='bold')

        # create top frame
        frame2 = Frame(win, bg="green")
        frame2.pack(fill=BOTH, expand=True, padx=5, pady=5)
        # create bottom frame
        frame = Frame(win, relief=RAISED, borderwidth=2, bg="blue")
        frame.pack(fill=X, padx=5, pady=5, anchor=S)

        self.exitButton = Button(frame,
                                 text="Exit", font=self.myFontM,
                                 command=self.exitProgram,
                                 padx=20, pady=10)
        self.exitButton.pack(side=BOTTOM, fill=X, expand=True, padx=5, pady=0)

        self.blinkButton = Button(frame2,
                                  text="BLINK", font=self.myFontL,
                                  command=self.startBlink,
                                  width=3, padx=20, pady=10)
        self.blinkButton.grid(row=1, column=0, padx=5, pady=0)

        global txt1
        txt1 = StringVar()
        txt1.set(0)
        self.lbl1 = Label(frame2, textvariable=txt1, width=3,
                          font=self.myFontL, fg="darkblue",
                          borderwidth=5, relief="sunken")
        self.lbl1.grid(row=1, column=1, padx=5, pady=0)
        self.lbl1.bind("<Button-1>", self.onMouseLclick)

        self.cb_var = IntVar()
        # self.cb_var = False
        c = Checkbutton(frame2,
                        text="LED 1",
                        variable=self.cb_var,
                        command=lambda: self.cb(self.cb_var),
                        font=self.myFontL)
        c.grid(row=1, column=3, padx=5, pady=0)

    def cb(self, cb_status):
        print("cb status is ", cb_status)
        self.ledToggle()

    def onMouseLclick(self, event):
        global txt1
        print(event.widget)
        numpad.NumPad(self.win)
        this_value = numpad.my_value
        txt1.set(this_value)

    def ledToggle(self, pin=[0]):
        pin[0] = not pin[0]
        print("LED button pressed ", pin)
        # tag:GPIO 	if GPIO.input(40) :
        if not pin[0]:
            # tag:GPIO  		GPIO.output(40,GPIO.LOW)
            # todo: check if this is OK
            self.blinkButton.config(relief=RAISED)
            self.cb_var.set(0)
        # tag:GPIO 	else:
        else:
            # tag:GPIO 		GPIO.output(40,GPIO.HIGH)
            self.blinkButton.config(relief=SUNKEN)
            self.cb_var.set(1)
            print("cb_var is, ", self.cb_var.get())

    def startBlink(self):
        if int(txt1.get())>0:
            global blink_clicked
            blink_clicked = True
            self.blink()

    def blink(self, toggle_flag=[0]):
        # read number of blinks from the label
        global txt1, blink_clicked
        if blink_clicked==True:
            nr = int(txt1.get())
            toggle_flag[0] = not toggle_flag[0]
            self.ledToggle()
            time.sleep(0.5)
            nr -=1
            print("here 1, ", nr)
            after_id = tk.after(50, self.blink)
            if not toggle_flag[0] and nr >= 0:
                txt1.set(nr)
                if nr == 0:
                    blink_clicked = False
                    self.blinkButton.config(relief=RAISED)
                    self.cb_var.set(0)
                    tk.after_cancel(after_id)



    def exitProgram(self):
        print("Exit Button pressed")
        # tag:GPIO         GPIO.cleanup()
        tk.quit()


if __name__ == "__main__":
    tk = Tk()
    tk.title("First GUI")
    tk.geometry('640x480')
    app = Main_gui(tk)
    # tk.after(10, Main_gui.blink)
    tk.mainloop()
