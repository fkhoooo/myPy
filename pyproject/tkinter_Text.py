import tkinter as tk
window = tk.Tk()
window.title("my Window")
window.geometry('500x300')
l = tk.Label(window, text = "hello tkinter",bg = "green")
l.pack()

def click():
    print("点击")

def insertTx():
    var  = e2.get()
    tx.insert("end",var)#文本最后追加输入的文字

b = tk.Button(window,text = "点击", command = insertTx)
b.pack()

e1 = tk.Entry(window,show = "*")#输入文本
e2 = tk.Entry(window)
e1.pack()
e2.pack()

tx = tk.Text(window)#普通文本
tx.pack()

window.mainloop()