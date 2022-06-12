from cgitb import text
import tkinter as tk
from tkinter import ANCHOR, PhotoImage, ttk
from ctypes import windll
from tkinter.messagebox import showinfo
import time
import tkinter.font as font



# Makes text not blurry
windll.shcore.SetProcessDpiAwareness(1)


# Opens a 'main' / 'root' window
root = tk.Tk()
root.configure(bg='#181A1D')

# Font
myFont = font.Font(family='Small Fonts', size=15)


# Progress
def progress_label():
    return f"Current Progress: {bar['value']}%"


# Creates a progress bar
bar = ttk.Progressbar(root, orient='horizontal', length=400, mode='determinate')
bar.place(relx=0.5, rely=0.75, anchor='center')

# Progress label
value_label = tk.Label(root, text=progress_label(),fg='#ffffff', bg='#181A1D',font=myFont)
value_label.place(relx=0.5, rely=0.6, anchor='center')

# Enter name
name_label = tk.Label(root, text='Enter your name here:', fg='#ffffff', bg='#181A1D', font=myFont)
name_label.place(relx=0.5, rely=0.1, anchor='center')
text = tk.StringVar()
textbox = tk.Entry(root, textvariable=text, font=myFont, fg='#ffffff', bg='#181A1D')
textbox.place(relx=0.5, rely=0.25, anchor='center')

def progress(): 
    for i in range(100):
        root.update_idletasks()
        bar['value'] += 1
        value_label['text'] = progress_label()
        time.sleep(.05)
    if text.get().lower() == 'eli':
        name_label.destroy()
        start_button.destroy()
        textbox.destroy()
        bar.destroy()
        value_label.destroy()
        newFont = font.Font(family='Small Fonts', size=35, weight='bold')
        tk.Label(root, text='You ARE a melon!', font=newFont, fg='#ffffff', bg='#181A1D').place(relx=0.5, rely=0.5, anchor='center')
    else:
        name_label.destroy()
        start_button.destroy()
        textbox.destroy()
        bar.destroy()
        value_label.destroy()
        newFont = font.Font(family='Small Fonts', size=35, weight='bold')
        tk.Label(root, text='You are NOT a melon!', font=newFont, fg='#ffffff', bg='#181A1D').place(relx=0.5, rely=0.5, anchor='center')


# Start the progress bar
start_button = tk.Button(root, text='Begin Melon Check', fg='#ffffff', bg='#181A1D',command=progress)
start_button['font'] = myFont
start_button.place(relx=0.5, rely=0.45, anchor='center')


# Creates a title for the window
root.title('Melon Dectection System')

window_width = 800
window_height = 400

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Changes icon of window > requires .ico file
root.iconbitmap('./icon.ico')
# Keeps the window open until closed manually
root.mainloop()
