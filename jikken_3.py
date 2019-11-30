import numpy as np
import matplotlib.pyplot as plt

"""

### 実験番号に対応した部分にコメントを振ってあります
### 実験3-1を行うときには実験3-2と3-3はコメントアウトしてください
### ほかについても同様です　コメントアウトしないと多分ぶっ壊れます

"""



## とりあえずいっぱい乱数を確保
## バスが100台行くまでで計測
np.random.seed()
N = 500000
U = np.random.uniform(0.0,1.0,N)
np.random.seed()
U2 = np.random.uniform(0.0,1.0,N*10)
X = np.linspace(0,25)

nbins = 50
ramda_1 = 0.1
ramda_2 = 10

F = ramda_2 * np.exp(-1*ramda_2*X)
bus_kankaku = (-1/ramda_1) * np.log(1-U)
hito_kankaku = (-1/ramda_2) * np.log(1-U)

print("bus")
print(bus_kankaku)

print("hito")
print(hito_kankaku)

bus_count = 1
howmanypeople = 0
totaltime = 0
totalpeople = 0
howlongwait = 0
howlongwait_list = []
hito_crowd_list = []
bus_crowd_list = []

for i in hito_kankaku:
    if bus_kankaku[bus_count] <= totaltime-i:
        output = \
        "\n\nbasu ga kita zikoku : " + str(bus_kankaku[bus_count]) + "  hun\n" + \
        "kita ninzuu  " + str(howmanypeople) + "  nin\n" + \
        "matta zikan  " + str(totaltime-i) + "  hun\n" + \
        "count  " + str(bus_count)

        print(output)

        bus_count += 1

        # 人から見たバスの混雑
        # 乗客100人のバスの場合は乗客100人が混んでいると判断する
        # 逆に乗客が1人の場合は1人しか空いていると判断しない
        for j in range(0,howmanypeople):
            hito_crowd_list.append(howmanypeople)
        # バスから見た人の混雑
        bus_crowd_list.append(howmanypeople)

        howmanypeople = 0
        totaltime = 0

    if bus_count > 1000: ## 1000台バスを見たら終了処理
        break

    howmanypeople += 1
    totalpeople += 1
    totaltime += i
    howlongwait_list.append(bus_kankaku[bus_count] - i)

## 業務用 ライブラリの都合で日本語が豆腐になるので調整
igfont = {'family':'Yu Gothic'}

nbins = 20
print("-"*50)
# 実験3-1 バスから見た混雑具合の平均
#"""
print("\ncrowd_ave_bus:" + str(np.mean(bus_crowd_list))) ## バスから見た混雑度（バス１台あたりの混雑度 / バスの台数（100））
plt.hist(bus_crowd_list,nbins,ec='black',range=(0,1000))
plt.vlines([np.mean(bus_crowd_list)],-1,500,"red",linestyle="solid")
plt.title('実験3-1　$λ_1$=0.1 $λ_2$=1の時のバスから見た混雑度',**igfont)
plt.xlabel('混雑具合',**igfont)
plt.ylabel('バスの台数',**igfont)
plt.show()

#"""

# 実験3-2 乗客から見たバスの混雑具合の平均
"""
print("\ncrowd_ave_hito:" + str(np.mean(hito_crowd_list))) ## 人から見た混雑度（バスの１台あたりの混雑度*人数 / 総人数　）　
plt.hist(hito_crowd_list,nbins,ec='black',range=(0,1000))
plt.vlines([np.mean(hito_crowd_list)],-1,20000,"red",linestyle="solid")

plt.title('実験3-2　$λ_1$=0.1 $λ_2$=1の時の人から見た混雑度',**igfont)
plt.xlabel('同乗者の数',**igfont)
plt.ylabel('同乗者がいると感じている人数',**igfont)
plt.show()
"""

# 実験3-3 乗客の待ち時間の平均値と分布
"""
print("howlongwait_ave:" + str(np.mean(howlongwait_list))) ## 人がどれだけバスを待ったかの平均
plt.hist(howlongwait_list,nbins,ec='black')
plt.vlines([np.mean(howlongwait_list)],-1,20000,"red",linestyle="solid")
plt.title('実験3-3　$λ_1$=0.1 $λ_2$=1の時の待ち時間',**igfont)
plt.xlabel('待ち時間',**igfont)
plt.ylabel('待った人の数',**igfont)
plt.show()

"""
