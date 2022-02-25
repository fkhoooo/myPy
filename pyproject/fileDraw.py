import windnd
import tkinter as tk
from pathlib import Path
import xls
import xlsx
import decodeTs
window = tk.Tk()
def readFile(data):
    for item in data:
        msg = item.decode("gbk")# 必须解码
        fileData = Path(msg)
        if(fileData.is_dir()):
            for i in fileData.glob("**/*"):
                doFun(i)
        else:
            doFun(msg)

def doFun(data):
    print(data)
    xlsx.resolve(data)
    decodeTs.decode(data)

windnd.hook_dropfiles(window,readFile)
tk.mainloop()