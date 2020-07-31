from tkinter import *
#CREATING A INTERFACE
window=Tk()

#TITLE
window.title("Calculator")

#CREATING ENTRY FIELD
entry=Entry(window,width=35)
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

#BUTTON CLICK FUNCTION
def button_click(num):
    current=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current)+str(num))

#CLEAR ALL FUNCTION    
def button_clear():
    entry.delete(0,END)
    

#ADD FUNCTION    
def button_add():
    firstnumber=entry.get()
    global math
    math='addition'
    global f_num
    f_num=int(firstnumber)
    entry.delete(0,END)
    
#SUBTRACT FUNCTION
def button_sub():
    firstnumber=entry.get()
    global math
    math='subtraction'
    global f_num
    f_num=int(firstnumber)
    entry.delete(0,END)

    
#MULTIPLY FUNCTION    
def button_mul():
    firstnumber=entry.get()
    global math
    math='multiplication'
    global f_num
    f_num=int(firstnumber)
    entry.delete(0,END)
    
#DIVISION FUNCTION
def button_div():
    firstnumber=entry.get()
    global math
    math='division'
    global f_num
    f_num=int(firstnumber)
    entry.delete(0,END)
    
#EQUAL TO FUNCTION    
def button_equal():
    second_number=entry.get()
    entry.delete(0,END)
    if math=='addition':
        entry.insert(0,int(second_number)+f_num)
    elif math=='subtraction':
        entry.insert(0,f_num-int(second_number))
    elif math=='multiplication':
        entry.insert(0,int(second_number)*f_num)
    elif math=='division':
        entry.insert(0,f_num/int(second_number))

    

#CREATING BUTTONS
button_1=Button(window,text='1',padx=20,pady=20,command=lambda : button_click(1))
button_2=Button(window,text='2',padx=20,pady=20,command=lambda : button_click(2))
button_3=Button(window,text='3',padx=20,pady=20,command=lambda : button_click(3))
button_4=Button(window,text='4',padx=20,pady=20,command=lambda : button_click(4))
button_5=Button(window,text='5',padx=20,pady=20,command=lambda : button_click(5))
button_6=Button(window,text='6',padx=20,pady=20,command=lambda : button_click(6))
button_7=Button(window,text='7',padx=20,pady=20,command=lambda : button_click(7))
button_8=Button(window,text='8',padx=20,pady=20,command=lambda : button_click(8))
button_9=Button(window,text='9',padx=20,pady=20,command=lambda : button_click(9))
button_0=Button(window,text='0',padx=20,pady=20,command= lambda:button_click(0))
button_add=Button(window,text='+',bg='gray85',padx=20,pady=20,command=button_add)
button_sub=Button(window,text='-',bg='gray85',padx=20,pady=20,command=button_sub)
button_mul=Button(window,text='x',bg='gray85',padx=20,pady=20,command=button_mul)
button_div=Button(window,text='/',bg='gray85',padx=20,pady=20,command=button_div)
button_clear=Button(window,text='C',bg='tomato',padx=20,pady=20,command= button_clear)
button_equal=Button(window,text='=',bg='seagreen1',padx=20,pady=20,command=button_equal)


#ASSIGNING BUTTON GRIDS
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=1)

button_add.grid(row=1,column=3)
button_sub.grid(row=2,column=3)
button_mul.grid(row=3,column=3)
button_div.grid(row=4,column=3)

button_clear.grid(row=4,column=0)
button_equal.grid(row=4,column=2)

window.mainloop()                
                
