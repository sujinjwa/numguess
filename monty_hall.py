from random import shuffle, choice

doors = [0, 0, 1]

win_count = 0

for _ in range(100000):
    shuffle(doors)

    user = choice(doors)
    
    # 사용자가 선택지를 바꾸지 않은 경우
    if user == 1:
        win_count += 1