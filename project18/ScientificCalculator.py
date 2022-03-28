from tkinter import *
import numpy as np
import math as m

calculator = Tk()
calculator.configure(bg="black", bd=10)
calculator.geometry("460x580")
calculator.title("Scientific Calculator")

def ClickButton(char):
    global operator
    operator += str(char)
    InputText.set(operator)

def ClearAll():
    global operator
    operator = ""
    InputText.set("")

def Delete():
    global operator
    text = operator[:-1]
    operator = text
    InputText.set(text)

def Sqrt():
    global operator
    result = str(m.sqrt(float(operator)))
    operator = result
    InputText.set(result)

def CubeRoot():
    global operator

    result = str(eval(operator+'**(1/3)'))
    operator = result
    InputText.set(result)


def CalculateFactorial():
    global operator
    result = str(m.factorial(int(operator)))
    operator = result
    InputText.set(result)    

def percent():
    global operator
    result = str(eval(operator+'/100'))
    operator = result
    InputText.set(result)

def CalculateSin():
    global operator
    result = str(m.sin(float(operator)))
    operator = result
    InputText.set(result)

def CalculateCos():
    global operator
    result = str(m.cos(m.radians(int(operator))))
    operator = result
    InputText.set(result)

def CalculateTan():
    global operator
    result = str(m.tan(m.radians(int(operator))))
    operator = result
    InputText.set(result)

def CalculateCot():
    global operator
    result = str(1/m.tan(m.radians(int(operator))))
    operator = result
    InputText.set(result)
    
def CalculateSec():
    global operator
    result = str(1/m.cos(m.radians(int(operator))))
    operator = result
    InputText.set(result)

def CalculateCosec():
    global operator
    result = str(1/m.sin(m.radians(int(operator))))
    operator = result
    InputText.set(result)

def mulinverse():
    global operator
    result = str(1/(float(operator)))
    operator = result
    InputText.set(result)

def evaluate():
    global operator
    result= str(eval(operator))
    operator = result
    InputText.set(result)

def log10():
    global operator
    result = str(m.log10(float(operator)))
    operator = result
    InputText.set(result)

def logn():
    global operator
    result = str(m.log(float(operator)))
    operator = result
    InputText.set(result)


operator = ""
InputText = StringVar()

display = Entry(calculator, font=('Verdana', 20, 'bold'), textvariable=InputText,
                     bd=10, insertwidth =6, bg='white', justify='right').grid(columnspan=5, padx = 20, pady = 20)

FunctionButton = {'bd':5, 'fg':'#BBB', 'bg':'#1b1b2c', 'font':('Verdana', 15, 'bold')}
NumberButton = {'bd':5, 'fg':'#000', 'bg':'#BBB', 'font':('Verdana', 15, 'bold')}

sin = Button(calculator, FunctionButton, text='sin',
             command=CalculateSin).grid(row=1, column=0, sticky="nsew")

cos = Button(calculator, FunctionButton, text='cos',
             command=CalculateCos).grid(row=1, column=1, sticky="nsew")

tan = Button(calculator, FunctionButton, text='tan',
             command=CalculateTan).grid(row=1, column=2, sticky="nsew")

cot = Button(calculator, FunctionButton, text='cot',
             command=CalculateCot).grid(row=1, column=3, sticky="nsew")

sec = Button(calculator, FunctionButton, text='sec',
             command=CalculateSec).grid(row=3, column=4, sticky="nsew")
cosec = Button(calculator, FunctionButton, text='cosec',
             command=CalculateCosec).grid(row=4, column=4, sticky="nsew")


button_1 = Button(calculator, NumberButton, text='1',
                  command=lambda:ClickButton('1')).grid(row=8, column=0, sticky="nsew")
button_2 = Button(calculator, NumberButton, text='2',
                  command=lambda:ClickButton('2')).grid(row=8, column=1, sticky="nsew")
button_3 = Button(calculator, NumberButton, text='3',
                  command=lambda:ClickButton('3')).grid(row=8, column=2, sticky="nsew")
button_4 = Button(calculator, NumberButton, text='4',
                  command=lambda:ClickButton('4')).grid(row=7, column=0, sticky="nsew")

button_5 = Button(calculator, NumberButton, text='5',
                  command=lambda:ClickButton('5')).grid(row=7, column=1, sticky="nsew")

button_6 = Button(calculator, NumberButton, text='6',
                  command=lambda:ClickButton('6')).grid(row=7, column=2, sticky="nsew")
button_7 = Button(calculator, NumberButton, text='7',
                  command=lambda:ClickButton('7')).grid(row=6, column=0, sticky="nsew")

button_8 = Button(calculator, NumberButton, text='8',
                  command=lambda:ClickButton('8')).grid(row=6, column=1, sticky="nsew")

button_9 = Button(calculator, NumberButton, text='9',
                  command=lambda:ClickButton('9')).grid(row=6, column=2, sticky="nsew")
button_0 = Button(calculator, NumberButton, text='0',
                  command=lambda:ClickButton('0')).grid(row=9, column=0, sticky="nsew")

mul = Button(calculator, NumberButton, text='*',
             command=lambda:ClickButton('*')).grid(row=7, column=3, sticky="nsew")

div = Button(calculator, NumberButton, text='/',
             command=lambda:ClickButton('/')).grid(row=7, column=4, sticky="nsew")


add = Button(calculator, NumberButton, text='+',
             command=lambda:ClickButton('+')).grid(row=8, column=3, sticky="nsew")
sub = Button(calculator, NumberButton, text='-',
             command=lambda:ClickButton('-')).grid(row=8, column=4, sticky="nsew")
equal = Button(calculator, NumberButton, text='=',
               command=evaluate).grid(row=9,column=4, sticky="nsew")

Square = Button(calculator, FunctionButton, text='x\u00B2',
             command=lambda:ClickButton('**2')).grid(row=3, column=0, sticky="nsew")

cube = Button(calculator, FunctionButton, text='x\u00B3',
             command=lambda:ClickButton('**3')).grid(row=3, column=1, sticky="nsew")


SquareRoot = Button(calculator, FunctionButton, text='\u00B2\u221A',
                     command=Sqrt).grid(row=4, column=0, sticky="nsew")

CubeRoot = Button(calculator, FunctionButton, text='\u00B3\u221A',
                    command=CubeRoot).grid(row=4, column=1, sticky="nsew")

LeftBracket = Button(calculator, FunctionButton, text='(',
                  command=lambda:ClickButton('(')).grid(row=4, column=2, sticky="nsew")

RightBracket = Button(calculator, FunctionButton, text=')',
                   command=lambda:ClickButton(')')).grid(row=4, column=3, sticky="nsew")

LogBase_10 = Button(calculator, FunctionButton, text='log\u2081\u2080', font=('Verdana', 16, 'bold'),
                   command=log10).grid(row=3, column=2, sticky="nsew")

LogBase_e = Button(calculator, FunctionButton, text='ln',
                   command=logn).grid(row=3, column=3, sticky="nsew")

DeleteOne = Button(calculator,NumberButton, 
              text='DEL', command=Delete).grid(row=9, column=2, sticky="nsew")

ClearAll = Button(calculator, NumberButton,
              text='AC', command=ClearAll).grid(row=9, column=3, sticky="nsew")

Pi = Button(calculator, FunctionButton, text='π',
                command=lambda:ClickButton(str(m.pi))).grid(row=1, column=4, sticky="nsew")

Exponent = Button(calculator, FunctionButton, text='e',
                    command=lambda:ClickButton(str(m.exp(1)))).grid(row=2, column=1, sticky="nsew")
Factorial = Button(calculator, FunctionButton, text='x!',
                   command=CalculateFactorial).grid(row=2, column=2, sticky="nsew")

mod = Button(calculator, FunctionButton, text='mod',
                command=lambda:ClickButton('%')).grid(row=2, column=4, sticky="nsew")

Percentage = Button(calculator, FunctionButton, text='%',
               command=percent).grid(row=2, column=0, sticky="nsew")


point = Button(calculator, NumberButton, text='.',
               command=lambda:ClickButton('.')).grid(row=9, column=1, sticky="nsew")


mulinverse = Button(calculator, FunctionButton, text='1/X',
                command=mulinverse).grid(row=2, column=3, sticky="nsew")


nthPowerButton = Button(calculator, FunctionButton, text='x^n',
             command=lambda:ClickButton('**')).grid(row=6, column=3, sticky="nsew")
TensPowerButton = Button(calculator, FunctionButton, text='10^x', font=('Verdana', 15, 'bold'),
                     command=lambda:ClickButton('10**')).grid(row=6, column=4, sticky="nsew")

calculator.mainloop()
