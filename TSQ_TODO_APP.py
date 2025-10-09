import tkinter as tk


# MAIN WINDOW FRAME
root = tk.Tk()
root.title("TSQ TODO APP")
root.geometry("400x400")
root.configure(bg="#399adb")

#listbox
listbox = tk.Listbox(root, width=30, height=10, font=("Arial", 12))
listbox.pack(pady=70)

#buttons
button1=tk.Button(root, text="Mark as done")
button1.place(x=50, y=320)
button2=tk.Button(root, text="Delete")
button2.place(x=170, y=320)
button3=tk.Button(root, text="Add")
button3.place(x=260, y=20)
button4=tk.Button(root, text="Clear All")
button4.place(x=250, y=320)

root.mainloop()