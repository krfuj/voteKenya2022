global rutoWins
rutoWins = 0
global railaWins
railaWins = 0

voteTimes = 5

while voteTimes == 5:
        if rutPer > raiPer:
            rutoWins +=1
            voteTimes -=1
        elif raiPer > rutPer:
            raiPer +=1
            voteTimes -=1
        elif raiPer == rutPer:
            voteTimes = 0