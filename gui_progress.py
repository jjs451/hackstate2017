from tkinter import *
from tkinter import ttk

class App:
    def __init__(self, master):
        def get_input():
            input1, input2 = self.get_matchup_input()
            input1 = self.convert_team(input1)
            input2 = self.convert_team(input2)
            print(input1, input2)

        self.master = master
        frame = Frame(master)
        label = Label(frame, text="College Football\nOutcome Predicter")
        button = Button(frame, text="Matchup", command=get_input)
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
        top = Toplevel()
        msg = Message(top, text=error)
        msg.pack()
        button = Button(top, text="Ok", command=top.destroy)
        button.pack()
        top.wait_window()

    def convert_team(self, name):
        teams = {
        "Alabama": 8,
        "Arkansas": 31,
        "Auburn": 37,
        "Florida": 235,
        "Georgia": 257, 
        "Kentucky": 334, 
        "LSU": 365,
        "Mississippi State": 430, 
        "Missouri": 434,
        "South Carolina": 648, 
        "Tennesee": 694,
        "TSUN": 433, 
        "Texas": 697, 
        "Vanderbilt": 736 }
        return teams[name]


    def get_matchup_input(self):
        Teams = ["Alabama", "Arkansas", "Auburn", "Florida", "Georgia", "Kentucky", "LSU" ,"Mississippi State", "Missouri", "South Carolina", "Tennesee", "TSUN", "Texas", "Vanderbilt" ]
        top = Toplevel()
        top.title = "Pick a Team"
        teampick1 = StringVar()
        teampick2 = StringVar()
        msg = Message(top, text="Please choose 2 teams to match up.")
        msg.pack()
        pick_one = ttk.Combobox(top, textvariable = teampick1, state="readonly")
        pick_one["values"] = Teams
        pick_two = ttk.Combobox(top, textvariable = teampick2, state="readonly")
        pick_two["values"] = Teams
        pick_one.pack(anchor=W)
        pick_two.pack(anchor=W)
        button = Button(top, text="Pick", command=top.destroy)
        button.pack(side=BOTTOM)
        root.wait_window(top)
        if (teampick1.get() == teampick2.get()) or (teampick1.get() == '' or teampick2.get() == ''):
            self.give_error("Please choose valid teams. Both teams must be picked, and both teams cannot be the same team.")
            return self.get_matchup_input()
        return teampick1.get(), teampick2.get()

root = Tk()
root.title("CFB Outcome Predicter")
App(root)
root.wm_geometry(newGeometry="300x300+0+0")

root.mainloop()