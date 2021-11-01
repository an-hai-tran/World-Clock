from datetime import datetime
import pytz
import time
from tkinter import *

app = Tk()
app.title("World Clock")
app.geometry("500x250")
app.resizable(0, 0)

def display_clock():
    location = pytz.timezone('America/New_York')
    local_time = datetime.now(location)
    current_time = local_time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    name.config(text="America")

    location = pytz.timezone('Europe/Vienna')
    local_time = datetime.now(location)
    current_time = local_time.strftime("%H:%M:%S")
    clock1.config(text=current_time)
    name1.config(text="Europe")

    location = pytz.timezone('Africa/Cairo')
    local_time = datetime.now(location)
    current_time = local_time.strftime("%H:%M:%S")
    clock2.config(text=current_time)
    name2.config(text="Africa")

    location = pytz.timezone('Australia/Melbourne')
    local_time = datetime.now(location)
    current_time = local_time.strftime("%H:%M:%S")
    clock3.config(text=current_time)
    name3.config(text="Australia")
    clock.after(200,display_clock)

name = Label(app,font=("display_clock",20, 'bold'))
name.place(x=30,y=5)
clock=Label(app,font=("display_clock",25, 'bold'))
clock.place(x=10,y=40)
display = Label(app, text="Hours   Minutes  Seconds", font="display_clock 10 bold")
display.place(x=10,y=80)

name1 = Label(app,font=("display_clock",20, 'bold'))
name1.place(x=330,y=5)
clock1=Label(app,font=("display_clock",25, 'bold'))
clock1.place(x=310,y=40)
display = Label(app, text="Hours   Minutes  Seconds", font="display_clock 10 bold")
display.place(x=310,y=80)

name2 = Label(app,font=("display_clock", 20, 'bold'))
name2.place(x=30,y=105)
clock2=Label(app,font=("display_clock", 25, 'bold'))
clock2.place(x=10,y=140)
display = Label(app, text="Hours   Minutes  Seconds", font="display_clock 10 bold")
display.place(x=10,y=180)

name3 = Label(app,font=("display_clock", 20, 'bold'))
name3.place(x=330,y=105)
clock3=Label(app,font=("display_clock", 25, 'bold'))
clock3.place(x=310,y=140)
display = Label(app, text="Hours   Minutes  Seconds", font="display_clock 10 bold")
display.place(x=310,y=180)

display_clock()
app.mainloop()



