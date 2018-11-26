import random 
import os

def print_map(map):
    for i in range(len(map)):
        print(" . ".join(map[i]))

def anti_cheat(b):
    for b in range('!'):
        print(b)

def random_player(players):
    return random.choice(players)

def random_row(map):
    return random.randint(0,len(map)-1)

def random_col(map):
    return random.randint(0,len(map[0])-1)

def creat_map():
    map = []
    for i in range(0,5):
        row  = ['0','0','0','0','0']
        map.append(row)
    return map

print('Welcome to battleship','\033[94m')
print('Please enter your name\'s')
print('Type "exit" to quit game')

map = creat_map()
print_map(map)

player_1 = input("Enter 1st name: ")
player_2 = input("Enter 2nd name: ")
players = [player_1,player_2]


ship_row_1 = random_row(map)
ship_col_1 = random_col(map)

ship_row_2 = random_row(map)
ship_col_2 = random_col(map)

print_map(map)

print(random_player(players), 'starts the game')

hit_count = 0

for turn in range(4):
   while True: 
    try:
        guess_row = int(input('guess row: (allowed values: 0-4)'))
        guess_col = int(input('guess col: (allowed values: 0-4)'))
    except ValueError:
        print('OPPS....please Enter a valid number!')
        continue     
    
    if (guess_row == ship_row_1 and guess_col == ship_col_1):
        hit_count = hit_count + 1
        map[guess_row][guess_col] ='*'
    elif (guess_row == ship_row_2 and guess_col == ship_col_2):
        hit_count = hit_count + 1
        map[guess_row][guess_col] ="*"
        print("Good job!!")
        if hit_count == 1:
            print('you sunk first battleship!')
        elif hit_count == 2:
            print('you sunk second battleship')
        print_map(map)
        break
    else:   
        if (guess_row < 0 or guess_row > 5) and (guess_col < 0 or guess_col > 5):
                print("HOPPA, you sailed too far")

        elif(map[guess_row][guess_col] == 'x'):
                print('Already been chossen')
        else:
            print ('you missed')
            map[guess_row][guess_col] = 'x'
        # except ValueError:
        #     continue

        print (turn + 1,'turn')   
    print_map(map)

   
# print('1st ship is hidden:')

# print(ship_row_1)
# print(ship_col_1)

# print('2nd ship is hidden:')

# print(ship_row_2)
# print(ship_col_2)