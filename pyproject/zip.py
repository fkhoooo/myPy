import zipfile
from pathlib import Path

# 在指定zip压缩文件目录下创建zip文件
create_zip_file = zipfile.ZipFile(r"C:\Users\Administrator\Desktop\CarGame\resource\jsonData.zip", mode='a', compression=zipfile.ZIP_DEFLATED)

# zip 放入文件
for i in Path(r"C:\Users\Administrator\Desktop\CarGame\resource\json").glob("*.json"):
   print(str(i),i.name)
   create_zip_file.write(str(i),i.name)
create_zip_file.close()