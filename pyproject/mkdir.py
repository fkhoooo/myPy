from pathlib import Path
#创建文件夹
fileData = Path("C:\\Users\\Administrator\\Desktop\\aa\\cc")
if (not fileData.exists()):
   fileData.mkdir(parents=True)#连续创建 aa,cc

if (not fileData.exists()):
   fileData.mkdir()#不能包括子目录(不能有cc).会报错

