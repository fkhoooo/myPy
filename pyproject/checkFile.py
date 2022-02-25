from pathlib import Path
from tkinter import filedialog
fileData = Path("C:\\Users\\Administrator\\Desktop\\CarGame")
#for i in fileData.iterdir():
    # print(i)

#递归遍历说有png(包含子目录)
#for i in fileData.rglob("*.png"):
#    print(i)

#遍历所有png (不包括子目录)
#for i in fileData.glob("*.png"):
#    print(i)

# 遍历所有文件(包括子目录)
for i in fileData.glob("**/*"):
#    print(i)
    for j in i.parents:
        print(str(j))

# Path("C:\\Users\\Administrator\\Desktop\\aa\\123.txt").replace("C:\\Users\\Administrator\\Desktop\\bb\\123.txt")替换



