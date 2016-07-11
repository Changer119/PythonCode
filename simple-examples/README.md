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

**与re.I类似的还有:**

- re.I(全拼：IGNORECASE): 忽略大小写（括号内是完整写法，下同）
- re.M(全拼：MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
- re.S(全拼：DOTALL): 点任意匹配模式，改变'.'的行为
- re.L(全拼：LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
- re.U(全拼：UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
- re.X(全拼：VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。


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