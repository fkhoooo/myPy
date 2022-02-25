from pathlib import Path
import shutil
from xmlrpc.client import Boolean
# 相同目录结构同步
srcUrl = "E:\\zg\client\\kingrbyz"
tarUrl = "F:\\testAssets"
# 需要同步的目录
srcList =[
        "E:\\zg\\client\\kingrbyz\\assets\\res\\dynamicSkin",
        "E:\\zg\\client\kingrbyz\\assets\stu\\assetsRes\\res\\dress",
        "E:\\zg\\client\kingrbyz\\assets\stu\\assetsRes\\res\\beauty",
        "E:\\zg\\client\kingrbyz\\assets\stu\\assetsRes\\res\\activity",
        "E:\\zg\\client\kingrbyz\\assets\stu\\assetsRes\\res\\package\itemicon",
        "E:\\zg\\client\kingrbyz\\assets\stu\\assetsRes\\res\\player"
    ]

desList = []

def doCopyFile1(data):
    srcPath = Path(data)
    for i in srcPath.glob("**/*"):
        if (not filterFile(i)):
            continue
        if(i.suffix == ".lua" or i.suffix == ".rej" or i.suffix == ".ttf"):
            continue
        if(i.is_file()):
            tarPath = Path(str(i).replace(srcUrl,tarUrl))
            if(not tarPath.parent.exists()):
                tarPath.parent.mkdir(parents = True)
                if(not tarPath.exists()):
                    shutil.copy(str(i),str(tarPath))
            else:
                if(not tarPath.exists()):
                    shutil.copy(str(i),str(tarPath))
    print("同步完毕-------") 

def filterFile(data):
    for i in data.parents:
        if (str(i) in srcList):
           return True
    return False
if __name__ == '__main__':
    doCopyFile1(srcUrl)


    