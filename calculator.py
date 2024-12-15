import tkinter as tk


w = tk.Tk()
w.title("Calculator")
w.geometry("200x200")

n=[1,2,3,4,5,6,7,8,9,0]
o=["+","-","*","/"]


def obc(x):
    global eq_t
    total = eq_l.get() + str(x)
    eq_l.set(total)
    eq_t = total
def answer():
    try:
        global eq_t
        answer = str(eval(eq_t))

        eq_l.set(answer)
        eq_t = answer 

    except ZeroDivisionError:
        eq_l.set("Error💀")
        
    except SyntaxError:
        eq_l.set("Error💀")




def clear():
    global eq_t
    eq_l.set("")
    eq_t = ""



eq_l = tk.StringVar()

f = tk.Frame(w,
             bg="white"
            ).grid()


e = tk.Label(f,width=30,
             height=5,
borderwidth=1,fg="black",bg="white",
textvariable=eq_l) 
e.grid(row=0,column=0,columnspan=8)			 





b1 = tk.Button(f,text="1",
fg="black",command=lambda :obc(1),)
b1.grid(row=1,column=0)

b2 = tk.Button(f,text="2",
fg="black",command=lambda :obc(2),
textvariable=n[1]			  )
b2.grid(row=1,column=1)


b3 = tk.Button(f,text="3",
fg="black",command=lambda :obc(3),
textvariable=n[2]		)
b3.grid(row=1,column=2)

b4 = tk.Button(f,text="4",
fg="black",command=lambda :obc(4),
textvariable=n[3]		)
b4.grid(row=2,column=0,)

b5 = tk.Button(f,text="5",
fg="black",command=lambda :obc(5),
textvariable=n[4]		)
b5.grid(row=2,column=1)

b6 = tk.Button(f,text="6",command=lambda :obc(6),
textvariable=n[5]		)
b6.grid(row=2,column=2)

b7 = tk.Button(f,text="7",
fg="black",command=lambda :obc(7),
textvariable=n[6]		)
b7.grid(row=3,column=0)

b8 = tk.Button(f,text="8",
fg="black",command=lambda :obc(8),
textvariable=n[7]		)
b8.grid(row=3,column=1)

b9 = tk.Button(f,text="9",
fg="black",command=lambda :obc(9),
textvariable=n[8]		)
b9.grid(row=3,column=2)



bp = tk.Button(f,text="+",
fg="black",command=lambda :obc("+"))
bp.grid(row=1,column=3)

bs = tk.Button(f,text="-",
fg="black",command=lambda :obc("-"))
bs.grid(row=2,column=3)

bm = tk.Button(f,text="×",
fg="black",command=lambda :obc("*"))
bm.grid(row=3,column=3)

bd = tk.Button(f,text="÷",
fg="black",command=lambda :obc("/"))
bd.grid(row=4,column=3)

b0 = tk.Button(f,text="0",
fg="black",command=lambda :obc(0),
textvariable=n[1]		)
b0.grid(row=4,column=0)

BAC = tk.Button(f,text="AC",
fg="black",command=clear)
BAC.grid(row=4,column=1)

Beq = tk.Button(f,text="=",
fg="black",command=answer)
Beq.grid(row=4,column=2)




w.mainloop()
