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
top.title('Window')
top.geometry('400x145')
top.grid(widthInc=4)

text_field = tkinter.StringVar()

form = tkinter.Entry(top, width=50, textvariable=text_field)
form.grid(columnspan=4, row=0)
res = tkinter.Entry(top, width=50)
res.grid(columnspan=4, row=1)
buttons = []

for i in range(9):
    tkinter.Button(top, bg='gray', width=10, text=str(i+1), command=lambda x=i+1: write(x)).grid(row=i//3+2, column=i%3)

equals = tkinter.Button(top, bg='gray', width=10, text='=', command=btn_click)
equals.grid(row=0, column=4, rowspan=2)
equals.config(height=2, width=10, text='=')
tkinter.Button(top, bg='gray', width=10, text='+', command=lambda: write('+')).grid(row=2, column=3)
tkinter.Button(top, bg='gray', width=10, text='-', command=lambda: write('-')).grid(row=3, column=3)
tkinter.Button(top, bg='gray', width=10, text='*', command=lambda: write('*')).grid(row=4, column=3)
tkinter.Button(top, bg='gray', width=10, text='/', command=lambda: write('/')).grid(row=5, column=3)


tkinter.Button(top, bg='gray', width=10, text='C', command=lambda: write('c')).grid(row=3, column=4)
tkinter.Button(top, bg='gray', width=10, text='Del', command=lambda: write('del')).grid(row=2, column=4)
tkinter.Button(top, bg='gray', width=10, text='0', command=lambda: write(0)).grid(row=5, column=1)
tkinter.Button(top, bg='gray', width=10, text='.', command=lambda: write('.')).grid(row=5, column=0)

tkinter.Button(top, bg='gray', width=10, text='(', command=lambda: write('(')).grid(row=4, column=4)
tkinter.Button(top, bg='gray', width=10, text=')', command=lambda: write(')')).grid(row=5, column=4)
tkinter.Button(top, bg='gray', width=10, text='', command=lambda: write('')).grid(row=5, column=2)


top.mainloop()

