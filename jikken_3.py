import numpy as np
import matplotlib.pyplot as plt
## とりあえずいっぱい乱数を確保
## バスが100台行くまでで計測
np.random.seed()
N = 100000
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

        for j in range(0,howmanypeople):
            hito_crowd_list.append(howmanypeople)
        bus_crowd_list.append(howmanypeople)

        howmanypeople = 0
        totaltime = 0

    if bus_count > 1000: ## 終了処理
        break

    howmanypeople += 1
    totalpeople += 1
    totaltime += i
    howlongwait_list.append(bus_kankaku[bus_count] - i)

print("\n")
print("-" * 30)
print("howlongwait_ave:" + str(np.mean(howlongwait_list))) ## 人がどれだけバスを待ったかの平均
print("\ncrowd_ave_bus:" + str(np.mean(bus_crowd_list))) ## バスから見た混雑度（バス１台あたりの混雑度 / バスの台数（100））
print("\ncrowd_ave_hito:" + str(np.mean(hito_crowd_list))) ## 人から見た混雑度（バスの１台あたりの混雑度*人数 / 総人数　）　
print("-" * 30)

#plt.plot(X,F)
#plt.hist(bus_kankaku,nbins)
#plt.hist(hito_kankaku,nbins)
#plt.show()
