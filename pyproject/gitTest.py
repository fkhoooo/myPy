from git import Repo
repo =Repo("E:\zg\client\kingrbyz\.git") #git文件的路径
repo.remote().pull()

print("拉取完成")