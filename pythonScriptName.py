import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, background = 'black')
canvas1.pack()

def hello ():  
    label1 = tk.Label(root, text= 'Hello World!', fg='white', bg='black', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 100, window=label1)
    
button1 = tk.Button(text='Click Me',command=hello, bg='white',fg='black')
canvas1.create_window(150, 250, window=button1)

root.mainloop()