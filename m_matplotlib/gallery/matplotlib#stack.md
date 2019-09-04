堆叠图可以用于显示**部分对整体**随时间的变化关系。

堆叠图基本上类似于饼图，只是随时间而变化。

让我们考虑一下：我们一天有24小时，我们想看看我们如何花费时间。我们将时间划分为四块：
睡觉，吃饭，工作和玩耍。

绘图代码如下：
```python
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.show()
```

效果图：

![](images/stack_1.png)

说明：
- `plt.stackplot`绘制堆叠图

