from pprint import pprint

file = open("log1.txt", "a", encoding="UTF-8")
file.write("--- 実行 ---")

# const
sakanobasyo = 100
kurumanodaisuu = 50

# 初期化
speed = [20]  # 20m/s = 72km/h
kyori = [0]
status1 = [0]  # 坂を上がったかどうかのステータス 0開始まえ -> 3終了
status2 = [0]  # 車間距離が少なくなっているかのステータス -1広すぎ 0ちょうど 1狭すぎ
for i in range(kurumanodaisuu - 1): # 車を50台分登録
    speed.append(20)
    kyori.append((i * kurumanodaisuu) - (i * 10))
    status1.append(0)
    status2.append(0)

for s in range(100): # 100回繰り返す
    for carno in range(kurumanodaisuu): # carno = Car No.

        kyori[carno] += speed[carno] # 距離を加算

        if status1[carno] == 0 and kyori[carno] >= 100: # 坂による減速
            speed[carno] -= 1
            status1[carno] += 1
        if status1[carno] == 1:
            status1[carno] += 1
        if status1[carno] == 2:
            speed[carno] += 1
            status1[carno] += 1

        if carno != 0: # 車間距離による減速 もし先頭の車じゃなければ
            if status2[carno] == 1:
                speed[carno] -= 1
            elif status2[carno] == -1:
                speed[carno] += 1
            if kyori[carno] - (kyori[carno] - 1) < 25: # もし車間距離が25m未満なら
                status2[carno] = 1
            elif kyori[carno] - (kyori[carno] - 1) > 30: # もし 車間距離が30mより大きい なら
                status2[carno] = -1

    print("◆" + str(s) + "秒目◆", file=file)
    print("◇速度", file=file)
    pprint(speed, stream=file)
    print("◇距離", file=file)
    pprint(kyori, stream=file)

file.close()