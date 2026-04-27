from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(0,0)

# Entry box 
e1 = Entry(root,font=("Arial",18),borderwidth=5,justify="right")
e1.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

# main function for calculation
def calc(value):
        current = e1.get()
    
        if value == "=":
            try:
                result = eval(e1.get())
                e1.delete(0,END)
                e1.insert(END,str(result))
            except:
                e1.delete(0,END)
                e1.insert(END,"Value Error")

        elif value == "C":
            e1.delete(0,END)
        else:
            if current == "0":
                 e1.delete(0,END)
            e1.insert(END,value)

# Buttons
buttons = [

    ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("+",3,3),
    ("0",4,0),(".",4,1),("-",4,2),("=",4,3),
    ("C",5,0)
]
for (text,r,c) in buttons:
    Button(root,text=text,width=8,height=3,font=("",10,"bold"),command=lambda t=text:calc(t)).grid(row=r,column=c,pady=4)


















root.mainloop()
