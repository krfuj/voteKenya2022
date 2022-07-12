import random

def vote():
    
    voteTimes = 5

    while voteTimes > 0:
        candidates = ['wajackoya', 'ruto', 'raila' , 'waihiga']

        votes = 22100000
        wajackoyaVotes = 0
        rutoVotes = 0
        railaVotes = 0
        waihigaVotes = 0
        badVotes = 0

        while (votes > 0):
            voterchoice = random.choices(candidates, weights=(8, 50, 50, 2), k=4)
            if voterchoice[0] == 'wajackoya':
                wajackoyaVotes +=1
                votes -=1
            elif voterchoice[0] == 'ruto':
                rutoVotes +=1
                votes -=1
            elif voterchoice[0] == 'raila':
                railaVotes +=1
                votes -=1
            elif voterchoice[0] == 'waihiga':
                waihigaVotes +=1
                votes -=1

        wajaPerc = round((wajackoyaVotes/21000000)*100, 2)
        global rutPer 
        rutPer = round((rutoVotes/21000000)*100, 2)
        global raiPer
        raiPer = round((railaVotes/21000000)*100, 2)
        waiPer = round((waihigaVotes/21000000)*100, 2)
        print(f"Wajackoya has: {wajackoyaVotes} Percentage: {wajaPerc} \n Ruto has: {rutoVotes} Percentage: {rutPer} \n Raila has: {railaVotes} Percentage: {raiPer} \n Waihiga has: {waihigaVotes} Percentage: {waiPer} \n")

        global rutoWins
        rutoWins = 0
        global railaWins
        railaWins = 0

            
        if rutPer > raiPer:
            rutoWins +=1
            print(rutoWins)
            voteTimes -=1
        elif raiPer > rutPer:
            raiPer +=1
            print(raiPer)
            voteTimes -=1
        elif raiPer == rutPer:
            voteTimes = 0

    if rutoWins > railaWins:
        print("Congratulations our president is: William Ruto")
    elif railaWins > rutoWins:
        print("Congratulations our president is: Raila Odinga")
    else:
        print("This calls for a rerun!!!")
        vote()
vote()
