from pathlib import Path
fileData = Path("C:\\Users\\Administrator\\Desktop\\xingQingUI")
for i in fileData.rglob("*.png"):
    na = i.stem + ".jpg"#新的名称后缀
    parUrl = i.resolve().parent #文件路径
    i.rename(parUrl / na) #参数是一个绝对路径 /拼接