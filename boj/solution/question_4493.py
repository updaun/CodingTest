import sys
input = sys.stdin.readline
for i in range(int(input())):
    player_1_score = 0
    player_2_score = 0
    for j in range(int(input())):
        player_1, player_2 = input().split()
        if player_1 != player_2:
            if player_1 == 'R':
                if player_2 == 'S':
                    player_1_score += 1
                else:
                    player_2_score += 1
            elif player_1 == 'S':
                if player_2 == 'P':
                    player_1_score += 1
                else:
                    player_2_score += 1
            else:
                if player_2 == 'R':
                    player_1_score += 1
                else:
                    player_2_score += 1
    if player_1_score == player_2_score:
        print('TIE')
    elif player_1_score > player_2_score:
        print('Player 1')
    else:
        print('Player 2')
