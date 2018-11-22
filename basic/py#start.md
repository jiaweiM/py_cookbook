
# 从零开始

我们从一个完整的 Python 程序开始：

```python
SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    '''Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string

    '''
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')

if __name__ == '__main__':
    print(approximate_size(1000000000000, False))
    print(approximate_size(1000000000000))
```

将上面的代码保存为 humansize.py，通过命令行运行，获得如下结果：

```
E:\py>python humansize.py
1.0 TB
931.3 GiB
```

上面，我们成功运行了第一个 Python 程序。我们通过命令行调用 Python 解释器，将 Python 脚本名作为参数传入。
这个脚本只包含 `approximate_size()` 这一个函数，该函数将文件大小的字节表示数转换为更合适的显示方式。


## 声明函数
Python 不像 C++ 有单独的头文件，直接通过 def 关键字声明：

```Python
def approximate_size(size, a_kilobyte_is_1024_bytes=True):
```

def 关键字，后跟函数名称，括号中为函数参数，多个参数通过逗号分隔。


# 基本类型操作

**数值类型**


# 参考资料
- http://cs231n.github.io/python-numpy-tutorial/#numpy
- https://www.programiz.com/
- https://zhuanlan.zhihu.com/p/28771945