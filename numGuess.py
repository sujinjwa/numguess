import inputView
import outputView

from random import randint
from time import sleep

class Game:
    def __init__(self):
        self.inputView = inputView.InputView()
        self.outputView = outputView.OutputView()
        self.name = ''

    def start(self):
        self.name = self.inputView.read_name()
        self.outputView.printHello(self.name)

game = Game()
game.start()

# username = input('이름을 입력해주세요: ')
# print('Hello, ', username)

# # user's guess
# answer = int(input('유추한 정답을 입력해주세요: '))
# print('유추한 값: ', answer)

# # create answer
# real_answer = randint(1, 100)
# #print('실제 정답: ', real_answer)

# # compare answer with user's guess
# if answer==real_answer:
#     print('*****')
#     sleep(1)
#     print('*****')
#     sleep(1)
#     print('*****')
#     sleep(1)
#     print(f'You got it right!! The answer is {answer}\n')
# elif answer > real_answer: 
#     print(f'That was too high, {username}..')
# elif answer < real_answer:
#     print(f'That was too low, {username}..')

# # DOn't Do
# animals = ['cat', 'dog', 'dragon']

# # Do (Trailing comma)
# menus = [
#     'ramen',
#     'pasta',
#     'bear soup',
#     'salad',
# ]
