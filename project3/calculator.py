from tkinter import*

mycalc=Tk()
mycalc.geometry("500x500")
mycalc.title("simple calculator")
mycalclabel = Label(mycalc,text="CALCULATOR",bg='dark gray',font=("Times",30,'bold'))
mycalclabel.pack(side=TOP)
mycalc.config(background='gray')

textin=StringVar()
operator=""

def clickbutton(number):   
     global operator
     operator=operator+str(number)
     textin.set(operator)

def equalbut():
     global operator
     add=str(eval(operator))
     textin.set(add)
     operator=''
def equalbut():
     global operator
     sub=str(eval(operator))
     textin.set(sub)
     operator=''     
def equlbut():
     global operator
     mul=str(eval(operator))
     textin.set(mul)
     operator=''
def equalbut():
     global operator
     div=str(eval(operator))
     textin.set(div)
     operator=''    

def clrbut():
     textin.set('')

     
mycalctext=Entry(mycalc,font=("Courier New",12,'bold'),textvar=textin,width=25,bd=5,bg='blue')
mycalctext.pack()

one=Button(mycalc,padx=14,pady=14,bg='red',command=lambda:clickbutton(1),text="1",font=("Courier New",16,'bold'))
one.place(x=10,y=100)

two=Button(mycalc,padx=14,pady=14,bg='red',command=lambda:clickbutton(2),text="2",font=("Courier New",16,'bold'))
two.place(x=10,y=170)

three=Button(mycalc,padx=14,pady=14,bg='red',command=lambda:clickbutton(3),text="3",font=("Courier New",16,'bold'))
three.place(x=10,y=240)

four=Button(mycalc,padx=14,pady=14,bg='red',command=lambda:clickbutton(4),text="4",font=("Courier New",16,'bold'))
four.place(x=75,y=100)

five=Button(mycalc,padx=14,pady=14,bg='red',command=lambda:clickbutton(5),text="5",font=("Courier New",16,'bold'))
five.place(x=75,y=170)

six=Button(mycalc,padx=14,pady=14,bg='red',command=lambda:clickbutton(6),text="6",font=("Courier New",16,'bold'))
six.place(x=75,y=240)

seven=Button(mycalc,padx=14,pady=14,bg='red',command=lambda:clickbutton(7),text="7",font=("Courier New",16,'bold'))
seven.place(x=140,y=100)

eight=Button(mycalc,padx=14,pady=14,bg='red',command=lambda:clickbutton(8),text="8",font=("Courier New",16,'bold'))
eight.place(x=140,y=170)

nine=Button(mycalc,padx=14,pady=14,bg='red',command=lambda:clickbutton(9),text="9",font=("Courier New",16,'bold'))
nine.place(x=140,y=240)

zero=Button(mycalc,padx=14,pady=14,bg='red',command=lambda:clickbutton(0),text="0",font=("Courier New",16,'bold'))
zero.place(x=10,y=310)

decimal=Button(mycalc,padx=47,pady=14,bg='red',command=lambda:clickbutton("."),text=".",font=("Courier New",16,'bold'))
decimal.place(x=75,y=310)

plus=Button(mycalc,padx=14,pady=14,bg='red',text="+",command=lambda:clickbutton("+"),font=("Courier New",16,'bold'))
plus.place(x=205,y=100)

sub=Button(mycalc,padx=14,pady=14,bg='red',text="-",command=lambda:clickbutton("-"),font=("Courier New",16,'bold'))
sub.place(x=205,y=170)

mul=Button(mycalc,padx=14,pady=14,bg='red',text="*",command=lambda:clickbutton("*"),font=("Courier New",16,'bold'))
mul.place(x=205,y=240)

div=Button(mycalc,padx=14,pady=14,bg='red',text="/",command=lambda:clickbutton("/"),font=("Courier New",16,'bold'))
div.place(x=205,y=310)

clear=Button(mycalc,padx=14,pady=120,bg='red',text="clr",command=clrbut,font=("Courier New",16,'bold'))
clear.place(x=270,y=100)

equal=Button(mycalc,padx=159,pady=14,bg='red',command=equalbut,text="=",font=("Courier New",16,'bold'))
equal.place(x=10,y=380)
mycalc.mainloop()
