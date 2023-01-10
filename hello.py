import random

username = input('이름을 입력해주세요: ')
print('Hello, ', username)

answer = input('유추한 정답을 입력해주세요: ')
print('유추한 값: ', answer)

real_answer = random.randrange(1, 100 + 1)
print('실제 정답: ', real_answer)

# DOn't Do
animals = ['cat', 'dog', 'dragon']

# Do (Trailing comma)
menus = [
    'ramen',
    'pasta',
    'bear soup'
]
