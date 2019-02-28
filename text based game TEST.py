#Made by Daddy (Matthew Jackson)
#23/02/2019

"""This is a text based adventure game for Annabelle.
The main character is Princess Unikitty from the Lego Movie"""

"""at the moment, gold lego does disppear from the location after collecting,
so you can visit the same place as many times as "count" allows t owin the game"""

import datetime
import time

class User:
    pass
        
class Location():
    def __init__(self, name, description, goldLego):
        self.name = name
        self.description = description
        self.goldLego = goldLego

bricksburgh = Location('Bricksburgh.', ' A beautiful Lego city.', 'No gold Lego blocks here')
emmetsHouse = Location('Emmets House', ' a boring house.', 'YOU FOUND A GOLD LEGO BLOCK!!')
cloudCuckooLand = Location('Cloud Cuckoo Land. ', 'This is Princess Unikitty\'s home. ', 'YOU FOUND A GOLD LEGO BLOCK!!' )
businessTower = Location('Lord Business\' Tower.' , ' A very scary place. ', 'YOU FOUND A GOLD LEGO BLOCK!!')

#print(bricksburgh.name, bricksburgh.description, bricksburgh.goldLego)
#print(emmetsHouse.name, emmetsHouse.description, emmetsHouse.goldLego)
#print(cloudCuckooLand.name, cloudCuckooLand.description, cloudCuckooLand.goldLego)
#print(businessTower.name, businessTower.description, businessTower.goldLego)

def newLinePause(seconds):
    time.sleep(seconds)
    print('\n')

def welcomePlayer():
    newLinePause(1)
    newLinePause(1)
    
    print('Hello, you cheeky little bumbum.')
    
    newLinePause(2)
    
    print('I am a computer program made by your Daddy.')
    
    newLinePause(0)
    
    player = User()
    player.name = input('Please tell me your name: ')
    player.favourite_colour = input('Please tell me your favourite colour: ')
    player.age = str(input('Please enter your age: '))
    player.name = player.name.upper()
    player.favourite_colour = player.favourite_colour.upper()
    
    
    newLinePause(2)
    
    print ('Nice to meet you ' + player.name + '!')
    newLinePause(2)
    print('So you like ' + player.favourite_colour + '? Awesome.')
    print('My favourite colour is blue... ' )
    newLinePause(2)
    print('no orange... ' )
    newLinePause(2)
    print('no blue... ')
    newLinePause(2)
    print('Well, it\'s either blue or orange')
    newLinePause(2)
    print('Anyway...')
    input('Would you like to meet my friend, Princess Unikitty? ')
    newLinePause(1)
    print('OK, I\'ll just give her a shout...')
    newLinePause(3)
    print('"HEY, PRINCESS UNIKITTY, GET OVER HERE AND MEET ' + player.name + '!"')
    newLinePause(1)
    print('...')
    newLinePause(1)
    print('...')
    newLinePause(1)
    print('...')
    newLinePause(1)
    print('...')
    newLinePause(2)
    print("""All right all right, stop shouting. You wouldn\'t want me to
get ANGRY would you???""")

    print('Oh, hello there ' + player.name + """. My name is Princess Unikitty!.
I see you love """ + player.favourite_colour + '! I love ' + 
player.favourite_colour + ' too.')
    newLinePause(2)
    print("""I'm sad because I have lost all my gold lego bricks.
DO you think you could help me find them?""")
    acceptMission = " "
    while acceptMission != 'yes' and acceptMission != 'no':
        acceptMission = input('Type "yes" to help, or "no" if you don\'t want to: ')
           
        if acceptMission == 'yes':
            newLinePause(1)
            print('THATS AWESOME!!')
        elif acceptMission == 'no':
            newLinePause(2)
            print('YOU STINKY BUMFACE! I\'M OFF TO FIND THEM ON MY OWN. BOO HOO HOO')
        else:
            newLinePause(2)
            print('What on earth does "' + acceptMission + '" mean you dumface?')
            newLinePause(2)
            
    newLinePause(2)
    print('Lets start looking for those gold lego blocks...')
            
            
def mainGame():
    
  
    count = 0
#    location1 = bricksburgh
#    location2 - emmetsHouse
#    location3 = cloudCuckooLand
#    location4 = businessTower
    
    while count < 3:    
        locationChoice = int(input("""To go to Bricksburgh type 1.
To go to Emmet\'s House type 2.
To go to Cloud Cuckoo Land type 3.
To go to Lord Business\' Tower type 4.
"""))
        if locationChoice == 1:
            newLinePause(1)
            print(bricksburgh.name, bricksburgh.description, bricksburgh.goldLego)
        
        elif locationChoice == 2:
            newLinePause(1)
            print(emmetsHouse.name, emmetsHouse.description, emmetsHouse.goldLego)
            newLinePause(2)
            count += 1
            print('You have found ' + str(count) + ' gold lego blocks. Well done')
        
        elif locationChoice == 3:
            newLinePause(1)
            print(cloudCuckooLand.name, cloudCuckooLand.description, cloudCuckooLand.goldLego)
            newLinePause(1)
            count += 1
            print('You have found ' + str(count) + ' gold lego blocks. Well done')
        
        elif locationChoice == 4:
            newLinePause(1)
            print(businessTower.name, businessTower.description, businessTower.goldLego)
            newLinePause(2)
            count += 1
            print('You have found ' + str(count) + ' gold lego blocks. Well done')
            
            
        
    newLinePause(2)
    print('YOU HAVE FOUND ALL MY GOLD LEGO BLOCKS!!!')
    newLinePause(2)
    print('THANKYOU')
    newLinePause(.5)
    print('THANKYOU')
    newLinePause(.5)
    print('THANKYOU')
    newLinePause(.5)
    print('THANKYOU')
    newLinePause(.5)
    print('THANKYOU')
    newLinePause(.5)
    print('THANKYOU')
    newLinePause(.5)
    print('THANKYOU')
    
    newLinePause(3)
    print('You are my best friend. Please come back soon!!')
               
            
            
            
def tryAgain():
    restart = input('If you would like to try again, type "yes". Otherwise, type anything else: ')         
    if restart == 'yes':
        print('LOADING........')
        newLinePause(1)
        print('LOADING........')
        newLinePause(1)
        print('LOADING........')
        newLinePause(1)
        print('LOADING........')
        newLinePause(1)
        welcomePlayer()
    else: 
        print('I hope you enjoyed the game. See you next time pickle! xxxxxx')
        
    
          
welcomePlayer()
mainGame()
tryAgain()


