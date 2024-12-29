import tkinter as tk

window = tk.Tk()
window.title('CALCULATOR')
window.geometry("440x600")
framemain = tk.Frame(master=window, width=70, height=100, bg="#217DE0") 
framemain.pack(fill=tk.BOTH)

entry = tk.Entry(framemain, width=14, font=("Arial", 40), justify="right")
entry.pack(pady=20)

# Variables to store operations and results
operations = []
numbers = []

# Helper Function to Create Buttons
def create_button(parent, text, command, font=("Arial", 40), width=3, bg="#217DE0", fg="white"):
    return tk.Button(parent, text=text, width=width, font=font, bg=bg, fg=fg, command=command)

# Operation Functions
def add_operation(symbol):
    operations.append(entry.get())
    operations.append(symbol)
    entry.delete(0, "end")

def clear():
    entry.delete(0, "end")
    operations.clear()

def calculate():
    try:
        # Combine operations into a single string
        expression = "".join(operations + [entry.get()])
        result = eval(expression)  # Use eval to compute the result
        entry.delete(0, "end")
        entry.insert(tk.END, str(result))
        operations.clear()
    except Exception as e:
        entry.delete(0, "end")
        entry.insert(tk.END, "Error")
        operations.clear()

# Frames for Layout
frames = [tk.Frame(master=window, width=100, height=100, bg="#217DE0") for _ in range(4)]
for frame in frames:
    frame.pack(fill=tk.BOTH)

# Adding Buttons
clearbutton = tk.Button(framemain, text="C", command=clear, font=("Arial", 17), width=7, bg="#217DE0", activebackground="red", activeforeground="white")
clearbutton.pack(side="right", padx=3, pady=3)

buttons = [
    ("÷", lambda: add_operation("/")), ("9", lambda: entry.insert(tk.END, "9")), ("8", lambda: entry.insert(tk.END, "8")), ("7", lambda: entry.insert(tk.END, "7")),
    ("✕", lambda: add_operation("*")), ("6", lambda: entry.insert(tk.END, "6")), ("5", lambda: entry.insert(tk.END, "5")), ("4", lambda: entry.insert(tk.END, "4")),
    ("-", lambda: add_operation("-")), ("3", lambda: entry.insert(tk.END, "3")), ("2", lambda: entry.insert(tk.END, "2")), ("1", lambda: entry.insert(tk.END, "1")),
    ("+", lambda: add_operation("+")), ("=", calculate), (".", lambda: entry.insert(tk.END, ".")), ("0", lambda: entry.insert(tk.END, "0"))
]

# Arrange Buttons in Frames
button_index = 0
for frame in frames:
    for _ in range(4):  # 4 buttons per row
        text, command = buttons[button_index]
        button = create_button(frame, text, command)
        button.pack(side="right", padx=3, pady=3)
        button_index += 1

window.mainloop()
