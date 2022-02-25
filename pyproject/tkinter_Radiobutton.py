import tkinter as tk 
window = tk.Tk()
window.title ("radiobutton")
window.geometry("300x400")
var = tk.StringVar()
l = tk.Label(window,bg ="yellow")
l.pack()
def print_selection():
    l.config(text = "you have selected" + var.get())
# 第5步，创建三个radiobutton选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
r1 = tk.Radiobutton(window,text = "Option A", variable = var, value = "A", command = print_selection)
r1.pack()
r2 = tk.Radiobutton(window,text = "Option B", variable = var, value = "B", command = print_selection)
r2.pack()
r3 = tk.Radiobutton(window,text = "Option C", variable = var, value = "C", command = print_selection)
r3.pack()
window.mainloop()