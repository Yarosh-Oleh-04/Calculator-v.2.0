import stack
import tkinter


def btn_click():
    txt = form.get()
    result = stack.calc(txt)
    if txt != '' and result != '':
        form.delete(0, len(txt))
        form.insert(0, result)
    res.delete(0, len(res.get()))


def write(val):
    if val == 'del':
        form.delete(0, len(form.get()))
        res.delete(0, len(res.get()))
        return 0
    if val == 'c':
        form.delete(len(form.get()) - 1, len(form.get()))
        result = stack.calc(form.get())
        if len(stack.infix_to_postfix(form.get()).split(' ')) != 1:
            res.delete(0, len(res.get()))
            res.insert(0, result)
    else:
        txt = form.get()
        form.delete(0, len(txt))
        form.insert(0, txt + str(val))
        result = stack.calc(form.get())
        if result != '' and len(stack.infix_to_postfix(form.get()).split(' ')) != 1:
            res.delete(0, len(res.get()))
            res.insert(0, result)


top = tkinter.Tk()
top.title('Calculator')
top.geometry('400x358')
top.grid(widthInc=4)
top.resizable(0, 0)

text_field = tkinter.StringVar()

form = tkinter.Entry(top, width=30, textvariable=text_field, font=('', '18'), bg='#FFCC99')
form.grid(columnspan=5, row=0)
res = tkinter.Entry(top, width=30, font=('', '18'), bg='#FFCC99')
res.grid(columnspan=5, row=1)
buttons = []

for i in range(9):
    buttons += [tkinter.Button(top, text=str(i+1), command=lambda x=i+1: write(x))]
    buttons[i].grid(row=i//3+2, column=i%3)

buttons += [tkinter.Button(top, bg='gray', width=10, text='=', command=btn_click)]
buttons[9].grid(row=5, column=2)
buttons += [tkinter.Button(top, text='+', command=lambda: write('+'))]
buttons += [tkinter.Button(top, text='-', command=lambda: write('-'))]
buttons += [tkinter.Button(top, text='*', command=lambda: write('*'))]
buttons += [tkinter.Button(top, text='/', command=lambda: write('/'))]

for i in range(1, 5):
    buttons[i+9].grid(row=i+1, column=3)

buttons += [tkinter.Button(top, text='C', command=lambda: write('c'))]
buttons[14].grid(row=3, column=4)
buttons += [tkinter.Button(top, text='Del', command=lambda: write('del'))]
buttons[15].grid(row=2, column=4)
buttons += [tkinter.Button(top, text='0', command=lambda: write(0))]
buttons[16].grid(row=5, column=1)
buttons += [tkinter.Button(top, text='.', command=lambda: write('.'))]
buttons[17].grid(row=5, column=0)

buttons += [tkinter.Button(top, text='(', command=lambda: write('('))]
buttons[18].grid(row=4, column=4)
buttons += [tkinter.Button(top, text=')', command=lambda: write(')'))]
buttons[19].grid(row=5, column=4)

# 0-8 and 16: numbers;
# 9: equals;
# 10-13: actions
# 14-15 and 18-19: Del, C, ();
# 15: dot
# 20: is empty

for button in buttons:
    button['bg'] = '#00CCFF'
    button['width'] = 5
    button.config(height=2)
    button['font'] = ('', '18')

top.mainloop()

