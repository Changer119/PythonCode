# try:
#     f = open("aa.txt", "r")
#     print(f.read())
# finally:
#     if f:
#         print("准备关闭文件句柄")
#         f.close()

# 以上可以简化为下面的代码
with open("aa.txt", "r") as f:
    print(f.read())
    print("会自动关闭文件句柄")
print("===================================")

with open("bb.txt", "w") as f:
    print("创建文件bb.txt")
    f.write("This is a file created by python")

with open("bb.txt", "r") as f:
    print("读取文件bb.txt")
    print(f.read())

with open("aa_pic.png", "rb") as f:
    print("以二进制方式读取文件aa_pic.png")
    print(f.read())