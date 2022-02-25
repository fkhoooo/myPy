import os
import shutil
source_path = r"C:\Users\Administrator\Desktop\test\greensock"
target_path = r"C:\Users\Administrator\Desktop\aa"



# if not os.path.exists(target_path):
#     # 如果目标路径不存在原文件夹的话就创建
#     os.makedirs(target_path)

# if os.path.exists(source_path):
#     # 如果目标路径存在原文件夹的话就先删除
#     shutil.rmtree(target_path)

if not os.path.exists(target_path):
    shutil.copytree(source_path, target_path)
print('copy dir finished!')