#Jackpot
#-allow users to input their amount of money
#-have 'bots' input their own various amounts
#-draw a winner based on seed due to %'s
import random
import time
playAgain = 'y'
balance = 1000

print('\n' * 22)
userName = input('What is your name?: ')
time.sleep(0.1)
print()

while playAgain == 'y':
    total = 0
    print('Balance: ',balance)
    time.sleep(0.1)
    print()
    userAmount = int(input('How much money do you want to put in? (Min: 50): '))
    time.sleep(0.5)
    print()
    
    if userAmount <= balance and userAmount >= 50:
        bots = random.randint(2,4)
        if bots == 2:
            bot1Amount = random.randint(50,1000)
            bot2Amount = random.randint(50,1000)
            total = userAmount + bot1Amount + bot2Amount    
            userPercent = (userAmount / total) * 100
            bot1Percent = (bot1Amount / total) * 100
            bot2Percent = (bot2Amount / total) * 100
            userPercent = round(userPercent,1)
            bot1Percent = round(bot1Percent,1)
            bot2Percent = round(bot2Percent,1)
            print(userName,'bets',str(userAmount),'(' + str(userPercent) + '%)' + '.','Range: 0-' + str(userAmount))
            time.sleep(0.2)
            print('Bot 1 bets',str(bot1Amount),'(' + str(bot1Percent) + '%)' + '.','Range:',str(userAmount) + '-' + str(userAmount + bot1Amount))
            time.sleep(0.2)
            print('Bot 2 bets',str(bot2Amount),'(' + str(bot2Percent) + '%)' + '.','Range:',str(bot1Amount + userAmount) + '-' + str(userAmount + bot1Amount + bot2Amount))
            print('Total:',total)
            time.sleep(6)
            print()
            
        if bots == 3:
            bot1Amount = random.randint(50,1000)
            bot2Amount = random.randint(50,1000)
            bot3Amount = random.randint(50,1000)
            total = userAmount + bot1Amount + bot2Amount + bot3Amount
            userPercent = (userAmount / total) * 100
            bot1Percent = (bot1Amount / total) * 100
            bot2Percent = (bot2Amount / total) * 100
            bot3Percent = (bot3Amount / total) * 100
            userPercent = round(userPercent,1)
            bot1Percent = round(bot1Percent,1)
            bot2Percent = round(bot2Percent,1)       
            bot3Percent = round(bot3Percent,1) 
            print(userName,'bets',str(userAmount),'(' + str(userPercent) + '%)' + '.','Range: 0-' + str(userAmount))
            time.sleep(0.2)
            print('Bot 1 bets',str(bot1Amount),'(' + str(bot1Percent) + '%)' + '.','Range:',str(userAmount) + '-' + str(userAmount + bot1Amount))
            time.sleep(0.2)
            print('Bot 2 bets',str(bot2Amount),'(' + str(bot2Percent) + '%)' + '.','Range:',str(bot1Amount) + '-' + str(userAmount + bot1Amount + bot2Amount))
            time.sleep(0.2)
            print('Bot 3 bets',str(bot3Amount),'(' + str(bot3Percent) + '%)' + '.','Range:',str(bot2Amount + bot1Amount + userAmount) + '-' + str(userAmount + bot1Amount + bot2Amount + bot3Amount))
            print('Total:',total)
            time.sleep(6)
            print()

        if bots == 4:
            bot1Amount = random.randint(50,1000)
            bot2Amount = random.randint(50,1000)
            bot3Amount = random.randint(50,1000)
            bot4Amount = random.randint(50,1000)
            total = userAmount + bot1Amount + bot2Amount + bot3Amount + bot4Amount
            userPercent = (userAmount / total) * 100
            bot1Percent = (bot1Amount / total) * 100
            bot2Percent = (bot2Amount / total) * 100
            bot3Percent = (bot3Amount / total) * 100
            bot4Percent = (bot4Amount / total) * 100
            userPercent = round(userPercent,1)
            bot1Percent = round(bot1Percent,1)
            bot2Percent = round(bot2Percent,1)       
            bot3Percent = round(bot3Percent,1)     
            bot4Percent = round(bot4Percent,1)   
            print(userName,'bets',str(userAmount),'(' + str(userPercent) + '%)' + '.','Range: 0-' + str(userAmount))
            time.sleep(0.2)
            print('Bot 1 bets',str(bot1Amount),'(' + str(bot1Percent) + '%)' + '.','Range:',str(userAmount) + '-' + str(userAmount + bot1Amount))
            time.sleep(0.2)
            print('Bot 2 bets',str(bot2Amount),'(' + str(bot2Percent) + '%)' + '.','Range:',str(bot1Amount) + '-' + str(userAmount + bot1Amount + bot2Amount))
            time.sleep(0.2)
            print('Bot 3 bets',str(bot3Amount),'(' + str(bot3Percent) + '%)' + '.','Range:',str(bot2Amount + bot1Amount + userAmount) + '-' + str(userAmount + bot1Amount + bot2Amount + bot3Amount))
            time.sleep(0.2)
            print('Bot 4 bets',str(bot4Amount),'(' + str(bot4Percent) + '%)' + '.','Range:',str(bot3Amount + bot2Amount + bot1Amount + userAmount) + '-' + str(userAmount + bot1Amount + bot2Amount + bot3Amount + bot4Amount))
            print('Total:',total)
            time.sleep(6)
            print()
              
        print('Generating number...')      
        time.sleep(1.5)
        print()
        num = random.randint(1,total)
        print(num,'is drawn!')
        time.sleep(1)
        print()
        if bots == 2:
            if num < userAmount:
                print(userName,'wins!')
                result = 'won:'
                amount = (total - userAmount)
                balance = balance + total - userAmount
            elif num > userAmount:
                result = 'lost:'
                amount = userAmount
                balance = balance - userAmount
                if num < (bot1Amount + userAmount):
                    print('Bot 1 wins!')
                elif num < (bot2Amount + bot1Amount + userAmount):
                    print('Bot 2 wins!')
            
        if bots == 3:
            if num < userAmount:
                print(userName,'wins!')
                result = 'won:'
                amount = (total - userAmount)
                balance = balance + total - userAmount
            elif num > userAmount:
                result = 'lost:'
                amount = userAmount
                balance = balance - userAmount
                if num < (bot1Amount + userAmount):
                    print('Bot 1 wins!')
                elif num < (bot2Amount + bot1Amount + userAmount):
                    print('Bot 2 wins!')
                elif num < (bot3Amount + bot2Amount + bot1Amount + userAmount):
                    print('Bot 3 wins!')
                        
        if bots == 4:
            if num < userAmount:
                print(userName,'wins!')
                result = 'won:'
                amount = (total - userAmount)
                balance = balance + total - userAmount
            elif num > userAmount:
                result = 'lost:'
                amount = userAmount
                balance = balance - userAmount
                if num < (bot1Amount + userAmount):
                    print('Bot 1 wins!')
                elif num < (bot2Amount + bot1Amount + userAmount):
                    print('Bot 2 wins!')
                elif num < (bot3Amount + bot2Amount + bot1Amount + userAmount):
                    print('Bot 3 wins!')
                elif num < (bot4Amount + bot3Amount + bot2Amount + bot1Amount + userAmount):
                    print('Bot 4 wins!')
        
    if balance == 0:
        print('Balance: 0')
        print('Restart.')
        time.sleep(10)
    elif userAmount > balance or userAmount < 50:
        print('Invalid Amount! Minimum: 50, Maximum:',balance)    
    
    print()
    time.sleep(1)
    print('You',result,amount)
    time.sleep(1)
    print()
    
    if balance != 0:
        print('Would you like to play again? (y/n)')
        playAgain = input('> ')
        print('\n' * 22)
                    
        if playAgain == 'n':
            print ('Exiting Program')
            time.sleep(0.5)            
        