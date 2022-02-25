import tkinter as tk
window = tk.Tk()
window.title("My Window")
window.geometry("300x400")
var1 = tk.StringVar()#定义变量
l = tk.Label(window,bg = "green",fg = "yellow",font = ("Arial",12), width = 10, textvariable = var1)
l.pack()
def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)#List选中赋值给Label
b1 = tk.Button(window,text = "print selection",command = print_selection)
b1.pack()

var2 = tk.StringVar()#定义变量
var2.set((1,2,3,4))#设置List内容
lb = tk.Listbox(window,listvariable = var2)
list_items = [11,22,33,44]
for item in list_items:
    lb.insert("end",item)#后面追加内容
lb.pack()
window.mainloop()
