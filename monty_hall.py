from random import shuffle, choice

doors = [0, 0, 1]

win_count = 0

for _ in range(100000):
    shuffle(doors)

    user = choice(doors)
    
    # 사용자가 선택지를 바꾸지 않은 경우
    if user == 1:
        win_count += 1

win_percentage = round((100000 - win_count) / 100000 * 100, 2)

print('사용자가 선택지를 변경하지 않은 경우 성공 횟수: ', win_count)
print('사용자가 선택지를 변경한 경우 성공 횟수:', 100000 - win_count)
print('선택지를 변경할 경우 성공할 확률: ', win_percentage, '%')