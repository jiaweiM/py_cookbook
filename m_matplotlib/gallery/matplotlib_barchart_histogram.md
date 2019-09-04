


# 条形图
```python
import matplotlib.pyplot as plt

plt.bar([1, 3, 5, 7, 9], [5, 2, 7, 8, 2], label="Example one")

plt.bar([2, 4, 6, 8, 10], [8, 6, 2, 5, 6], label="Example two", color='g')
plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')

plt.title('Epic Graph\nAnother Line! Whoa')

plt.show()
```
显示效果如下：

![](images/barchart_1.png)

说明：
- `plt.bar`创建条形图
- `label`用于指定 legend
- `color`用于指定颜色

# 直方图
直方图和条形图很类似，例：

```python
import matplotlib.pyplot as plt

population_ages = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102, 110, 120,
                   121, 122, 130, 111, 115, 112, 80, 75, 65, 54, 44, 43, 42, 48]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
```

效果图：

![](images/histogram_1.png)

说明：
- `plt.hist`用于绘制直方图