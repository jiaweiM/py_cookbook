散点图一般用于比较两个变量，寻找相关性或者进行分组。

示例代码：

```python
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y, label='skitscat', color='k', s=25, marker="o")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
```

效果图：

![](images/scatter_1.png)

说明：
- `plt.scatter`用于绘制散点图