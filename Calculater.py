import tkinter as tk
import re

def checkin(n):
    check.insert(tk.END, str(n))

def delte():
    check.delete(0, tk.END)

def calc():
    data = check.get()
    num = re.findall(r'\d+', data)
    oper = re.findall(r'[^\d]+', data)
    num = list(map(int, num))
    result = 0
    if oper[0] == '*':
        result = num[0] * num[1]
    elif oper[0] == '/':
        result = num[0] / num[1]
    elif oper[0] == '+':
        result = num[0] + num[1]
    elif oper[0] == '-':
        result = num[0] - num[1]
    check.delete(0, tk.END)
    check.insert(tk.END, result)


window = tk.Tk()
window.title('Calculater')
window.geometry('370x290+100+150')

check = tk.Entry(window, text='Result', width=15)
blank = tk.Label(window)

for i in range(1, 10, 1):
    side=(i-1)//3 +2
    leng=(i-1)%3
    button = tk.Button(window, text=str(i), width=10, height=3, command=lambda i=i: checkin(i))
    button.grid(row=side, column=leng)

delete = tk.Button(window, text='Del', width=10, height=3, command=delte)
zero = tk.Button(window, text='0', width=10, height=3, command=lambda i=0: checkin(i))
calcu = tk.Button(window, text='=', width=10, height=3, command=calc)

plus = tk.Button(window, text='+', width=10, height=3, command=lambda i='+': checkin(i))
minus = tk.Button(window, text='-', width=10, height=3, command=lambda i="-": checkin(i))
mix = tk.Button(window, text='X', width=10, height=3, command=lambda i='*': checkin(i))
divide = tk.Button(window, text='÷', width=10, height=3, command=lambda i='/': checkin(i))

check.grid(row=0, column=1)
blank.grid(row=1, column=0)
delete.grid(row=5, column=0)
zero.grid(row=5, column=1)
calcu.grid(row=5, column=2)
for i in range(2, 6, 1):
    blank.grid(row=i, column=4)

plus.grid(row=2, column=5)
minus.grid(row=3, column=5)
mix.grid(row=4, column=5)
divide.grid(row=5, column=5)

window.mainloop()