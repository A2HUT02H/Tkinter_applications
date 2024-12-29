import tkinter as tk
from tkinter import PhotoImage , messagebox,ttk


window = tk.Tk()
window.title('Python Window 🌐')
window.geometry("880x380")
icon = PhotoImage(file=r"print window\electric.png")
window.iconphoto(False,icon)
framemain = tk.Frame(master=window,width=100,height=100,bg="Indian red")  
closebutton =tk.Button(framemain,text="CLOSE❌",font=("Segoe UI",15,"bold"),
                       command=window.destroy,
                       relief="raised",
                       fg="red",
                       bg="white",
                       width=7,
                       activeforeground="white",
                       activebackground="red")
closebutton.pack(side="right",padx=10,pady=15,)
lbl1 = tk.Label(framemain,text="NAME PRINTER",font=("ShoraiSansStdN-Black", 24),bg= "Indian red",padx=30,pady=10).pack()
framemain.pack(fill=tk.BOTH)


namefrm = tk.Frame(width=100,height=100,bg="gold")
namefrm.pack(fill=tk.BOTH)

frame2 = tk.Frame(width=50,height=30,bg="gold",pady=4)
frame2.pack(fill=tk.BOTH)

frame22 = tk.Frame(window,width=50,bg="gold",pady=4)
frame22.pack(fill=tk.BOTH)

frame3 = tk.Frame(width=25,height=25,bg="gold") 
frame3.pack(fill=tk.BOTH) 
optionlable = tk.Label(frame2,text="Profesion:",font=("Arial",12),bg="gold").pack(side="left")
optionlist = ttk.Combobox(frame2,values=["Student","Teacher","Worker","Carpenter"])
optionlist.set("--------(No options selected)--------")
optionlist.config(font=("Arial", 12),width=25)

optionlist.pack(side="left",padx=10)
optionclr = tk.Button(frame2,text="❌",font=("Arial",10),bg="light blue",activebackground="blue",command=lambda: optionlist.set("--------(No options selected)--------")).pack(side="left",padx=5)

agelable = tk.Label(frame22,text="Age:",font=("Arial",12),bg="gold").pack(side="left")
agelist = ttk.Combobox(frame22,font=("Arial",12),width=3)
agelist.pack(side="left",pady=8,padx=10)
ages =[]
for a in range(8,50):
 ages.append(a)
print(ages)
 
agelist['values'] = ages



enternamelbl = tk.Label(namefrm,text="Enter name:",font=("Arial",12),bg="gold").pack(side="left")
entername = tk.Entry(master=namefrm,font=("Minecraft Regular",12),
                 bg="lightyellow",          
                 fg="black",             
                 insertbackground="red",   
                 selectbackground="red", 
                 selectforeground="white",width=50)
                

def printname():
 name = entername.get()
 print(f"Name:- {name}")
 messagebox.showinfo("Success!", "Your text has been printed!")
 entername.delete(0,'end')
 if messagebox.askyesno("Continue","Do you want to continue?")!=True:
   window.destroy()
 entername.delete(0,"end")
def clear():
 entername.delete(0,"end")
 



entername.pack(side="left",padx=6)

clrnamebutton = tk.Button(master=namefrm,font=("Arial",10,"italic"),text="Clear text",bg="light blue",activebackground="blue",command=clear)
clrnamebutton.pack(side="left",padx=5)

namebutton = tk.Button(master=namefrm,font=("Segoe UI",10,"bold"),text="Print Name",bg="light green",activebackground="green",command=printname)
namebutton.pack(side="left",pady=10)

def saveme():
 name = entername.get()
 prof = optionlist.get()
 age = agelist.get()
 data = f"Name: {name} \nProfession: {prof} \nAge: {age}" 
 if messagebox.askyesno("Save","Do you want to save?")==True:
    if name == "" and prof == "--------(No options selected)--------" and age == "":
     print("No data to save!")
     optionlist.set("--------(No options selected)--------")
    elif entername.get() == "" and optionlist.get() != "--------(No options selected)--------":
     print(f"Profession: {optionlist.get()}")
     optionlist.set("--------(No options selected)--------")
    elif entername.get()!= "" and optionlist.get() == "--------(No options selected)--------":
     print(f"Name: {entername.get()}") 
     optionlist.set("--------(No options selected)--------")
    else:
     print(data)
     entername.delete(0,"end")
     optionlist.delete(0,"end")
     optionlist.set("--------(No options selected)--------")
     filecreate = open("data.txt","w")
     filecreate.write(data)
 else:
     window.destroy()



savebutton = tk.Button(frame3,text="Save",font=("Arial",16,"bold"),bg="light blue",activebackground="blue",command=saveme).pack(pady=15)


#menus
mainmenu = tk.Menu(window)
edit_menu = tk.Menu(mainmenu,tearoff=0)
file_menu = tk.Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="File",menu=file_menu)
mainmenu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Edit")
file_menu.add_command(label="error")
file_menu.add_separator()

file_menu.add_command(label="Exit",command=window.destroy)


window.config(menu=mainmenu)



window.mainloop()
