
matplotlib-venn 对 matplotlib 进行了扩展，可用于绘制简单的韦恩图。

matplotlib-venn 包括4个主要函数：venn2, venn2_circles, venn3, venn3_circles.
venn2 和 venn3 用于绘制韦恩图，venn2_circles 和 venn3_circles 则仅绘制边框，可用于美化韦恩图。

它们大同小异，下面以 venn2 为例说明如何使用该库画图。

## venn2
venn2 函数用于绘制包含两个数据集的 Venn 图。

```python
venn2(subsets, set_labels=('A', 'B'), set_colors=('r', 'g'), alpha=0.4, normalize_to=1.0, ax=None, subset_label_formatter=None)
```

参数说明：

`subsets` 可以为下面任意一种参数：
- list (或 tuple)，包含两个数据集对象.
- dict, 提供三个区域的大小。不同区域通过两个数字标识（"10", "01", "11"），分别对应A数据集独有，B数据集独有，和AB数据集的交集的大小。
- list (或 tuple)，包含三个数据，按照(10, 01, 11)顺序提供不同区域的大小。

`set_labels` 包含两个字符串的 list。设置为 None则取消标签。

`set_colors` 包含两个颜色值，两个圆交集的颜色根据这两个颜色计算而来。

`normalize_to` 设置绘制圆圈的总体大小。

`ax` 指定绘制图的坐标，默认为当前坐标系。

`subset_label_formatter` 用于设置标签的格式。

##### 例 1 按照指定大小绘制
通过 `subsets` 指定其大小，如下：

```python
from matplotlib_venn import venn2
import matplotlib.pyplot as plt

plt.figure(figsize=(4, 4))
venn2(subsets=(3, 2, 1))
plt.show()
```

(3, 2, 1) 分别指定了Ab, Ba, AB 的大小。效果图：

![](images/venn_1.png)

##### 例 2 提供两个集合，绘制韦恩图

```python
set1 = {'A', 'B', 'C', 'D', 'E'}
set2 = {'C', 'D', 'F', 'G'}

venn2([set1, set2])
```

集合1包含5个元素，集合2包含4个，两者交集包含2个，效果图：

![](images/venn_2.png)

## venn3
venn3 类似于 venn2，对三个集合，有如下的情况：Abc, aBc, ABc, abC, AbC, aBC, ABC。

Abc 表示A有，b，c没有，其他类似；ABC表示 A,B,C 的交集。

venn2_unweighted 和 venn3_unweighted 绘制韦恩图的大小和数据不成正比。

##### 例 3 使用 venn3 绘制韦恩图

```python
from matplotlib_venn import venn3
import matplotlib.pyplot as plt

plt.figure(figsize=(4, 4))
venn3(subsets=(1, 1, 1, 2, 1, 2, 2), set_labels=('Set1', 'Set2', 'Set3'))
plt.show()
```

使用 subsets 指定了各个区域的大小，效果图：

![](images/venn_3.png)

##### 例 4 venn3 设置属性

```python
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3, venn3_circles

# Subset sizes
s = (
    2,  # Abc
    3,  # aBc
    4,  # ABc
    3,  # abC
    1,  # AbC
    0.5,  # aBC
    4,  # ABC
)

v = venn3(subsets=s, set_labels=('A', 'B', 'C'))

# Subset labels
v.get_label_by_id('100').set_text('Abc')
v.get_label_by_id('010').set_text('aBc')
v.get_label_by_id('110').set_text('ABc')
v.get_label_by_id('001').set_text('Abc')
v.get_label_by_id('101').set_text('aBc')
v.get_label_by_id('011').set_text('ABc')
v.get_label_by_id('111').set_text('ABC')

# Subset colors
v.get_patch_by_id('100').set_color('c')
v.get_patch_by_id('010').set_color('#993333')
v.get_patch_by_id('110').set_color('blue')

# Subset alphas
v.get_patch_by_id('101').set_alpha(0.4)
v.get_patch_by_id('011').set_alpha(1.0)
v.get_patch_by_id('111').set_alpha(0.7)

# Border styles
c = venn3_circles(subsets=s, linestyle='solid')
c[0].set_ls('dotted')  # Line style
c[1].set_ls('dashed')
c[2].set_lw(1.0)  # Line width

plt.show()
```

效果图

![](images/venn_4.png)



# 参考资料

- [https://pypi.python.org/pypi/matplotlib-venn](https://pypi.python.org/pypi/matplotlib-venn)
