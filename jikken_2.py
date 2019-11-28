import numpy as np
import matplotlib.pyplot as plt

np.random.seed()
N = 100000
U = np.random.uniform(0.0,1.0,N)
ramda = 1

# 6行目で作った一様乱数を指数分布に従った乱数に変換
X = -1/ramda * np.log(1-U)

X.sort()
print(X)

counts,bins = np.histogram(X)
plt.hist(bins[:-1],bins,weights=counts/N)
plt.grid(True)


graph_list = []
tmp = 0

for i in counts:
    print(i)
    tmp += i
    graph_list.append(tmp)

graph_list = np.array(graph_list)/N
bins = bins - (bins[1]-bins[0])/2 # 横幅の調整 これが無いと棒の右端に点がプロットされる
graph_list = np.insert(graph_list,0,0)
bins[0] = 0
plt.plot(bins,graph_list,marker="o")


## ライブラリの都合で日本語が豆腐になるので調整
igfont = {'family':'Yu Gothic'}
plt.title('実験２　指数分布に従う乱数と累積相対頻度のグラフ',**igfont)
plt.xlabel('生成された乱数の値',**igfont)
plt.ylabel('生成された量',**igfont)

plt.show()
#plt.savefig("fig/fig_jikken_2.png")
