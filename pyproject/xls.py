import xlrd
import json
from pathlib import Path
def resolve(path):
    book = xlrd.open_workbook(path)
    tabel = book.sheets()[0]
    key = tabel.row_values(1)
    length = len(tabel.row_values(1))
    dataList = []
    for i in range(3,tabel.nrows):#第4行开始
        rowList = tabel.row_values(i)
        setlist = {}
        for j in range (length):
            setlist[key[j]] = rowList[j]
        dataList.append(setlist)

    #dumps是把python对象转换成json对象的一个过程，生成的是字符串
    tx = json.dumps(dataList, ensure_ascii = False,sort_keys=False, indent = 2)#sort_keys 排序, indent 缩进
    #写入文件
    pathData = Path(path)
    na = pathData.stem + ".json"
    newPath = pathData.parent.parent / na
    f=open(newPath,"w",encoding="utf-8")#utf8中文编码
    f.write(tx)
    f.close 

def writeTs(path):

    book = xlrd.open_workbook(path)
    tabel = book.sheets()[0]
    annot= tabel.row_values(0)#注释
    pro = tabel.row_values(1)#属性
    valueType =  tabel.row_values(2)#值类型
    pathData = Path(path)
    na = pathData.stem.capitalize() + ".ts"

  ##############################
    info = "class " + na + "\n" + "{"
    for i in pro:
        info += "  public " + pro[i] + ":" + getValueType(valueType[i]) + "//" + annot[i] + "\n"
    
    info += "  public static dataList:any = {}\n"
    info += "  private static key:string[] = ["
    key = []
    for i in annot:
        if(annot[i].index("#") != -1):
            key.append(pro[i])
    if(len(key) == 0):
        key[0] = pro[0]
    idx = 0
    for i in key:
        info += "'" +key[i] + "'"
        if(idx == len(key) -1):
            info += "]\n"
        else:
            info += ","
        idx += 1

##################################

    info += "  public constructor()\n" + "{\n" + "super();\n" + "}"

##################################


    info += "  public static decodeJson(data:any)\n"
    info += "  {\n"	
    info += "     for(let j in data)\n"
    info += "     {\n"	
    info += "         let vo:any = data[j];\n"
    info += "         let keyIdx:string = '';\n"
    info += "         let flg:string = '';\n"
    info += "         for(let i:number = 0; i < this.key.length; i++)\n"
    info += "         {\n"
    info += "              flg = i == this.key.length - 1 ? '': '_'\n"
    info += "              keyIdx += vo[this.key[i]] + flg;\n"
    info += "         }\n"
    info += "         this.dataList[keyIdx] = vo;\n"
    info += "     }\n"
    info += "  }\n"

##################################
    info += "}"
    newPath = pathData.parent.parent / na
    f=open(newPath,"w",encoding="utf-8")#utf8中文编码
    f.write(info)
    f.close 

def getValueType(type):
    if(type == "int"):
        return "number"
    elif(type == "str"):
        return "string"

    


