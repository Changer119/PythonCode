from io import StringIO

print("测试 写入StringIO")
f = StringIO()
f.write("hello \n")
f.write("world \n")
f.write("from fcjiang !!!")
print(f.getvalue())
print("\n")

print("测试 读取StringIO")
f = StringIO("水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。")
while True:
    s = f.readline()
    if s == "":
        break
    print(s)