## 正则表达式

### 常见的使用方式(2种)

- 方式1:直接使用正则表达式

``` python
import re
result = re.findall(r"hello", src, re.I)
```

- 方式2:使用编译后的正则对象(速度快)

``` python
import re
patt = re.compile(r"hello", re.I)
result = patt.findall(src)
```

### 常见的方法

#### match/search
match   从头匹配,如果没有则返回None,有匹配则返回匹配对象.要从匹配对象中获取数据,可以使用```macth_object.group(0)```
serach  只有目前文本中有匹配,就会返回去匹配对象.

#### findall/finditer
findall     返回匹配的数据的list
finditer    返回匹配数据的迭代器
 
#### sub/subn
sub         将符合正则表达式的字符串替换
subn        同上,同时返回替换的个数

#### split
split       根据表达式进行分割