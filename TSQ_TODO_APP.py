import tkinter as tk
import tkinter.messagebox as mbox

# MAIN WINDOW FRAME
root = tk.Tk()
root.title("TSQ TODO APP")
root.geometry("400x400")
root.configure(bg="#399adb")

#ENTRY PATH
entry=tk.Entry(root,width=25,font=("Arial",14))
entry.grid(row=0,column=0,padx=10,pady=10)

#FUNCTION FOR ENTRY BUTTON
def  add_task():
    task=entry.get()
    if task:
        listbox.insert(tk.END, task)
        last_index =listbox.size() - 1
        listbox.itemconfig(last_index,"",fg="blue")
        entry.delete(0, tk.END)
        save_task()
        mbox.showinfo("Info", f"You entered: {task}")

    elif task == "":
        mbox.showwarning("Warning", "Please enter something — field is empty")
        
    else:
        pass

    
def save_task():
        tasks = listbox.get(0, tk.END)
        print("Saving:", tasks)

#Function for mark as done button
def mark_as_done():
    selected = listbox.curselection()
    if selected:
        task = listbox.get(selected)
        task.endswith("Done")
        listbox.delete(selected)
        listbox.insert(selected, "✓" "|" " "+ task)
    else:
        mbox.showwarning("Warning", "Please select a task to mark as done.")

#Function for Edit Task button
def edit_task():
    selected = listbox.curselection()
    if selected:
        task = listbox.get(selected)
        entry.delete(0, tk.END)
        entry.insert(0, task)
        listbox.delete(selected)
    else:
        mbox.showwarning("Warning", "Please select a task to edit.")

#FUNCTION FOR DELETE AND CLEAR ALL
def delete_task():
    access = listbox.curselection() 
    
    if access:
        
        for i in reversed(access):
            task = listbox.get(i)
            listbox.delete(i)
        entry.delete(0, tk.END)
        entry.insert(0, task)
        mbox.showinfo("Info", f"You delete: {task}")
    else:
        mbox.showwarning("Warning", "Please select a task to delete")


#FUNCTION FOR CLEAR ALL
def clear_task():
    clear = listbox.curselection()
    if clear:
        index= clear[0]
        task = listbox.get(index)
        entry.delete(0, tk.END)
        entry.insert(0, task)
        listbox.selection_clear(0, tk.END)
    else:
        mbox.showwarning("Warning", "Please select a task to clear.")




button=tk.Button(root,text="Add Task",width=10,bg="#2ecc71",fg="#ecf0f1",font=("Arial",10),command=add_task)
button.grid(row=0,column=1,padx=6)

#LISTBOX PATH
listbox = tk.Listbox(root, width=40, height=12, font=("Arial", 12))
listbox.place(x=18, y=60)


#buttons
button1=tk.Button(root, text="Mark as done",bg="blue",fg="white",font=("Arial",10),command=mark_as_done)
button1.place(x=10, y=320)
button2=tk.Button(root, text="Delete",bg="red",fg="white", command=delete_task)
button2.place(x=130, y=320)
button4=tk.Button(root, text="Clear all",bg="orange",fg="white",command=clear_task)
button4.place(x=210, y=320)
button5=tk.Button(root, text="Edit Task",bg="black",fg="white",command=edit_task)
button5.place(x=300, y=320)


root.mainloop()