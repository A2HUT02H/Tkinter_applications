import tkinter as tk
from tkinter import PhotoImage

window = tk.Tk()
window.title('CALCULATOR')
window.geometry("440x600")
icon = PhotoImage(file=r"Tkinter calculator\Calculator_512.png")
window.iconphoto(False,icon)
framemain = tk.Frame(master=window,width=70,height=100,bg="#217DE0") 
framemain.pack(fill=tk.BOTH)

entry = tk.Entry(framemain,width=14,font=("Arial",40),justify="right")
entry.pack(pady=20)

frame1 = tk.Frame(master=window,width=100, height=100, bg="#217DE0") 
frame1.pack(fill=tk.BOTH)

operations =[]


def div():
    operations.append(entry.get())
    operations.append("/")
    entry.delete(0,"end")

hist = tk.Menubutton(framemain,text="",font=("",19),foreground="white",background="#217DE0")
hist.pack(side="left")

clearbutton = tk.Button(framemain, text="C", width=7, justify="right",font=("Arial", 17),bg="#217DE0", fg="white",activebackground="red",activeforeground="white", command=lambda: (entry.delete(0,"end"),(operations.clear())))  # divide
clearbutton.pack(side="right", padx=3, pady=3)

divbutton = tk.Button(frame1, text="÷", width=3, font=("Arial", 40),bg="orange", fg="white", command=div)  # divide
divbutton.pack(side="right", padx=3, pady=3)

ninebutton = tk.Button(frame1, text="9", width=3, font=("Arial", 40),bg="#217DE0", fg="white",command=lambda:entry.insert(tk.END, "9"))    #9
ninebutton.pack(side="right", padx=3, pady=3)

eightbutton = tk.Button(frame1, text="8", width=3, font=("Arial", 40),bg="#217DE0", fg="white",command=lambda: entry.insert(tk.END, "8"))   #8
eightbutton.pack(side="right", padx=3, pady=3)

    
sevenbutton = tk.Button(frame1, text="7", width=3, font=("Arial", 40), bg="#217DE0", fg="white",command=lambda: entry.insert(tk.END, "7"))   #7
sevenbutton.pack(side="right", padx=3, pady=3)

frame2 = tk.Frame(master=window, width=100, height=100, bg="#217DE0") 
frame2.pack(fill=tk.BOTH)
def multi():
    operations.append(entry.get())
    operations.append("*")
    entry.delete(0,"end")
    

multibutton = tk.Button(frame2, text="✕", width=3, bg="orange", fg="white",font=("Arial", 40), command=multi)    #multiply
multibutton.pack(side="right", padx=3, pady=3)
sixbutton = tk.Button(frame2, text="6", width=3, bg="#217DE0", fg="white",font=("Arial", 40), command=lambda: entry.insert(tk.END, "6"))      #6
sixbutton.pack(side="right", padx=3, pady=3)
fivebutton = tk.Button(frame2, text="5", width=3, bg="#217DE0", fg="white",font=("Arial", 40), command=lambda: entry.insert(tk.END, "5"))     #5
fivebutton.pack(side="right", padx=3, pady=3)
fourbutton = tk.Button(frame2, text="4", width=3,bg="#217DE0", fg="white", font=("Arial", 40), command=lambda: entry.insert(tk.END, "4"))      #4
fourbutton.pack(side="right", padx=3, pady=3)

frame3 = tk.Frame(master=window, width=100, height=100, bg="#217DE0") 
frame3.pack(fill=tk.BOTH)
def minus():
    operations.append(entry.get())
    operations.append("-")
    entry.delete(0,"end")


minusbutton = tk.Button(frame3, text="-", width=3,bg="orange", fg="white", font=("Arial", 40), command=minus)    #subtract
minusbutton.pack(side="right", padx=3, pady=3)
threebutton = tk.Button(frame3, text="3", width=3, bg="#217DE0", fg="white",font=("Arial", 40), command=lambda: entry.insert(tk.END, "3"))    #3
threebutton.pack(side="right", padx=3, pady=3)
twobutton = tk.Button(frame3, text="2", width=3, bg="#217DE0", fg="white",font=("Arial", 40), command=lambda: entry.insert(tk.END, "2"))      #2
twobutton.pack(side="right", padx=3, pady=3)
onebutton = tk.Button(frame3, text="1", width=3,bg="#217DE0", fg="white", font=("Arial", 40), command=lambda: ((entry.delete(0,"end"), (entry.insert(tk.END, "1") ) )) )      #1
onebutton.pack(side="right", padx=3, pady=3)


frame4 = tk.Frame(master=window, width=100, height=100, bg="#217DE0") 
frame4.pack(fill=tk.BOTH)

def plus():
    operations.append(entry.get())
    operations.append("+")
    entry.delete(0,"end")

plusbutton = tk.Button(frame4, text="+", width=3,bg="orange", fg="white",font=("Arial", 40), command=plus)    #add
plusbutton.pack(side="right", padx=3, pady=3)



def ans():
    lost =""
    operations.append(entry.get())
    for i in range(len(operations)):
     lost  += operations[i]
    if operations[-1]in ["","/","*","+","-"] or "ERROR" in operations:
     print(operations)
     entry.delete(0,"end")
     entry.insert(tk.END,"ERROR")
    else:
     print(operations)
     final_ans = eval(lost)
     entry.delete(0,"end")
     entry.insert(tk.END,final_ans)
     operations.clear()
     equation = lost.replace("*", "×").replace("/", "÷")
     print(equation)
     hist.config(text=equation)
     print(">",final_ans)
   
    
   
           

isequalbutton = tk.Button(frame4, text="=", width=3,bg="light green", activebackground="green",fg="green", font=("Arial", 40),command=ans)  #equal
isequalbutton.pack(side="right", padx=3, pady=3)
dotbutton = tk.Button(frame4, text=".", width=3, bg="#217DE0", fg="white",font=("Arial", 40), command=lambda: entry.insert(tk.END, "."))      # .
dotbutton.pack(side="right", padx=3, pady=3)
zerobutton = tk.Button(frame4, text="0", width=3, bg="#217DE0", fg="white",font=("Arial", 40), command=lambda: entry.insert(tk.END, "0"))      #0
zerobutton.pack(side="right", padx=3, pady=3)



window.mainloop()