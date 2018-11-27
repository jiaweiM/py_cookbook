import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file1 = r"Z:\MaoJiawei\dataset-2\result\open_0.01_v7.1\cp_intensify_msfragger-raw_deltaMasses_his.csv"
file2 = r"Z:\MaoJiawei\dataset-2\result\open_0.01_v7.1\raw-cp_intensify_msfragger_deltaMasses_his.csv"
file3 = r"Z:\MaoJiawei\dataset-2\result\open_0.01_v7.1\cp_intensify_msfragger^raw_deltaMasses_his.csv"
outPath = r'Z:\MaoJiawei\dataset-2\result\open_0.01_v7.1\cp_intensify_msfragger_raw.png'

legend1 = 'Complementary Intensify + MSFragger'
# legend1 = 'Complementary intensify'
# legend1 = 'Deconvolution'
# legend1 = 'MSFragger'
legend2 = 'Raw'
legend3 = legend1 + ' ^ ' + legend2

x_lower = -50
x_upper = 350
y_lower = 0.0
y_upper = 1.0
removeNone = True  # 移除无修饰部分的数据，即 [-1.2,1.2] 区间之间的数据，因为它们强度太高，影响其他数据的展示
doNormalization = False  # 以2.0 处的值归一化数据，对应 index 5020，默认以最高强度的作为 normalization 值

table1 = pd.read_csv(filepath_or_buffer=file1, header=None)
table2 = pd.read_csv(filepath_or_buffer=file2, header=None)
table3 = pd.read_csv(filepath_or_buffer=file3, header=None)

deltas = table1[1]
count1 = table1[3]
count2 = table2[3]
countInter = table3[3]

# 移除 delta masses [-1.2,1.2] 范围内的值
if removeNone:
    indexes = np.arange(4988, 5012)
    for index in indexes:
        count1.iat[index] = 0
        count2.iat[index] = 0
        countInter.iat[index] = 0

width = 0.6

# do normalization
nor1 = 0
nor2 = 0
nor3 = 0
if doNormalization:
    nor1 = count1.iat[5020]
    nor2 = count2.iat[5020]
    nor3 = countInter.iat[5020]
    y_upper = 30
else:
    nor1 = max(count1)
    nor2 = max(count2)
    nor3 = max(countInter)

count1 = count1 / nor1
count2 = count2 / nor2
countInter = countInter / nor3

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, sharex=True)
fig.subplots_adjust(hspace=0)
ax1.bar(x=deltas, height=count1, width=width, label=legend1, color='C1')
ax2.bar(x=deltas, height=count2, width=width, label=legend2, color='C2')
ax2.invert_yaxis()
ax3.bar(x=deltas, height=countInter, width=width, label=legend3, color='C0')

# 设置坐标轴属性
ax1.set_xbound(x_lower, x_upper)
yaxis = ax1.get_yaxis()
yaxis.set_label_text('PSM (relative number)')
yaxis.set_label_coords(-0.08, 0.0)

# ax1.set_ybound(y_lower, y_upper)
# ax2.set_ybound(y_lower, y_upper)
# ax3.set_ybound(y_lower, y_upper)

ax3.set_xlabel("Mass difference")
ax3.tick_params(left=False, labelleft=False)

# 添加 legend
ax1.legend(loc='upper right')
ax2.legend(loc='upper right')
ax3.legend(loc='upper right')

# 设置大小
# print(fig.get_size_inches())
# fig.set_size_inches(6.4, 4.8)

plt.savefig(outPath, dpi=300)
# plt.show()
