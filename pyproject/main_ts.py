from Class_ts import Student #在Class_ts模块里 导入 Student类
import Class_ts

#在不同文件夹下调用

#A.py文件的文件路径为：C:\\AmyPython\\Test1

#B.py中调用A.py文件：
import sys
#'C:\\Users\\Administrator\\Desktop\\robe\\Class_ts1.py'
sys.path.append('C:\\Users\\Administrator\\Desktop\\robe')#导入指定目录 不包括模块名(Class_ts1)
#python import模块时， 是在sys.path里按顺序查找的。sys.path是一个列表，里面以字符串的形式存储了许多路径。使用A.py文件中的函数需要先将他的文件路径放到sys.path中
import Class_ts1


stu = Student("a",20)
print(stu.name,stu.score)

Class_ts.fun() #直接调用模块里的函数
Class_ts1.fun()#直接调用模块里的函数