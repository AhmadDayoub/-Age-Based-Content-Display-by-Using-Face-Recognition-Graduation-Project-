from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import *
import subprocess
from PIL import Image, ImageTk


def run_script():
    # Call bar function to show the progress bar
    bar()

    # Define the path to the Python script you want to run
    script_path = r"realtime_demo.py"

    # Use subprocess to run the script
    subprocess.call(["python", script_path])

    # Close the splash screen after the script has finished executing
    close_splash(None)


def close_splash(event):
    w.destroy()


w = Tk()

# Set the size and position of the window
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

# Remove the window border
w.overrideredirect(1)

# Set the background image of the window
# Load the image using PIL and resize it to fit the window
image = Image.open("7.png")
image = image.resize((width_of_window, height_of_window), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image)

# Set the background image of the window
background_label = Label(w, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# Set the style and color of the progress bar
s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#357EC7')
progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)


def bar():
    import time
    r=0
    for i in range(100):
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.03)
        r=r+1

    w.update()

# Set the position of the progress bar
progress.place(x=-10,y=235)

# Add a "Run Script" button that will execute the bar() function from another Python script when clicked
a='white'
run_script_button = Button(w,width=10,height=1,text='START',command=run_script,border=0,fg=a,bg='#357EC7')
run_script_button.place(x=300,y=200)


# Bind the ESC key to the close_splash function
w.bind('<Escape>', close_splash)

w.mainloop()