import tkinter
from tkinter import *
from playsound import playsound
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk


#window configuration
root=Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)
root.configure(background = '#333333')

# Intialise the task list array
task_list = []


# pystray minimise to tray

# Define a function for quit the window
# This is for the system tray area
# This is referenced further down in the code
def quit_window(icon, item):
   icon.stop()
   root.destroy()

# Define a function to show the window again 
# This is the system tray area
# This is referenced down further in the code
def show_window(icon, item):
   icon.stop()
   root.after(0,root.deiconify())
   root.lift()
   root.attributes('-topmost',True)

# Hide the window and show on the system taskbar
def hide_window():
   root.withdraw()
   image=Image.open("Image/task.png")
   menu=(item('Quit', quit_window), item('Show', show_window))
   icon=pystray.Icon("name", image, "My System Tray Icon", menu)
   icon.run()

# destroys application, creates a system tray icon and is fed Quit, and Show when right clicked
def show_icon():
    root.withdraw()
    image=Image.open("Image/task.png")
    menu=(item('Quit', quit_window), item('Show', show_window))
    icon=pystray.Icon("name", image, "My System Tray Icon", menu)
    icon.run()

# runs the show icon function, when windows application is closed
root.protocol('WM_DELETE_WINDOW', show_icon)




#function to add tasks to list
def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert( END,  task)

# Play complete task SFX using playsound (windows compatible only)
def completetasksfx():
    playsound('sfx/complete.mp3', False)

# Play sound when task ADD using playsound (windows compatible only)
def addtasksfx():
    playsound('sfx/add.mp3', False)

#function to remove tasks from list
def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

        listbox.delete( ANCHOR)

#function to read the taskfile adn display the list of tasks
def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != "\n":
                task_list.append(task)
                listbox.insert(END, task)

    except:
        file = open("tasklist.txt", "w")
        file.close()




# -------------------------------------------------------------------------------------------------
# UI

# image for application

Image_icon = PhotoImage(file="Image/task.png")
root.iconphoto(False, Image_icon)

# image for top bar
TopImage=PhotoImage(file="Image/topbar.png")
Label(root, image=TopImage, background = '#333333').pack()

# image for dock
dockImage=PhotoImage(file="Image/dock.png")


# image for tasks
noteImage = PhotoImage(file="image/task.png")
Label(root, image=noteImage, bg="#32405b").place(x=340, y=19)

heading = Label(root, text="To Do", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=160, y=20)


# main

frame = Frame(root, width=400, height=50, bg="#252526")
frame.place(x=0, y=180)

task = StringVar()
task_entry = Entry(frame, width = 18, font="cascadia 20 ", bd=0, bg = '#464646', fg = 'white')
task_entry.place(x=10, y=7)
task_entry.focus()



button = Button(frame, text="ADD", font="Helvetica 20", width = 6, bg = "#1E1E1E", fg="#2F89FF", activebackground = '#2F89FF', activeforeground ='#FFFFFF', bd = 0, command= lambda:([addTask(), addtasksfx()]))
button.place(x = 300, y = 0)
# Enter button allows for same functionality as add button
root.bind_all("<Return>", lambda event: button.invoke())



#list box
frame1 = Frame(root, bd=3, width = 700, height = 280, bg = "#333333")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font = ("gadugi", 12), width=40, height=16, bg="#1E1E1E", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill = BOTH, padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side = RIGHT, fill = BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)




# Create a button
button = tkinter.Button(root, text="Menu", image = dockImage, highlightbackground="#32405B", background="#32405B", borderwidth=0)

# Create a label to display the white box

label = tkinter.Label(root, text = "drop down", bg="#23262E", borderwidth=1)

# Define a function that animates the white box
def animate_box(event):
    if label.winfo_ismapped():
        label.place_forget()
    else:
        label.place(x=0, y=0, width=200, height=650)
        label.lift()


# Bind the function to the button's click event
button.bind("<Button-1>", animate_box)

# Place the button in the top left corner of the screen
button.place(x=30, y=25)

# Create a delete button and set the sticky attribute to "ew"
delete_button = tkinter.Button(label, text="Delete", width = 200, height = 1)

# Define a function that deletes the label
def delete_label(event):
    label.place_forget()

# Bind the delete function to the delete button's click event
delete_button.bind("<Button-1>", delete_label)

# Place the delete button on the label
delete_button.place(x=0, y=0)



# UI
# -------------------------------------------------------------------------------------------------


openTaskFile()


# delete

Delete_icon = PhotoImage(file="Image/delete.png")
Button(root, image = Delete_icon, fg = '#333333', bg = '#333333', activebackground = '#333333', bd = 0, command = lambda:[deleteTask(), completetasksfx()]).pack(side = BOTTOM, pady = 13)






root.mainloop()
