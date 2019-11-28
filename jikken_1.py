import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as ticker
np.random.seed()
N = 100000

# 0か1しかないのに横軸に小数点が出てくるのは気持ち悪いので整数のみ出力されるようにする
plt.gca().get_xaxis().set_major_locator(ticker.MaxNLocator(integer=True))

plt.ylim([0,1])

list = []

delta = 1
p = 0.1
U = np.random.uniform(0.0,1.0,N) # 0.から1.までの乱数生成
for i in U:
    # 生成した乱数がdelta/p以下ならリストの終わりに1を追加
    # そうでないならリストの終わりに0を追加
    if i <= p:
        list.append(1)
    else:
        list.append(0)

print(np.mean(list))
print(np.var(list))

count = 0
kankaku_list = []
for i in list:
    print("-"*10)
    count += 1
    print(count)
    print(i)
    if i == 1:
        kankaku_list.append(count)
        count = 0



counts,bins = np.histogram(kankaku_list)
print(np.mean(kankaku_list))
plt.hist(bins[:-1],bins,weights=counts/list.count(1))
plt.grid(True)

## 業務用 ライブラリの都合で日本語が豆腐になるので調整
igfont = {'family':'Yu Gothic'}
plt.title('実験１　δ=1,p=0.1に基づくベルヌーイ過程に基づく乱数の到着感覚の分布',**igfont)
plt.xlabel('生成された乱数（０：未到着　１：到着）',**igfont)
plt.ylabel('全体に占める割合',**igfont)
plt.show()
