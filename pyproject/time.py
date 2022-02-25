import time
 
# 获得当前时间时间戳
now = int(time.time())
print(now)
#转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
timeArray = time.localtime(now)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)

timeList = time.strptime(otherStyleTime,"%Y-%m-%d %H:%M:%S")
timeNum = int(time.mktime(timeList))
print(timeNum)