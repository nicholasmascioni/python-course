import random

name = input("Enter your name: ")
print("Hello, " + name)

score = 0

leaderboard = open('rating.txt', 'r')

for score_line in leaderboard:
    score_name, score_value = score_line.split(' ')
    if score_name == name:
        score += int(score_value)

leaderboard.close()

game_options = input("Choose which options to include, separated by commas."
                     " Leave blank for only rock, paper and scissors"
                     "(i.e. rock,paper,scissors,dragon): ")
options_list = game_options.split(sep=',')

if game_options == "":
    options_list = ['rock', 'paper', 'scissors']

print("Okay, let's start")
# print(options_list)  # Debugging

# Dictates all losing matchups for all available options
matchups = {
    'rock': ('gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'),
    'gun': ('lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'),
    'lightning': ('devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'),
    'devil': ('dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'),
    'dragon': ('water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'),
    'water': ('air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'),
    'air': ('paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'),
    'paper': ('sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'),
    'sponge': ('wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'),
    'wolf': ('tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'),
    'tree': ('human', 'snake', 'scissors', 'fire', 'rock', 'gun', 'lightning'),
    'human': ('snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'),
    'snake': ('scissors', 'fire', 'rock', 'gun', 'lightning', 'devil', 'dragon'),
    'scissors': ('fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'),
    'fire': ('rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air')
}

while True:
    # Computer selects a number from 0 --> len(options_list) - 1
    CPU_option_index = random.randint(0, len(options_list)-1)
    CPU_option = options_list[CPU_option_index]
    # Get what user picks:
    option = input()

    if option == '!rating':
        print("Your rating: ", score)
        continue

    if option == '!exit':
        print('Bye!')
        break

    if option not in options_list:
        print("Invalid input")
        continue

    if option == CPU_option:  # A draw
        print('There is a draw (' + option + ')')
        score += 50
        continue
    if option in matchups[CPU_option]:  # User wins
        print('Well done. Computer chose ' + CPU_option + ' and failed')
        score += 100
        continue
    if CPU_option in matchups[option]:  # User loses
        print('Sorry, but the computer chose ' + CPU_option)
        continue
