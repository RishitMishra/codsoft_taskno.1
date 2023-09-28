from tkinter import *

r = Tk(className="To do list by RM")
r.geometry("450x450")
r.resizable(0,0)
r.config(bg="light blue")

header = Label(r,text="To Do List",font=("arial",20,"bold"),bg="light blue") 
header.pack()

frame2 = Frame(r,bg="light blue")
frame2.pack(pady=20)

l1 = Label(frame2,text="Enter task: ",font=("arial",10),bg="light blue") 
l1.pack(side=LEFT)

task_entry = Entry(frame2,font=("arial",14),width=30)
task_entry.pack(side=RIGHT) 

frame = Frame(r)
frame.pack(pady=10)

task_box = Listbox(frame,width=28,height=8,font=("arial",18))
task_box.pack(side=LEFT,fill=BOTH)

scroll = Scrollbar(frame)
scroll.pack(side=RIGHT,fill=BOTH)

frame1 = Frame(r)
frame1.pack(pady=20)

submit_button = Button(frame1,text="Submit",command=lambda:task_box.insert(END,task_entry.get()),width=8,height=8,font=("arial",16))
submit_button.pack(side=LEFT,fill=BOTH)

delete_button = Button(frame1,text="Delete",command=lambda:task_box.delete("anchor"),font=("arial",16),width=8,height=8)
delete_button.pack(side=LEFT,fill=BOTH)

deleteall_button = Button(frame1,text="Delete all",command=lambda:task_box.delete(0,END),font=("arial",16),width=8,height=8)
deleteall_button.pack(side=RIGHT,fill=BOTH)

task_box.config(yscrollcommand=scroll.set)
scroll.config(command=task_box.yview)

r.mainloop()