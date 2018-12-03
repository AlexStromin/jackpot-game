#Jackpot
#-allow users to input their amount of money
#-have 'bots' input their own various amounts
#-draw a winner based on seed due to %'s
import random
import time
playAgain = 'y'
balance = 1000

print('\n' * 66)
time.sleep(0.5)
print('What is your name?')
userName = input('> ')
time.sleep(0.5)
print()

while playAgain == 'y':
    
    bot1name = ['Robert', 'Chelsea', 'Rebecca', 'Max', 'Victor', 'Joshua', 'Conrad', 'Benjamin', 'Robin', 'Gene']
    bot2name = ['Frank', 'Jessica', 'James', 'Michael', 'Joseph', 'Christine', 'Matthew', 'Jennifer', 'Linda', 'Thomas']
    bot3name = ['Lisa', 'Mark', 'Paul', 'Steven', 'Emily', 'Michelle', 'Helen', 'Brian', 'Edward', 'Sharon']
    
    bot1 = random.choice(bot1name)
    bot2 = random.choice(bot2name)
    bot3 = random.choice(bot3name)
    
    bot1pos = 0
    bot2pos = 0
    bot3pos = 0  
    
    pos1 = ''
    pos2 = ''
    pos3 = ''
    pos4 = ''
    
    pos1Amount = 0
    pos2Amount = 0
    pos3Amount = 0
    pos4Amount = 0
    
    pos1Percent = 0
    pos2Percent = 0
    pos3Percent = 0
    pos4Percent = 0  
    
    
    v = [1,2]
    vv = [2,3]
    vvv = [1,3]
    
    total = 0
    print('Balance: $' + str(balance))
    print()
    print('Low = $50 -> $500')
    print('Medium = $500 -> $2000')
    print('High = $2000 -> $10000')
    print()
    print('Which pot would you like to enter?')
    potTier = input('> ')
    time.sleep(0.5)
    while potTier != 'Low' and potTier != 'Medium' and potTier != 'High' and potTier != 'low' and potTier != 'medium' and potTier != 'high' :
        print()
        print('Invalid Pot type. (Low,Medium,High)')
        potTier = input('> ')
        time.sleep(0.5)
    print()
    print('How much money do you want to put in?')
    while True:
        try:
            userAmount = int(input('> $'))
            time.sleep(0.5)
            break
        except ValueError:
            print()
            print('How much money do you want to put in?')
            pass
    while (potTier == 'Low' or potTier == 'low') and (userAmount < 50 or userAmount > 500):
        print()
        print('Invalid amount, Low Pot bets must be between $50 and $500.')
        while True:
            try:
                userAmount = int(input('> $'))
                time.sleep(0.5)
                break
            except ValueError:
                print()
                print('Invalid amount, Low Pot bets must be between $50 and $500.')
                pass            
    while (potTier == 'Medium' or potTier == 'medium') and (userAmount < 500 or userAmount > 2000):
        print()
        print('Invalid amount, Medium Pot bets must be between $500 and $2000.')
        while True:
            try:
                userAmount = int(input('> $'))
                time.sleep(0.5)
                break
            except ValueError:
                print()
                print('Invalid amount, Medium Pot bets must be between $500 and $2000.')
                pass            
    while (potTier == 'High' or potTier == 'high') and (userAmount < 2000 or userAmount > 10000):
        print()
        print('Invalid amount, High Pot bets must be between $2000 and $10000.')
        while True:
            try:
                userAmount = int(input('> $'))
                time.sleep(0.5)
                break
            except ValueError:
                print()
                print('Invalid amount, High Pot bets must be between $2000 and $10000.')
                pass            
    print()
    if userAmount <= balance and userAmount >= 50 and (potTier == 'Low' or potTier == 'low'):
        bots = random.randint(2,3)
        if bots == 2:
            bot1Amount = random.randint(50,500)
            bot2Amount = random.randint(50,500)
            total = userAmount + bot1Amount + bot2Amount    
            userPercent = (userAmount / total) * 100
            bot1Percent = (bot1Amount / total) * 100
            bot2Percent = (bot2Amount / total) * 100
            userPercent = round(userPercent,1)
            bot1Percent = round(bot1Percent,1)
            bot2Percent = round(bot2Percent,1)
            userpos = random.randint(1,3)
            bot1pos = random.randint(1,3)
            bot2pos = random.randint(1,3)
            while userpos == bot1pos or userpos == bot2pos or bot1pos == userpos or bot1pos == bot2pos or bot2pos == userpos or bot2pos == bot1pos:
                userpos = random.randint(1,3)
                bot1pos = random.randint(1,3)
                bot2pos = random.randint(1,3)        
            if userpos == 1:
                pos1 = userName
                pos1Percent = userPercent
                pos1Amount = userAmount
            if userpos == 2:
                pos2 = userName
                pos2Percent = userPercent
                pos2Amount = userAmount
            if userpos == 3:
                pos3 = userName
                pos3Percent = userPercent
                pos3Amount = userAmount
            if bot1pos == 1:
                pos1 = bot1
                pos1Percent = bot1Percent
                pos1Amount = bot1Amount
            if bot1pos == 2:
                pos2 = bot1
                pos2Percent = bot1Percent
                pos2Amount = bot1Amount
            if bot1pos == 3:
                pos3 = bot1
                pos3Percent = bot1Percent
                pos3Amount = bot1Amount   
            if bot2pos == 1:
                pos1 = bot2
                pos1Percent = bot2Percent
                pos1Amount = bot2Amount
            if bot2pos == 2:
                pos2 = bot2
                pos2Percent = bot2Percent
                pos2Amount = bot2Amount
            if bot2pos == 3:
                pos3 = bot2
                pos3Percent = bot2Percent
                pos3Amount = bot2Amount  
            print(pos1,'bets $' + str(pos1Amount),'(' + str(pos1Percent) + '%)','Range: 0-' + str(pos1Amount))
            time.sleep(0.5)
            print(pos2,'bets $' + str(pos2Amount),'(' + str(pos2Percent) + '%)','Range:',str(pos1Amount) + '-' + str(pos1Amount + pos2Amount))
            time.sleep(0.5)
            print(pos3,'bets $' + str(pos3Amount),'(' + str(pos3Percent) + '%)','Range:',str(pos2Amount + pos1Amount) + '-' + str(pos1Amount + pos2Amount + pos3Amount))
            time.sleep(0.5)
            print()
            time.sleep(0.5)
            print('Total Jackpot: $' + str(total))
            time.sleep(0.5)
            print()
            
        if bots == 3:
            bot1Amount = random.randint(50,500)
            bot2Amount = random.randint(50,500)
            bot3Amount = random.randint(50,500)
            total = userAmount + bot1Amount + bot2Amount + bot3Amount
            userPercent = (userAmount / total) * 100
            bot1Percent = (bot1Amount / total) * 100
            bot2Percent = (bot2Amount / total) * 100
            bot3Percent = (bot3Amount / total) * 100
            userPercent = round(userPercent,1)
            bot1Percent = round(bot1Percent,1)
            bot2Percent = round(bot2Percent,1)       
            bot3Percent = round(bot3Percent,1) 
            userpos = random.randint(1,4)
            bot1pos = random.randint(1,4)
            bot2pos = random.randint(1,4)
            bot3pos = random.randint(1,4)
            while userpos == bot1pos or userpos == bot2pos or userpos == bot3pos or bot1pos == userpos or bot1pos == bot2pos or bot1pos == bot3pos or bot2pos == userpos or bot2pos == bot1pos or bot2pos == bot3pos or bot3pos == userpos or bot3pos == bot1pos or bot3pos == bot2pos:
                userpos = random.randint(1,4)
                bot1pos = random.randint(1,4)
                bot2pos = random.randint(1,4)
                bot3pos = random.randint(1,4)                
            if userpos == 1:
                pos1 = userName
                pos1Percent = userPercent
                pos1Amount = userAmount
            if userpos == 2:
                pos2 = userName
                pos2Percent = userPercent
                pos2Amount = userAmount
            if userpos == 3:
                pos3 = userName
                pos3Percent = userPercent
                pos3Amount = userAmount
            if userpos == 4:
                pos4 = userName
                pos4Percent = userPercent
                pos4Amount = userAmount
            if bot1pos == 1:
                pos1 = bot1
                pos1Percent = bot1Percent
                pos1Amount = bot1Amount
            if bot1pos == 2:
                pos2 = bot1
                pos2Percent = bot1Percent
                pos2Amount = bot1Amount
            if bot1pos == 3:
                pos3 = bot1
                pos3Percent = bot1Percent
                pos3Amount = bot1Amount   
            if bot1pos == 4:
                pos4 = bot1
                pos4Percent = bot1Percent
                pos4Amount = bot1Amount 
            if bot2pos == 1:
                pos1 = bot2
                pos1Percent = bot2Percent
                pos1Amount = bot2Amount
            if bot2pos == 2:
                pos2 = bot2
                pos2Percent = bot2Percent
                pos2Amount = bot2Amount
            if bot2pos == 3:
                pos3 = bot2
                pos3Percent = bot2Percent
                pos3Amount = bot2Amount   
            if bot2pos == 4:
                pos4 = bot2
                pos4Percent = bot2Percent
                pos4Amount = bot2Amount 
            if bot3pos == 1:
                pos1 = bot3
                pos1Percent = bot3Percent
                pos1Amount = bot3Amount
            if bot3pos == 2:
                pos2 = bot3
                pos2Percent = bot3Percent
                pos2Amount = bot3Amount
            if bot3pos == 3:
                pos3 = bot3
                pos3Percent = bot3Percent
                pos3Amount = bot3Amount
            if bot3pos == 4:
                pos4 = bot3
                pos4Percent = bot3Percent
                pos4Amount = bot3Amount 
            print(pos1,'bets $' + str(pos1Amount),'(' + str(pos1Percent) + '%)','Range: 0-' + str(pos1Amount))
            time.sleep(0.5)
            print(pos2,'bets $' + str(pos2Amount),'(' + str(pos2Percent) + '%)','Range:',str(pos1Amount) + '-' + str(pos1Amount + pos2Amount))
            time.sleep(0.5)
            print(pos3,'bets $' + str(pos3Amount),'(' + str(pos3Percent) + '%)','Range:',str(pos2Amount + pos1Amount) + '-' + str(pos1Amount + pos2Amount + pos3Amount))
            time.sleep(0.5)
            print(pos4,'bets $' + str(pos4Amount),'(' + str(pos4Percent) + '%)','Range:',str(pos3Amount + pos2Amount + pos1Amount) + '-' + str(pos1Amount + pos2Amount + pos3Amount + pos4Amount))
            time.sleep(0.5)
            print()
            time.sleep(0.5)
            print('Total Jackpot: $' + str(total))
            time.sleep(0.5)
            print()

        print('Generating number...')      
        time.sleep(0.5)
        print()
        num = random.randint(1,total)
        print(num,'is drawn!')
        time.sleep(0.5)
        print()
        
        if bots == 2:
            if num < pos1Amount:
                print(pos1,'wins!')
                if pos1 == userName:
                    result = 'won: $'
                    amount = (total - pos1Amount)
                    balance = balance + total - pos1Amount 
                if pos1 != userName:
                    result = 'lost: $'
                    amount = userAmount
                    balance = balance - userAmount 
            elif num > pos1Amount:
                if num < (pos2Amount + pos1Amount):
                    print(pos2,'wins!')
                    if pos2 == userName:
                        result = 'won: $'
                        amount = (total - pos2Amount)
                        balance = balance + total - pos2Amount  
                    if pos2 != userName:
                        result = 'lost: $'
                        amount = userAmount
                        balance = balance - userAmount                     
                elif num < (pos3Amount + pos2Amount + pos1Amount):
                    print(pos3,'wins!')
                    if pos3 == userName:
                        result = 'won: $'
                        amount = (total - pos3Amount)
                        balance = balance + total - pos3Amount  
                    if pos3 != userName:
                        result = 'lost: $'
                        amount = userAmount
                        balance = balance - userAmount                         
                
        if bots == 3:
            if num < pos1Amount:
                print(pos1,'wins!')
                if pos1 == userName:
                    result = 'won: $'
                    amount = (total - pos1Amount)
                    balance = balance + total - pos1Amount    
                if pos1 != userName:
                    result = 'lost: $'
                    amount = userAmount
                    balance = balance - userAmount
            elif num > pos1Amount:
                if num < (pos2Amount + pos1Amount):
                    print(pos2,'wins!')
                    if pos2 == userName:
                        result = 'won: $'
                        amount = (total - pos2Amount)
                        balance = balance + total - pos2Amount  
                    if pos2 != userName:
                        result = 'lost: $'
                        amount = userAmount
                        balance = balance - userAmount                        
                elif num < (pos3Amount + pos2Amount + pos1Amount):
                    print(pos3,'wins!')
                    if pos3 == userName:
                        result = 'won: $'
                        amount = (total - pos3Amount)
                        balance = balance + total - pos3Amount   
                    if pos3 != userName:
                        result = 'lost: $'
                        amount = userAmount
                        balance = balance - userAmount                        
                elif num < (pos4Amount + pos3Amount + pos2Amount + pos1Amount):
                    print(pos4,'wins!')
                    if pos4 == userName:
                        result = 'won: $'
                        amount = (total - pos4Amount)
                        balance = balance + total - pos4Amount    
                    if pos4 != userName:
                        result = 'lost: $'
                        amount = userAmount
                        balance = balance - userAmount                          
                            
        print()
        print('You',result + str(amount))
        time.sleep(0.5)
        print('Balance: $' + str(balance))
        time.sleep(0.5)
        print()     
            
    if userAmount <= balance and userAmount >= 50 and (potTier == 'Medium' or potTier == 'medium'):
        bots = random.randint(2,3)
        if bots == 2:
            bot1Amount = random.randint(500,2000)
            bot2Amount = random.randint(500,2000)
            total = userAmount + bot1Amount + bot2Amount    
            userPercent = (userAmount / total) * 100
            bot1Percent = (bot1Amount / total) * 100
            bot2Percent = (bot2Amount / total) * 100
            userPercent = round(userPercent,1)
            bot1Percent = round(bot1Percent,1)
            bot2Percent = round(bot2Percent,1)
            userpos = random.randint(1,3)
            bot1pos = random.randint(1,3)
            bot2pos = random.randint(1,3)
            while userpos == bot1pos or userpos == bot2pos or bot1pos == userpos or bot1pos == bot2pos or bot2pos == userpos or bot2pos == bot1pos:
                userpos = random.randint(1,3)
                bot1pos = random.randint(1,3)
                bot2pos = random.randint(1,3)        
            if userpos == 1:
                pos1 = userName
                pos1Percent = userPercent
                pos1Amount = userAmount
            if userpos == 2:
                pos2 = userName
                pos2Percent = userPercent
                pos2Amount = userAmount
            if userpos == 3:
                pos3 = userName
                pos3Percent = userPercent
                pos3Amount = userAmount
            if bot1pos == 1:
                pos1 = bot1
                pos1Percent = bot1Percent
                pos1Amount = bot1Amount
            if bot1pos == 2:
                pos2 = bot1
                pos2Percent = bot1Percent
                pos2Amount = bot1Amount
            if bot1pos == 3:
                pos3 = bot1
                pos3Percent = bot1Percent
                pos3Amount = bot1Amount   
            if bot2pos == 1:
                pos1 = bot2
                pos1Percent = bot2Percent
                pos1Amount = bot2Amount
            if bot2pos == 2:
                pos2 = bot2
                pos2Percent = bot2Percent
                pos2Amount = bot2Amount
            if bot2pos == 3:
                pos3 = bot2
                pos3Percent = bot2Percent
                pos3Amount = bot2Amount  
            print(pos1,'bets $' + str(pos1Amount),'(' + str(pos1Percent) + '%)','Range: 0-' + str(pos1Amount))
            time.sleep(0.5)
            print(pos2,'bets $' + str(pos2Amount),'(' + str(pos2Percent) + '%)','Range:',str(pos1Amount) + '-' + str(pos1Amount + pos2Amount))
            time.sleep(0.5)
            print(pos3,'bets $' + str(pos3Amount),'(' + str(pos3Percent) + '%)','Range:',str(pos2Amount + pos1Amount) + '-' + str(pos1Amount + pos2Amount + pos3Amount))
            time.sleep(0.5)
            print()
            time.sleep(0.5)
            print('Total Jackpot: $' + str(total))
            time.sleep(0.5)
            print()
            
        if bots == 3:
            bot1Amount = random.randint(500,2000)
            bot2Amount = random.randint(500,2000)
            bot3Amount = random.randint(500,2000)
            total = userAmount + bot1Amount + bot2Amount + bot3Amount
            userPercent = (userAmount / total) * 100
            bot1Percent = (bot1Amount / total) * 100
            bot2Percent = (bot2Amount / total) * 100
            bot3Percent = (bot3Amount / total) * 100
            userPercent = round(userPercent,1)
            bot1Percent = round(bot1Percent,1)
            bot2Percent = round(bot2Percent,1)       
            bot3Percent = round(bot3Percent,1) 
            userpos = random.randint(1,4)
            bot1pos = random.randint(1,4)
            bot2pos = random.randint(1,4)
            bot3pos = random.randint(1,4)
            while userpos == bot1pos or userpos == bot2pos or userpos == bot3pos or bot1pos == userpos or bot1pos == bot2pos or bot1pos == bot3pos or bot2pos == userpos or bot2pos == bot1pos or bot2pos == bot3pos or bot3pos == userpos or bot3pos == bot1pos or bot3pos == bot2pos:
                userpos = random.randint(1,4)
                bot1pos = random.randint(1,4)
                bot2pos = random.randint(1,4)
                bot3pos = random.randint(1,4)                
            if userpos == 1:
                pos1 = userName
                pos1Percent = userPercent
                pos1Amount = userAmount
            if userpos == 2:
                pos2 = userName
                pos2Percent = userPercent
                pos2Amount = userAmount
            if userpos == 3:
                pos3 = userName
                pos3Percent = userPercent
                pos3Amount = userAmount
            if userpos == 4:
                pos4 = userName
                pos4Percent = userPercent
                pos4Amount = userAmount
            if bot1pos == 1:
                pos1 = bot1
                pos1Percent = bot1Percent
                pos1Amount = bot1Amount
            if bot1pos == 2:
                pos2 = bot1
                pos2Percent = bot1Percent
                pos2Amount = bot1Amount
            if bot1pos == 3:
                pos3 = bot1
                pos3Percent = bot1Percent
                pos3Amount = bot1Amount   
            if bot1pos == 4:
                pos4 = bot1
                pos4Percent = bot1Percent
                pos4Amount = bot1Amount 
            if bot2pos == 1:
                pos1 = bot2
                pos1Percent = bot2Percent
                pos1Amount = bot2Amount
            if bot2pos == 2:
                pos2 = bot2
                pos2Percent = bot2Percent
                pos2Amount = bot2Amount
            if bot2pos == 3:
                pos3 = bot2
                pos3Percent = bot2Percent
                pos3Amount = bot2Amount   
            if bot2pos == 4:
                pos4 = bot2
                pos4Percent = bot2Percent
                pos4Amount = bot2Amount 
            if bot3pos == 1:
                pos1 = bot3
                pos1Percent = bot3Percent
                pos1Amount = bot3Amount
            if bot3pos == 2:
                pos2 = bot3
                pos2Percent = bot3Percent
                pos2Amount = bot3Amount
            if bot3pos == 3:
                pos3 = bot3
                pos3Percent = bot3Percent
                pos3Amount = bot3Amount
            if bot3pos == 4:
                pos4 = bot3
                pos4Percent = bot3Percent
                pos4Amount = bot3Amount 
            print(pos1,'bets $' + str(pos1Amount),'(' + str(pos1Percent) + '%)','Range: 0-' + str(pos1Amount))
            time.sleep(0.5)
            print(pos2,'bets $' + str(pos2Amount),'(' + str(pos2Percent) + '%)','Range:',str(pos1Amount) + '-' + str(pos1Amount + pos2Amount))
            time.sleep(0.5)
            print(pos3,'bets $' + str(pos3Amount),'(' + str(pos3Percent) + '%)','Range:',str(pos2Amount + pos1Amount) + '-' + str(pos1Amount + pos2Amount + pos3Amount))
            time.sleep(0.5)
            print(pos4,'bets $' + str(pos4Amount),'(' + str(pos4Percent) + '%)','Range:',str(pos3Amount + pos2Amount + pos1Amount) + '-' + str(pos1Amount + pos2Amount + pos3Amount + pos4Amount))
            time.sleep(0.5)
            print()
            time.sleep(0.5)
            print('Total Jackpot: $' + str(total))
            time.sleep(0.5)
            print()

        print('Generating number...')    
        time.sleep(0.5)
        print()
        num = random.randint(1,total)
        print(num,'is drawn!')
        time.sleep(0.5)
        print()
            
        if bots == 2:
            if num < pos1Amount:
                print(pos1,'wins!')
                if pos1 == userName:
                    result = 'won: $'
                    amount = (total - pos1Amount)
                    balance = balance + total - pos1Amount 
                if pos1 != userName:
                    result = 'lost: $'
                    amount = userAmount
                    balance = balance - userAmount 
            elif num > pos1Amount:
                if num < (pos2Amount + pos1Amount):
                    print(pos2,'wins!')
                    if pos2 == userName:
                        result = 'won: $'
                        amount = (total - pos2Amount)
                        balance = balance + total - pos2Amount  
                    if pos2 != userName:
                        result = 'lost: $'
                        amount = userAmount
                        balance = balance - userAmount                     
                elif num < (pos3Amount + pos2Amount + pos1Amount):
                    print(pos3,'wins!')
                    if pos3 == userName:
                        result = 'won: $'
                        amount = (total - pos3Amount)
                        balance = balance + total - pos3Amount  
                    if pos3 != userName:
                        result = 'lost: $'
                        amount = userAmount
                        balance = balance - userAmount                         
                
        if bots == 3:
            if num < pos1Amount:
                print(pos1,'wins!')
                if pos1 == userName:
                    result = 'won: $'
                    amount = (total - pos1Amount)
                    balance = balance + total - pos1Amount    
                if pos1 != userName:
                    result = 'lost: $'
                    amount = userAmount
                    balance = balance - userAmount
            elif num > pos1Amount:
                if num < (pos2Amount + pos1Amount):
                    print(pos2,'wins!')
                    if pos2 == userName:
                        result = 'won: $'
                        amount = (total - pos2Amount)
                        balance = balance + total - pos2Amount  
                    if pos2 != userName:
                        result = 'lost: $'
                        amount = userAmount
                        balance = balance - userAmount                        
                elif num < (pos3Amount + pos2Amount + pos1Amount):
                    print(pos3,'wins!')
                    if pos3 == userName:
                        result = 'won: $'
                        amount = (total - pos3Amount)
                        balance = balance + total - pos3Amount   
                    if pos3 != userName:
                        result = 'lost: $'
                        amount = userAmount
                        balance = balance - userAmount                        
                elif num < (pos4Amount + pos3Amount + pos2Amount + pos1Amount):
                    print(pos4,'wins!')
                    if pos4 == userName:
                        result = 'won: $'
                        amount = (total - pos4Amount)
                        balance = balance + total - pos4Amount    
                    if pos4 != userName:
                        result = 'lost: $'
                        amount = userAmount
                        balance = balance - userAmount                          
                            
        print()
        print('You',result + str(amount))
        time.sleep(0.5)
        print('Balance: $' + str(balance))
        time.sleep(0.5)
        print()
        
    if userAmount <= balance and userAmount >= 50 and (potTier == 'High' or potTier == 'high'):
        bots = random.randint(2,3)
        if bots == 2:
            bot1Amount = random.randint(2000,10000)
            bot2Amount = random.randint(2000,10000)
            total = userAmount + bot1Amount + bot2Amount    
            userPercent = (userAmount / total) * 100
            bot1Percent = (bot1Amount / total) * 100
            bot2Percent = (bot2Amount / total) * 100
            userPercent = round(userPercent,1)
            bot1Percent = round(bot1Percent,1)
            bot2Percent = round(bot2Percent,1)
            userpos = random.randint(1,3)
            bot1pos = random.randint(1,3)
            bot2pos = random.randint(1,3)
            while userpos == bot1pos or userpos == bot2pos or bot1pos == userpos or bot1pos == bot2pos or bot2pos == userpos or bot2pos == bot1pos:
                userpos = random.randint(1,4)
                bot1pos = random.randint(1,4)
                bot2pos = random.randint(1,4)        
            if userpos == 1:
                pos1 = userName
                pos1Percent = userPercent
                pos1Amount = userAmount
            if userpos == 2:
                pos2 = userName
                pos2Percent = userPercent
                pos2Amount = userAmount
            if userpos == 3:
                pos3 = userName
                pos3Percent = userPercent
                pos3Amount = userAmount
            if bot1pos == 1:
                pos1 = bot1
                pos1Percent = bot1Percent
                pos1Amount = bot1Amount
            if bot1pos == 2:
                pos2 = bot1
                pos2Percent = bot1Percent
                pos2Amount = bot1Amount
            if bot1pos == 3:
                pos3 = bot1
                pos3Percent = bot1Percent
                pos3Amount = bot1Amount   
            if bot2pos == 1:
                pos1 = bot2
                pos1Percent = bot2Percent
                pos1Amount = bot2Amount
            if bot2pos == 2:
                pos2 = bot2
                pos2Percent = bot2Percent
                pos2Amount = bot2Amount
            if bot2pos == 3:
                pos3 = bot2
                pos3Percent = bot2Percent
                pos3Amount = bot2Amount  
            print(pos1,'bets $' + str(pos1Amount),'(' + str(pos1Percent) + '%)','Range: 0-' + str(pos1Amount))
            time.sleep(0.5)
            print(pos2,'bets $' + str(pos2Amount),'(' + str(pos2Percent) + '%)','Range:',str(pos1Amount) + '-' + str(pos1Amount + pos2Amount))
            time.sleep(0.5)
            print(pos3,'bets $' + str(pos3Amount),'(' + str(pos3Percent) + '%)','Range:',str(pos2Amount + pos1Amount) + '-' + str(pos1Amount + pos2Amount + pos3Amount))
            time.sleep(0.5)
            print()
            time.sleep(0.5)
            print('Total Jackpot: $' + str(total))
            time.sleep(0.5)
            print()
            
        if bots == 3:
            bot1Amount = random.randint(2000,10000)
            bot2Amount = random.randint(2000,10000)
            bot3Amount = random.randint(2000,10000)
            total = userAmount + bot1Amount + bot2Amount + bot3Amount
            userPercent = (userAmount / total) * 100
            bot1Percent = (bot1Amount / total) * 100
            bot2Percent = (bot2Amount / total) * 100
            bot3Percent = (bot3Amount / total) * 100
            userPercent = round(userPercent,1)
            bot1Percent = round(bot1Percent,1)
            bot2Percent = round(bot2Percent,1)       
            bot3Percent = round(bot3Percent,1) 
            userpos = random.randint(1,4)
            bot1pos = random.randint(1,4)
            bot2pos = random.randint(1,4)
            bot3pos = random.randint(1,4)
            while userpos == bot1pos or userpos == bot2pos or userpos == bot3pos or bot1pos == userpos or bot1pos == bot2pos or bot1pos == bot3pos or bot2pos == userpos or bot2pos == bot1pos or bot2pos == bot3pos or bot3pos == userpos or bot3pos == bot1pos or bot3pos == bot2pos:
                userpos = random.randint(1,4)
                bot1pos = random.randint(1,4)
                bot2pos = random.randint(1,4)
                bot3pos = random.randint(1,4)                
            if userpos == 1:
                pos1 = userName
                pos1Percent = userPercent
                pos1Amount = userAmount
            if userpos == 2:
                pos2 = userName
                pos2Percent = userPercent
                pos2Amount = userAmount
            if userpos == 3:
                pos3 = userName
                pos3Percent = userPercent
                pos3Amount = userAmount
            if userpos == 4:
                pos4 = userName
                pos4Percent = userPercent
                pos4Amount = userAmount
            if bot1pos == 1:
                pos1 = bot1
                pos1Percent = bot1Percent
                pos1Amount = bot1Amount
            if bot1pos == 2:
                pos2 = bot1
                pos2Percent = bot1Percent
                pos2Amount = bot1Amount
            if bot1pos == 3:
                pos3 = bot1
                pos3Percent = bot1Percent
                pos3Amount = bot1Amount   
            if bot1pos == 4:
                pos4 = bot1
                pos4Percent = bot1Percent
                pos4Amount = bot1Amount 
            if bot2pos == 1:
                pos1 = bot2
                pos1Percent = bot2Percent
                pos1Amount = bot2Amount
            if bot2pos == 2:
                pos2 = bot2
                pos2Percent = bot2Percent
                pos2Amount = bot2Amount
            if bot2pos == 3:
                pos3 = bot2
                pos3Percent = bot2Percent
                pos3Amount = bot2Amount   
            if bot2pos == 4:
                pos4 = bot2
                pos4Percent = bot2Percent
                pos4Amount = bot2Amount 
            if bot3pos == 1:
                pos1 = bot3
                pos1Percent = bot3Percent
                pos1Amount = bot3Amount
            if bot3pos == 2:
                pos2 = bot3
                pos2Percent = bot3Percent
                pos2Amount = bot3Amount
            if bot3pos == 3:
                pos3 = bot3
                pos3Percent = bot3Percent
                pos3Amount = bot3Amount
            if bot3pos == 4:
                pos4 = bot3
                pos4Percent = bot3Percent
                pos4Amount = bot3Amount 
            print(pos1,'bets $' + str(pos1Amount),'(' + str(pos1Percent) + '%)','Range: 0-' + str(pos1Amount))
            time.sleep(0.5)
            print(pos2,'bets $' + str(pos2Amount),'(' + str(pos2Percent) + '%)','Range:',str(pos1Amount) + '-' + str(pos1Amount + pos2Amount))
            time.sleep(0.5)
            print(pos3,'bets $' + str(pos3Amount),'(' + str(pos3Percent) + '%)','Range:',str(pos2Amount + pos1Amount) + '-' + str(pos1Amount + pos2Amount + pos3Amount))
            time.sleep(0.5)
            print(pos4,'bets $' + str(pos4Amount),'(' + str(pos4Percent) + '%)','Range:',str(pos3Amount + pos2Amount + pos1Amount) + '-' + str(pos1Amount + pos2Amount + pos3Amount + pos4Amount))
            time.sleep(0.5)
            print()
            time.sleep(0.5)
            print('Total Jackpot: $' + str(total))
            time.sleep(0.5)
            print()
            
        print('Generating number...')    
        time.sleep(0.5)
        print()
        num = random.randint(1,total)
        print(num,'is drawn!')
        time.sleep(0.5)
        print()
            
        if bots == 2:
            if num < pos1Amount:
                print(pos1,'wins!')
                if pos1 == userName:
                    result = 'won: $'
                    amount = (total - pos1Amount)
                    balance = balance + total - pos1Amount 
                if pos1 != userName:
                    result = 'lost: $'
                    amount = userAmount
                    balance = balance - userAmount 
            elif num > pos1Amount:
                if num < (pos2Amount + pos1Amount):
                    print(pos2,'wins!')
                    if pos2 == userName:
                        result = 'won: $'
                        amount = (total - pos2Amount)
                        balance = balance + total - pos2Amount  
                    if pos2 != userName:
                        result = 'lost: $'
                        amount = userAmount
                        balance = balance - userAmount                     
                elif num < (pos3Amount + pos2Amount + pos1Amount):
                    print(pos3,'wins!')
                    if pos3 == userName:
                        result = 'won: $'
                        amount = (total - pos3Amount)
                        balance = balance + total - pos3Amount  
                    if pos3 != userName:
                        result = 'lost: $'
                        amount = userAmount
                        balance = balance - userAmount                         
                
        if bots == 3:
            if num < pos1Amount:
                print(pos1,'wins!')
                if pos1 == userName:
                    result = 'won: $'
                    amount = (total - pos1Amount)
                    balance = balance + total - pos1Amount    
                if pos1 != userName:
                    result = 'lost: $'
                    amount = userAmount
                    balance = balance - userAmount
            elif num > pos1Amount:
                if num < (pos2Amount + pos1Amount):
                    print(pos2,'wins!')
                    if pos2 == userName:
                        result = 'won: $'
                        amount = (total - pos2Amount)
                        balance = balance + total - pos2Amount  
                    if pos2 != userName:
                        result = 'lost: $'
                        amount = userAmount
                        balance = balance - userAmount                        
                elif num < (pos3Amount + pos2Amount + pos1Amount):
                    print(pos3,'wins!')
                    if pos3 == userName:
                        result = 'won: $'
                        amount = (total - pos3Amount)
                        balance = balance + total - pos3Amount   
                    if pos3 != userName:
                        result = 'lost: $'
                        amount = userAmount
                        balance = balance - userAmount                        
                elif num < (pos4Amount + pos3Amount + pos2Amount + pos1Amount):
                    print(pos4,'wins!')
                    if pos4 == userName:
                        result = 'won: $'
                        amount = (total - pos4Amount)
                        balance = balance + total - pos4Amount    
                    if pos4 != userName:
                        result = 'lost: $'
                        amount = userAmount
                        balance = balance - userAmount                          
                            
        print()
        print('You',result + str(amount))
        time.sleep(0.5)
        print('Balance: $' + str(balance))
        time.sleep(0.5)
        print()     
        
    if balance != 0:        
        print('Would you like to play again? (y/n)')
        playAgain = input('> ')
        print('\n' * 66)
                                
        if playAgain == 'n':
            print ('Exiting Program') 
                
    if balance == 0:
        print('Would you like to start over? (y/n)')
        balance += 1000
        playAgain = input('> ')
        print('\n' * 66)
        
        if playAgain == 'n':
            time.sleep(0.5)
            print('Exiting Program')