`type()` 函数可以获取参数对象类型

# 语法

```python
type(object)
type(name, bases, dict)
```

## 1. type(object)
单参数类型，返回对象类型，和 `object.__class__` 相同。

#### 例 1 获得对象类型

```python
numberList = [1, 2]
print(type(numberList))

numberDict = {1: 'one', 2: 'two'}
print(type(numberDict))

class Foo:
    a = 0

InstanceOfFoo = Foo()
print(type(InstanceOfFoo))
```

输出：

```
<class 'list'>
<class 'dict'>
<class '__main__.Foo'>
```

如果需要检查对象类型，推荐使用 `isinstance` 函数，因为 `type()`判断类型比较严格，type()不会认为子类是一种父类类型，而 `isinstance` 则会认为子类是一种父类类型。如下所示：

```python
class Shape():
    pass

class Circle(Shape):
    pass

print(type(Shape()) == Shape)
print(type(Circle()) == Shape)
print(isinstance(Circle(), Shape))
```

输出为：

```
True
False
True
```

使用 type 判断，Circle 是 Shape 子类，然而 `type(Circle()) == Shape` 为 False。

**所以在类型判断上，用 `isinstance` 更合适。**


## 2. `type(name, bases, dict)` 形式
返回一个新的类型对象。可以将其看做动态类型的 class 声明。

参数说明
- *name*, 类名，`__name__` 属性值
- *bases*, tuple，枚举所有基类，为 `__bases__` 属性值。
- *dict*, 命名空间包含定义，为 `__dict__` 属性值。
