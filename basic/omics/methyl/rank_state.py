import pandas as pd
import matplotlib.pyplot as plt

filexx = r"G:\methyl\20151217\raw\mzML\mgfs\\pairs_xx.xlsx"

'''
首先，读取数据
'''
data = {}
with pd.ExcelFile(filexx) as xlsx:
    data['intersect-target'] = pd.read_excel(xlsx, 'intersect-target')
    data['intersect-decoy'] = pd.read_excel(xlsx, 'intersect-decoy')

'''
然后，根据 rank 进行分类
'''


def category_byrank(df):
    """
    :rtype: tuples of rank11, rank1x, rankxx score list
    """
    rank11 = []
    rank1x = []
    rankxx = []
    for index, data in df.iterrows():
        light_rank = data[6]
        heavy_rank = data[11]
        light_score = data[5]
        heavy_score = data[10]
        if light_rank == 1 and heavy_rank == 1:
            rank11.append((light_score, heavy_score))
        elif light_rank == 1 or heavy_rank == 1:
            rank1x.append((light_score, heavy_score))
        else:
            rankxx.append((light_score, heavy_score))
    return rank11, rank1x, rankxx


'''根据对应的 rank 打分数据绘图'''


def create_graph(target_scores, decoy_scores, out):
    fig, axes = plt.subplots(figsize=(10, 8), dpi=300)

    target_light = []
    target_heavy = []
    for light, heavy in target_scores:
        target_light.append(light)
        target_heavy.append(heavy)

    decoy_light = []
    decoy_heavy = []
    for light, heavy in decoy_scores:
        decoy_light.append(light)
        decoy_heavy.append(heavy)

    light_data = target_light + decoy_light
    heavy_data = target_heavy + decoy_heavy
    light_series = pd.Series(light_data)
    heavy_series = pd.Series(heavy_data)

    corr = light_series.corr(heavy_series)

    axes.scatter(target_light,
                 target_heavy,
                 s=8,
                 alpha=0.5,
                 facecolor='red')
    axes.scatter(decoy_light,
                 decoy_heavy,
                 s=8,
                 alpha=0.5,
                 facecolor='blue')

    axes.set_xlabel('Light Peptide Score', fontsize=18)
    axes.set_ylabel('Heavy Peptide Score', fontsize=18)
    plt.text(0.2, 0.8, r"corr=" + str(corr), transform=axes.transAxes)

    for tick in axes.yaxis.get_major_ticks():
        tick.label.set_fontsize(14)
    for tick in axes.xaxis.get_major_ticks():
        tick.label.set_fontsize(14)

    print(len(target_light))
    print(len(decoy_light))

    fig.savefig(out)


def fdr_state(data):
    target_data = data['intersect-target']
    decoy_data = data['intersect-decoy']

    target_data.sort_values(by=target_data.columns[5], ascending=False)
    decoy_data.sort_values(by=decoy_data.columns[5], ascending=False)

    for index, row in data.iterrows():
        light_rank = data[6]
        heavy_rank = data[11]
        light_prot = data[4]
        heavy_prot = data[9]


    pass


target_scores = category_byrank(data['intersect-target'])
decoy_scores = category_byrank(data['intersect-decoy'])

create_graph(target_scores[0], decoy_scores[0], 'xx_rank11.png')
create_graph(target_scores[1], decoy_scores[1], 'xx_rank1x.png')
create_graph(target_scores[2], decoy_scores[2], 'xx_rankxx.png')
