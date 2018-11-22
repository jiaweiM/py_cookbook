import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

'''
该例子只使用 diabetes 数据集的第一个feature，以方便使用二维图解释回归技术。

在图中可以看到一条直线，用于演示线性回归如何尝试找到一条最小化残差平方和的直线。

还计算了直线参数，残差平方和方差。
'''

# 载入 diabetes 数据集
diabetes = datasets.load_diabetes()

# 只用一个 feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# 将数据分为 training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# 将 target 也分为 training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# 创建线性回归对象
regr = linear_model.LinearRegression()

# 使用训练数据集训练模型
regr.fit(diabetes_X_train, diabetes_y_train)

# 预测测试数据集的结果
diabetes_y_pred = regr.predict(diabetes_X_test)

# 参数
print('Coefficients: \n', regr.coef_)
# 均方差
print("Mean squared error: %.2f" % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# 方差打分 variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

# 绘图
plt.scatter(diabetes_X_test, diabetes_y_test, color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())
plt.show()
