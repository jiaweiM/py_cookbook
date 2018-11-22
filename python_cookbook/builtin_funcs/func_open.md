open 函数打开文件，并返回文件对象。

### **语法**
```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```
#### 参数说明
- file, 要打开文件的文件路径
- mode, 文件打开模式
- buffering, 缓冲策略
- encoding, 文件编码，一般为UTF-8或GBK
- errors, 报错级别
- newline, 指定换行符，可选值如 `None`, ` `, `\n`, `\r\n`
- closefd, 传入的 file 参数类型（默认为True）

#### 参数详细说明
1. file, 文件路径
如果文件在当前工作目录，则可以只指定文件名，否则必须指定完整路径（绝对路径或相对路径）。

2. mode, 文件打开模式

|字符串|说明|
|:---:|---|
|'r'|读，默认值|
|'w'|写，如果文件不存在，则新建；如果已存在，则清除原有内容重写|
|'x'|独占创建，如果文件已存在，操作失败|
|'a'|追加模式，添加内容到文件末尾，文件不存在则新建|
|'t'|文本模式，默认值|
|'b'|二进制模式|
|'+'|读写模式|
|'U'|通用换行模式，deprecated|

`rwxa`可以和`bt+`进行多种组合，获得文本文件或二进制文件的各种读写模式。
默认模式为 'rt'，即读取文本文件。

### **实例**

- 文件路径

```python
# 打开当前目录下的 test.text 文件
f = open("test.txt")

# 通过完整路径指定文件
f = open("C:/Python33/README.txt")
```

由于没有指定打开模式，所以都是 'rt' 模式。

- 打开模式

```python
# 读模式
f = open("path_to_file", mode='r')

# 写模式
f = open("path_to_file", mode = 'w')

# 追加模式
f = open("path_to_file", mode = 'a')
```

- 测试
文本文件 'test.txt':

```
hello
world
how
are
you
```

以 'rt' 模式读取：

```python
with open("test.txt", "rt", encoding='UTF-8') as f:
    for line in f:
        print(line, end='')
```

输出和 'test.txt'内容完全相同。
因为 'rt'是默认模式，在 python3中，默认编码为 'UTF-8'，所以上面的 'rt'和 encoding都可以省略。
