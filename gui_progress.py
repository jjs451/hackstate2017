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
        center(master)
        label = Label(master, text="College Football Outcome Predicter")
        button = Button(master, text="Matchup", command=get_input)
        button_last = Button(master, text="Quit", command=self.quit)
        label.grid(row=0, column=0)
        button.grid(row=1, column=0)
        button_last.grid(row=2, column=0)

    def quit(self):
        top = Toplevel()
        center(top)
        top.title = "Confirmation"
        msg = Label(top, text="Are you sure you want to quit?")
        msg.grid(column=0, row=0, columnspan=2)
        button_yes = Button(top, text="Yes", command=self.master.destroy)
        button_yes.grid(column=0, row=1)
        button_no = Button(top, text="No", command=top.destroy)
        button_no.grid(column=1, row=1)

    def give_error(self, error):
        top = Toplevel()
        center(top)
        msg = Message(top, text=error)
        msg.grid(row=0, column=0, rowspan=2)
        button = Button(top, text="Ok", command=top.destroy)
        button.grid(row=2, column=0)
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
        center(top)
        top.title = "Pick a Team"
        teampick1 = StringVar()
        teampick2 = StringVar()
        Label(top, text="Please choose 2 teams to match up.").grid(column=0, row=0, columnspan=2)
        Label(top, text="First Team").grid(row=1, column=0)
        Label(top, text="First Team").grid(row=2, column=0)
        pick_one = ttk.Combobox(top, textvariable = teampick1, state="readonly")
        pick_one["values"] = Teams
        pick_two = ttk.Combobox(top, textvariable = teampick2, state="readonly")
        pick_two["values"] = Teams
        pick_one.grid(column=1, row=1)
        pick_two.grid(column=1, row=2)
        button = Button(top, text="Pick", command=top.destroy)
        button.grid(column=0, row=3, columnspan=2)
        root.wait_window(top)
        if (teampick1.get() == teampick2.get()) or (teampick1.get() == '' or teampick2.get() == ''):
            self.give_error("Please choose valid teams. Both teams must be picked, and both teams cannot be the same team.")
            return self.get_matchup_input()
        return teampick1.get(), teampick2.get()

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

root = Tk()
root.title("CFB Outcome Predicter")
App(root)

root.mainloop()