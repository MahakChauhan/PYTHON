import os

folders=os.listdir("data")
print(folders)
print(os.getcwd())
os.chdir("/users")
print(os.getcwd())
# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))