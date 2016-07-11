from io import BytesIO

print("测试 写入BytesIO")
f = BytesIO()
f.write(b"hello \n")
f.write(b"world \n")
f.write(b"from fcjiang !!!")
print(f.getvalue())
print("\n")

print("测试 读取BytesIO")
dataBytes = "一万年太久,只争朝夕".encode("utf-8")
f = BytesIO(dataBytes)
print(f.read())