from tkinter import *
from tkinter import ttk

class App:
    def __init__(self, master):
        self.master = master
        frame = Frame(master)
        label = Label(frame, text="College Football\nOutcome Predicter")
        button = Button(frame, text="Matchup", command=self.get_matchup_input)
        button_last = Button(frame, text="Quit", command=self.quit)
        frame.pack()
        label.pack()
        button.pack()
        button_last.pack()

    def quit(self):
        top = Toplevel()
        top.title = "Confirmation"
        msg = Message(top, text="Are you sure you want to quit?")
        msg.pack()
        button_yes = Button(top, text="Yes", command=self.master.destroy)
        button_yes.pack()
        button_no = Button(top, text="No", command=top.destroy)
        button_no.pack()

    def give_error(self, error):
        pass

    def get_matchup_input(self):
        Teams = ["MSSTATE", "LSU"]
        top = Toplevel()
        top.title = "Pick a Team"
        teampick1 = StringVar()
        teampick2 = StringVar()
        msg = Message(top, text="Please choose a team.")
        msg.pack()
        pick_one = ttk.Combobox(top, textvariable = teampick1, state="readonly")
        pick_one["values"] = Teams
        pick_two = ttk.Combobox(top, textvariable = teampick2, state="readonly")
        pick_two["values"] = Teams
        pick_one.pack(anchor=W)
        pick_two.pack(anchor=W)
        button = Button(top, text="Pick", command=top.destroy)
        button.pack(side=BOTTOM)

root = Tk()
root.title("CFB Outcome Predicter")
App(root)
root.wm_geometry(newGeometry="300x300+0+0")

root.mainloop()