from pprint import pprint

file = open("log1.txt", "a", encoding="UTF-8")
file.write("--- 実行 ---")

file2 = open("log2.txt", "a", encoding="UTF-8")
file2.write("--- 実行 ---")

# const
sakanobasyo = 1500
kurumanodaisuu = 75

# 初期化
speed = [20]  # 20m/s = 72km/h
kyori = [12 * (kurumanodaisuu - 1)]
status1 = [0]  # 坂を上がったかどうかのステータス 0開始まえ -> 6終了
status2 = [0]  # 車間距離が少なくなっているかのステータス -1広すぎ 0ちょうど 1狭すぎ
for i in range(kurumanodaisuu - 1): # 車を50台分登録
    speed.append(20)
    kyori.append((12 * (kurumanodaisuu - 2)) - (i * 12))
    status1.append(0)
    status2.append(0)

for s in range(500): # 500回繰り返す
    for carno in range(kurumanodaisuu): # carno = Car No.

        kyori[carno] += speed[carno] # 距離を加算

        if status1[carno] == 0 and kyori[carno] >= sakanobasyo and speed[carno] != 0: # 坂による減速
            speed[carno] -= 1
            status1[carno] += 1
        elif status1[carno] == 1:
            speed[carno] -= 1
            status1[carno] += 1
        elif status1[carno] == 2:
            speed[carno] -= 1
            status1[carno] += 1
        elif status1[carno] == 3:
            speed[carno] += 1
            status1[carno] += 1
        elif status1[carno] == 4:
            speed[carno] += 1
            status1[carno] += 1
        elif status1[carno] == 5:
            speed[carno] += 1
            status1[carno] += 1

        if carno != 0: # 車間距離による減速 もし先頭の車じゃなければ
            if status2[carno] == 1 and speed[carno] != 0:
                if speed[carno] > 4:
                    speed[carno] -= 3
                else:
                    speed[carno] = 0
            elif status2[carno] == -1 and speed[carno] < 23:
                speed[carno] += 3
            if (kyori[carno - 1]) - kyori[carno] < 12: # もし車間距離が12m未満なら
                status2[carno] = 1
            elif (kyori[carno - 1]) - kyori[carno] > 12: # もし 車間距離が12mより大きい なら
                status2[carno] = -1
            else:
                status2[carno] = 0

    print("◆" + str(s + 1) + "秒目◆", file=file)
    print("◇速度", file=file)
    pprint(speed, stream=file, compact=True, width=1000)
    print("◇距離", file=file)
    pprint(kyori, stream=file, compact=True, width=1000)
    if (s + 1) % 10 == 0:
        print("◆" + str(s + 1) + "秒目◆", file=file2)
        pprint(speed, stream=file2, compact=True, width=1000)

file.close()