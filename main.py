### ERNESTS RALFS KALNIŅŠ
player1 = 1
player2 = 1
blue_ladders = [18, 67, 74, 90] # nosaka kuros skaitļos ir zilas trepes
red_ladders = [15, 24, 33, 87] #  nosaka kuros skaitļos ir sarkanas trepes
import random
while player2 < 100: # spele beigsies kad otrais player ir virs 100, man pirmais player neiet :()
        dicenumbers = random.randint(1, 6) # dators izvelas nejausu skaitli no 1 lidz 6
        player1 = input("Type Roll to roll the dice")
        if player1 == 1:
            print("You rolled a 1")
            player1= player1+dicenumbers
            print("\n Player1 is currently at: ", player1)
            pass
        elif player1 == 2:
            print("You rolled a 2")
            player1= player1+dicenumbers
            print("\n Player1 is currently at: ", player1)
            pass
        elif player1 == 3:
            print("You rolled a 3")
            player1= player1+dicenumbers
            print("\n Player1 is currently at: ", player1)
            pass
        elif player1 == 4:
            print("You rolled a 4")
            player1= player1+dicenumbers
            print("\n Player1 is currently at: ", player1)
            pass
        elif player1 == 5:
            print("You rolled a 5")
            player1= player1+dicenumbers
            print("\n Player1 is currently at: ", player1)
            pass
        elif player1 == 6:
            print("You rolled a 6")
            player1= player1+dicenumbers
            print("\n Player1 is currently at: ", player1)
            pass
        if player1 == 18:
            print("/n You've landed on a blue ladder! Moving back down to spot 7.")
            player1 -= 11
            print("\n Player1 is currently at: ", player1)
        elif player1 == 67:
            print("/n You've landed on a blue ladder! Moving back down to spot 46.")
            player1 -= 21
            print("\n Player1 is currently at: ", player1)
        elif player1 == 80:
            print("/n You've landed on a blue ladder! Moving back down to spot 69")
            player1 -= 11
            print("\n Player1 is currently at: ", player1)
        elif player1 == 74:
            print("/n You've landed on a blue ladder! Moving back down to spot 63")
            player1 -= 11
            print("\n Player1 is currently at: ", player1)
        elif player1 == 15:
            print("/n You've landed on a red ladder! Moving up to spot 24.")
            player1 += 9
            print("\n Player1 is currently at: ", player1)
        elif player1 == 39:
            print("/n You've landed on a red ladder! Moving up to spot 48.")
            player1 += 9
            print("\n Player1 is currently at: ", player1)
        elif player1 == 33:
            print("/n You've landed on a red ladder! Moving up to spot 52")
            player1 += 19
            print("\n Player1 is currently at: ", player1)
        elif player1 == 87:
            print("/n You've landed on a red ladder! Moving up to spot 96")
            player1 += 9
            print("\n Player1 is currently at: ", player1)
        dicenumberss = random.randint(1, 6)
        if dicenumberss == 1:
            print("You rolled a 1")
            player2= player2+dicenumberss
            print("\n Player2 is currently at: ", player2)
            pass
        elif dicenumberss == 2:
            print("You rolled a 2")
            player2= player2+dicenumberss
            print("\n Player2 is currently at: ", player2)
            pass
        elif dicenumberss == 3:
            print("You rolled a 3")
            player2= player2+dicenumberss
            print("\n Player2 is currently at: ", player2)
            pass
        elif dicenumberss == 4:
            print("You rolled a 4")
            player2= player2+dicenumberss
            print("\n Player2 is currently at: ", player2)
            pass
        elif dicenumberss == 5:
            print("You rolled a 5")
            player2= player2+dicenumberss
            print("\n Player2 is currently at: ", player2)
            pass
        elif dicenumberss == 6:
            print("You rolled a 6")
            player2= player2+dicenumberss
            print("\n Player2 is currently at: ", player2)
            pass
        if player2 == 18:
            print("/n You've landed on a blue ladder! Moving back down to spot 7.")
            player2 -= 11
            print("\n Player2 is currently at: ", player2)
        elif player2 == 67:
            print("/n You've landed on a blue ladder! Moving back down to spot 46.")
            player2 -= 21
            print("\n Player2 is currently at: ", player2)
        elif player2 == 80:
            print("/n You've landed on a blue ladder! Moving back down to spot 69")
            player2 -= 11
            print("\n Player2 is currently at: ", player2)
        elif player2 == 74:
            print("/n You've landed on a blue ladder! Moving back down to spot 63")
            player2 -= 11
            print("\n Player2 is currently at: ", player2)
        elif player2 == 15:
            player2 += 9
            print("/n You've landed on a red ladder! Moving up to spot 24.")
            player2 += 9
            print("\n Player2 is currently at: ", player2)
        elif player2 == 39:
            print("/n You've landed on a red ladder! Moving up to spot 48.")
            player2 += 9
            print("\n Player2 is currently at: ", player2)
        elif player2 == 33:
            print("/n You've landed on a red ladder! Moving up to spot 52")
            player2 += 19
            print("\n Player2 is currently at: ", player2)
        elif player2 == 87:
            print("/n You've landed on a red ladder! Moving up to spot 96")
            player2 += 9
            print("\n Player2 is currently at: ", player2)
            
