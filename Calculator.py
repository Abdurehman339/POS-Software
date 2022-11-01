from tkinter import *
root = Tk()
root.geometry('400x400')
root.minsize(400,400)
root.maxsize(400,400)

myInput = Entry(root,font = 'Arial 30',border=12,width=17)
myInput.grid(row=0,columnspan=4)

def Click(num):
    myInput.insert(END,num)

def Clear():
    myInput.delete(0,END)
    
def Equal():
    value = myInput.get()
    Clear()
    if value.isdigit():
        myInput.insert(0,value)
    else:
        value = eval(value)
        myInput.insert(0,value)


width = 40
height = 29        

button_7 = Button(root,text="7",padx=width,pady=height,command=lambda: Click('7')).grid(row=1,column=0)
button_8 = Button(root,text="8",padx=width,pady=height,command=lambda: Click('8')).grid(row=1,column=1)
button_9 = Button(root,text="9",padx=width,pady=height,command=lambda: Click('9')).grid(row=1,column=2)
button_add = Button(root,text="+",padx=width,pady=height,command=lambda: Click('+')).grid(row=1,column=3)

button_4 = Button(root,text="4",padx=width,pady=height,command=lambda: Click('4')).grid(row=2,column=0)
button_5 = Button(root,text="5",padx=width,pady=height,command=lambda: Click('5')).grid(row=2,column=1)
button_6 = Button(root,text="6",padx=width,pady=height,command=lambda: Click('6')).grid(row=2,column=2)
button_sub = Button(root,text="-",padx=width,pady=height,command=lambda: Click('-')).grid(row=2,column=3)

button_1 = Button(root,text="1",padx=width,pady=height,command=lambda: Click('1')).grid(row=3,column=0)
button_2 = Button(root,text="2",padx=width,pady=height,command=lambda: Click('2')).grid(row=3,column=1)
button_3 = Button(root,text="3",padx=width,pady=height,command=lambda: Click('3')).grid(row=3,column=2)
button_mul = Button(root,text="*",padx=width,pady=height,command=lambda: Click('*')).grid(row=3,column=3)

button_ce = Button(root,text="c",padx=width,pady=height,command=Clear).grid(row=4,column=0)
button_0 = Button(root,text="0",padx=width,pady=height,command=lambda: Click('0')).grid(row=4,column=1)
button_equal = Button(root,text="=",padx=width,pady=height,command=Equal).grid(row=4,column=2)
button_divide = Button(root,text="/",padx=width,pady=height,command=lambda: Click('/')).grid(row=4,column=3)

root.mainloop()