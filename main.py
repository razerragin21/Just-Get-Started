import tkinter
from tkinter import *
from playsound import playsound

#window configuration
root=Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)
root.configure(background = '#333333')

task_list = []

#function to add tasks to list
def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert( END,  task)

#functions for sfx
def completetasksfx():
    playsound('sfx/complete.mp3', False)

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






# image for application

Image_icon = PhotoImage(file="Image/task.png")
root.iconphoto(False, Image_icon)

# image for top bar
TopImage=PhotoImage(file="Image/topbar.png")
Label(root, image=TopImage, background = '#333333').pack()

# image for dock
dockImage=PhotoImage(file="Image/dock.png")
Label(root, image=dockImage, bg="#32405b").place(x=30, y=25)

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



#list box
frame1 = Frame(root, bd=3, width = 700, height = 280, bg = "#333333")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font = ("gadugi", 12), width=40, height=16, bg="#1E1E1E", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill = BOTH, padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side = RIGHT, fill = BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


openTaskFile()


# delete

Delete_icon = PhotoImage(file="Image/delete.png")
Button(root, image = Delete_icon, fg = '#333333', bg = '#333333', activebackground = '#333333', bd = 0, command = lambda:[deleteTask(), completetasksfx()]).pack(side = BOTTOM, pady = 13)




root.mainloop()
