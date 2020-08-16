scores = input().split()
# put your python code here
count_wins = 0
count_losses = 0
for score in scores:
    if score == 'C':
        count_wins += 1
    else:
        count_losses += 1
    if count_losses == 3:
        break
if count_losses < 3:
    print("You won\n{wins}".format(wins=count_wins))
else:
    print("Game over\n{losses}".format(losses=count_wins))
