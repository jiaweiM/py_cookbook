'''
在提取成对谱图后，生成两个极度相似的轻重标谱图，它们只是在配对谱峰的强度上有差异。

'''

import pandas as pd
import matplotlib.pyplot as plt

filexx = r"G:\methyl\20151217\raw\mzML\mgfs\\pairs_xx.xlsx"
file1x = r"G:\methyl\20151217\raw\mzML\mgfs\\pairs_1x.xlsx"
file11 = r"G:\methyl\20151217\raw\mzML\mgfs\\pairs_11.xlsx"


def read_data(fileLoc):
    data = {}
    with pd.ExcelFile(fileLoc) as xlsx:
        data['intersect-target'] = pd.read_excel(xlsx, 'intersect-target', parse_cols=[5, 10])
        data['intersect-decoy'] = pd.read_excel(xlsx, 'intersect-decoy', parse_cols=[5, 10])
    data['intersect-target'].columns = ['Light Peptide Score', 'Heavy Peptide Score']
    data['intersect-decoy'].columns = ['Light Peptide Score', 'Heavy Peptide Score']
    return data


def create_graph(fileLoc, out):
    data = read_data(fileLoc)

    fig, axes = plt.subplots(figsize=(10, 8), dpi=300)

    axes.scatter(data['intersect-target']["Light Peptide Score"],
                 data['intersect-target']["Heavy Peptide Score"],
                 s=8,
                 alpha=0.5,
                 facecolor='red')
    axes.scatter(data['intersect-decoy']["Light Peptide Score"],
                 data['intersect-decoy']["Heavy Peptide Score"],
                 s=8,
                 alpha=0.5,
                 facecolor='blue')

    axes.set_xlabel('Light Peptide Score', fontsize=18)
    axes.set_ylabel('Heavy Peptide Score', fontsize=18)

    for tick in axes.yaxis.get_major_ticks():
        tick.label.set_fontsize(14)
    for tick in axes.xaxis.get_major_ticks():
        tick.label.set_fontsize(14)

    fig.savefig(out)


create_graph(file1x, "ax.png")
create_graph(file11, "aa.png")
create_graph(filexx, "xx.png")
