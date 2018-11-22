import matplotlib.pyplot as plt
import pandas as pd

file1 = r"Z:\MaoJiawei\dataset-2\result\open_0.01_v7.1\pFind-raw_deltaMasses_his.csv"
file2 = r"Z:\MaoJiawei\dataset-2\result\open_0.01_v7.1\raw-pFind_deltaMasses_his.csv"
file3 = r"Z:\MaoJiawei\dataset-2\result\open_0.01_v7.1\pFind^raw_deltaMasses_his.csv"
outPath = r'Z:\MaoJiawei\dataset-2\result\open_0.01_v7.1\pFind_raw.png'

legend1 = 'Open-pFind'
legend2 = 'Raw'
legend3 = legend1 + ' ^ ' + legend2

x_lower = -500
x_upper = 500
removeNone = False

table1 = pd.read_csv(filepath_or_buffer=file1, header=None)
table2 = pd.read_csv(filepath_or_buffer=file2, header=None)
table3 = pd.read_csv(filepath_or_buffer=file3, header=None)

deltas = table1[1]
count1 = table1[3]
count2 = table2[3]
countInter = table3[3]

if removeNone:
    

width = 0.6

# do normalization
count1 = count1 / max(count1)
count2 = count2 / max(count2)
countInter = countInter / max(countInter)

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, sharex=True)
fig.subplots_adjust(hspace=0)
ax1.bar(x=deltas, height=count1, width=width, label=legend1, color='C1')
ax2.bar(x=deltas, height=count2, width=width, label=legend2, color='C2')
ax2.invert_yaxis()
ax3.bar(x=deltas, height=countInter, width=width, label=legend3, color='C0')

# 设置坐标轴属性
ax1.set_xbound(-50, 200)
yaxis = ax1.get_yaxis()
yaxis.set_label_text('PSM (relative number)')
yaxis.set_label_coords(-0.08, 0.0)

ax3.set_xlabel("Mass difference")
ax3.tick_params(left=False, labelleft=False)

# 添加 legend
ax1.legend(loc='upper right')
ax2.legend(loc='upper right')
ax3.legend(loc='upper right')

plt.savefig(outPath)
