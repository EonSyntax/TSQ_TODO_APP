import tkinter as tk


# MAIN WINDOW FRAME
root = tk.Tk()
root.title("TSQ TODO APP")
root.geometry("400x400")
root.configure(bg="#399adb")

#ENTRY PATH
entry=tk.Entry(root,width=25,font=("Arial",14))
entry.grid(row=0,column=0,padx=10,pady=10)

button=tk.Button(root,text="Add Task",width=10,bg="#2ecc71",fg="#ecf0f1",font=("Arial",10))
button.grid(row=0,column=1,padx=6)


#LISTBOX PATH
listbox = tk.Listbox(root, width=40, height=12, font=("Arial", 12))
listbox.place(x=18, y=60)

root.mainloop()