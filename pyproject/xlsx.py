from openpyxl import load_workbook
import json
from pathlib import Path
def resolve(path):
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
    
    key = lines[1]
    length = len(key)
    dataList = []
    for i in range(3,len(lines)):#第4行开始
        rowList = lines[i]
        setlist = {}
        for j in range (length):
            setlist[key[j]] = rowList[j]
        dataList.append(setlist)
    #dumps是把python对象转换成json对象的一个过程，生成的是字符串
    tx = json.dumps(dataList, ensure_ascii = False,sort_keys=False, indent = 2)#sort_keys 排序, indent 缩进
    #写入文件
    pathData = Path(path)
    na = pathData.stem + "Json.json"
    newPath = pathData.parent.parent / na
    f=open(newPath,"w",encoding="utf-8")#utf8中文编码
    f.write(tx)
    f.close 