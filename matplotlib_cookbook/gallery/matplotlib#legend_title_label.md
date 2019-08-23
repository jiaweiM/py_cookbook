
目的:

给图添加图例(legend)、标题(title)和标签(label)。

# pyplot 风格

```python
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 7, 4]

x2 = [1, 2, 3]
y2 = [10, 14, 12]

plt.plot(x, y, label='First Line')
plt.plot(x2, y2, label='Second Line')

plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Interesting Graph\nCheck it out')
plt.legend()

plt.show()
```

效果图：

![](images/label_1.png)

**总结**

|函数|说明|
|---|---|
|pyplot.xlabel("a label")|设置 X 轴标签|
|pyplot.ylabel("a label")|设置 Y 轴标签|
|pyplot.title("a title")|设置标题|
|pyplot.legend()|显示图例|
|pyplot.plot(x, y, label="a label")|绘制图形，并通过 label指定图例|
