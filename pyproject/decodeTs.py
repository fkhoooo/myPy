from openpyxl import load_workbook
import json
from pathlib import Path
def decode(path):
    wb = load_workbook(path)
    sheets = wb.get_sheet_names()
    #第一个表格的名称
    sheet_first = sheets[0]
    #获取特定的worksheet
    ws = wb.get_sheet_by_name(sheet_first)
    rows = ws.rows 
    #迭代所有的行
    lines = []
    for row in rows:
        lines.append([col.value for col in row]) 
    
    annot = lines[0]
    pro = lines[1]
    valueType = lines[2]
    pathData = Path(path)
    na = pathData.stem.capitalize() + "Json_json"
    ##############################
    info = "class " + na + "\n" + "{\n"
    for i in range(len(pro)):
        info += "   public " + pro[i] + ":" + getValueType(valueType[i]) + "//" + annot[i] + ";\n"
    
    info += "   private static dataList:any = {};\n"
    info += "   private static key:string[] = ["
    key = []
    for i in range(len(annot)):
        if(annot[i].find("#") != -1):
            key.append(pro[i])
    if(len(key) == 0):
        key.append(pro[0])

    idx = 0
    for i in key:
        info += "'" + i + "'"
        if(idx == len(key)-1):
            info += "];\n"
        else:
            info += ","
        idx += 1

##################################

    info += "   public constructor()\n" + "   {\n" + "   }\n\n"

##################################
    info += "   public static getData(" + getArg(key,valueType) + "):" + na +"\n"
    info += "   {\n"  
    info += "      let key:string = " + getkey(key) + ";\n"
    info += "      return this.dataList[key]\n"
    info += "   }\n\n"
##################################

    info += "   public static decodeJson(data:any)\n"
    info += "   {\n"	
    info += "      for(let j in data)\n"
    info += "      {\n"	
    info += "          let vo:" + na + " = data[j];\n"
    info += "          let keyIdx:string = '';\n"
    info += "          for(let i:number = 0; i < this.key.length; i++)\n"
    info += "          {\n"
    info += "               keyIdx += vo[this.key[i]] + (i == this.key.length - 1 ? '' : '_');\n"
    info += "          }\n"
    info += "          this.dataList[keyIdx] = vo;\n"
    info += "      }\n"
    info += "   }\n"

##################################
    info += "}"
    tsName = na + ".ts"
    url = "C:\\Users\\Administrator\\Desktop\\CarGame\\src\\json\\"
    newPath = url +  tsName
    f=open(newPath,"w",encoding="utf-8")#utf8中文编码
    f.write(info)
    f.close 

def getValueType(type):
    if(type == "int"):
        return "number"
    elif(type == "str"):
        return "string"

def getArg(key,valueType):
    arg = ""
    idx = 0
    for i in range(len(key)):
        if(idx == len(key)-1):
            arg += key[i] + ":" + getValueType(valueType[i])
        else:
            arg += key[i] + ":" + getValueType(valueType[i]) + ","
        idx += 1
    return arg

def getkey(key):
    idx = 0
    keystr = ""
    for i in range(len(key)):
        if(idx == len(key)-1):
            keystr += key[i]
        else:
            keystr += key[i] + " + '_' + "
        idx += 1
    return keystr + " + ''"
