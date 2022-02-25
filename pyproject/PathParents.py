from pathlib import Path
fileData = Path(r"C:\Users\Administrator\Desktop\a")
for i in fileData.parents:
    print(str(i) == r"C:\Users\Administrator\Desktop")
    # 是否是父目录
