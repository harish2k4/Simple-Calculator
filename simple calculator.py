from tkinter import *

root=Tk()
root.title("SIMPLE CALCULATOR")



my_entry=Entry(root,width=30,borderwidth=5)

my_entry.grid(row=0,column=0,columnspan=4)


def myclick(number):
    current=my_entry.get()
    my_entry.delete(0,END)
    my_entry.insert(0,str(current)+str(number))


def myclear():
    my_entry.delete(0,END)

def myadd():
    global fnum
    global case
    case="addition"
    firstnumber=my_entry.get()
    fnum=int(firstnumber)
    my_entry.delete(0,END)
   
   
    
def myequal():
    secondnumber=my_entry.get()
    my_entry.delete(0,END)
    if case == "addition":
         my_entry.insert(0,fnum+int(secondnumber))
    if case == "subraction":
        my_entry.insert(0,fnum-int(secondnumber))
    if case == "division":
        my_entry.insert(0,fnum/int(secondnumber))
    if case == "multiplication":
        my_entry.insert(0,fnum*int(secondnumber))

def mysub():
    global fnum
    global case
    case="subraction"
    firstnumber=my_entry.get()
    fnum=int(firstnumber)
    my_entry.delete(0,END)

def mydiv():
    global fnum
    global case
    case="division"
    firstnumber=my_entry.get()
    fnum=int(firstnumber)
    my_entry.delete(0,END)

def mymul():
    global fnum
    global case
    case="multiplication"
    firstnumber=my_entry.get()
    fnum=int(firstnumber)
    my_entry.delete(0,END)
  
    


button_1=Button(root,text="1",padx=30,pady=10,command=lambda: myclick(1))
button_2=Button(root,text="2",padx=30,pady=10,command=lambda: myclick(2))
button_3=Button(root,text="3",padx=30,pady=10,command=lambda: myclick(3))
button_4=Button(root,text="4",padx=30,pady=10,command=lambda: myclick(4))
button_5=Button(root,text="5",padx=30,pady=10,command=lambda: myclick(5))
button_6=Button(root,text="6",padx=30,pady=10,command=lambda: myclick(6))
button_7=Button(root,text="7",padx=30,pady=10,command=lambda: myclick(7))
button_8=Button(root,text="8",padx=30,pady=10,command=lambda: myclick(8))
button_9=Button(root,text="9",padx=30,pady=10,command=lambda: myclick(9))
button_0=Button(root,text="0",padx=30,pady=10,command=lambda: myclick(0))
button_add=Button(root,text="+",padx=30,pady=10,command=myadd)
button_sub=Button(root,text="-",padx=30,pady=10,command=mysub)
button_div=Button(root,text="/",padx=30,pady=10,command=mydiv)
button_mul=Button(root,text="*",padx=30,pady=10,command=mymul)
button_clear=Button(root,text="CLR",padx=22,pady=10,command=myclear)
button_equal=Button(root,text="=",padx=30,pady=10,command=myequal)


button_9.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_7.grid(row=1,column=2)

button_6.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_4.grid(row=2,column=2)


button_3.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_1.grid(row=3,column=2)


button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1)
button_equal.grid(row=4,column=2)


button_add.grid(row=1,column=4)
button_sub.grid(row=2,column=4)
button_div.grid(row=3,column=4)
button_mul.grid(row=4,column=4)

root.mainloop()
