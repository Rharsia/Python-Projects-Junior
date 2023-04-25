import tkinter as tk

root = tk.Tk()

# set the window to desired size
root.geometry("500x500")

# set the title
root.title("(not) My First GUI")

# Label
label = tk.Label(root, text="Hello World!", font=("Ariel", 18))
# Padding of the label
label.pack(padx=20,pady=20)

# Textbox
textbox = tk.Text(root, height=3, font=("Arial", 16))
textbox.pack(padx=10, pady=10)

# Entrybox
# myentry = tk.Entry(root)
# myentry.pack()

# Button
# button = tk.Button(root, text="Click Me!", font=("Arial", 18))
# button.pack(padx=10, pady=10)

# Button frame for 3 columns
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

# buttons
btn1 = tk.Button(buttonframe, text="1", font=("Arial", 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=("Arial", 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=("Arial", 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font=("Arial", 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", font=("Arial", 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6", font=("Arial", 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

# add the buttonframe to the window and stretch to x dimension
buttonframe.pack(fill="x")

# manually place the button
anotherbtn = tk.Button(root, text="TEST")
anotherbtn.place(x=200, y=200, height=100, width=100)

root.mainloop()