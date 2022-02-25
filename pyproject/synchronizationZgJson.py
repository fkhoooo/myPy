from distutils import cmd
from pathlib import Path
import shutil
import subprocess

def zgConfig():
    srcPath = Path(r"E:\zg\client\kingrbyz\config")
    decPath = Path(r"E:\testAssets\ZgH5\resource\json\config")
    if not decPath.exists():
        decPath.mkdir(parents = True)

    isUpdate = False
    for i in srcPath.glob("*.xls"): 
        decFile = decPath / i.name
        if not isUpdate:
            if decFile.exists():
                if i.stat().st_mtime != decFile.stat().st_mtime:
                    isUpdate = True
            else:
                isUpdate = True
        shutil.copy2(str(i), decFile)
    if isUpdate == True:
        bat = Path.cwd() / "zgcongfig.bat"
        p = subprocess.Popen("cmd.exe /c" + str(bat), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        curline = p.stdout.readline()
        while (curline != b''):
            print(curline)
            curline = p.stdout.readline()
        p.wait()
        print(p.returncode)
        print("配置表更新完成")
    else:
        print("没有可更新配置表")
if __name__ == '__main__':
    zgConfig()


    
