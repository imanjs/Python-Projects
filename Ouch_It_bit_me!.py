import random
import math

# Define the number of zombies
zombies = 5
# Define the player's initial lives
lives = 3
# Deine the player's initial score
score = 0


while lives > 0:
    zombie = random.randint(1, zombies)
    print(f'Zombie {zombie} has appeared!')

# Prompt user to shoot the zombie.
    shoot = input('Do you want to shoot the zombie? (y/n)')
    if shoot == 'y':
        hit = random.randint(1,2)
        if hit == 1:
            # User misses the shot.
            print('You missed! The zombie bit you.')
            lives -= 1
            print(f'You have {lives} lives left.')

        else: 
            # User succesfully kills the zombie.
            print('You killed the zombie!')
            score += 1
            print(f'Your score is now {score}.')
        if score == 5:
            print('SURVIVOR ENDING: You survived the night, GAME WON!')
        if lives == 0:
            print('FIGHTER ENDING: You died, GAME OVER!')
    else:
        # User does not want to shoot the zombie. Prompt user to block.
        block = input('You did not shoot the zombie. It is about to attack you.\nDo you want to block the zombie\'s attack? (y/n)')
        if block == 'y':
            # Randomly assign user's outcome.
            hit = random.randint(1,3)
            if hit == 1:
                # User block's the attack to late and loses one life.
                print('You blocked the attack too late. The zombie attacked you.')
                lives -= 1
                print(f'You have {lives} lives left.')
            if hit == 2:
                # User succesfully blocks the attack, however, does not kill the zombie.
                print('You blocked the attack perfectly. However, did not kill it.\n The zombie is still alive.')
                print(f'There are {zombies} zombies left.')
            if hit == 3:
                # User succesfully blocks the attack. Kills the zombie in the process.
                print('You blocked the attack perfectly. You killed it in the process.')
                zombies -= 1
                score += 1
                print(f'There are {zombies} zombies left.')
                print(f'Your score is now {score}.')
        if block == 'n':
            # User chooses not to block the attack at all. Results in user immediately dying.
            print('You did not block the zombie\'s attack.')
            lives -= lives
            print('STUPID ENDING: The zombie ate you alive. GAME OVER!')
        else:
            # Hidden Route
            block = input('Last chance...\nDo you want to block the zombie\'s attack... (y/n)')
            if block == '':
                stupid = input('Are you stupid (y/n)...')
                if stupid == 'y': 
                    print('Yeah you really are. Trying to be a smart ass but that won\'t work on me.')
                    print('I know people like you, thinking they are so fucking special. Always trying to \'MaKE tEeIr oWn PaTH\' like a dumbass.')    
                    print('WELL IT DOES\'NT FUCKING WORK LIKE THAT HERE.')
                    print('That\'s okay... I\'ll just kill you myself.')
                    print('JACKASS ENDING: Ģ̶̡̭̞͇̯̯͉̫̀̀̃̅̅̄͒̂̀̈́́̈́͝A̴̗͓̫̗͔͙̪͓͛̓̾̐̍̒̉̓̉͊̀̑͠M̶̻̬͗̈́͊̀̌̑̋͛̇̚ͅE̶̞̖̮͖̟͉͎̼̿̓̑́̄̈ ̴̧̻̬̣̉͑̉̓̋O̵̱͌͜V̶̳̥̥̓̇͠Ȅ̷͓̙̳̖̥̬̩͙͇̣́̔̃̒͌̄͘̚̕͜ͅR̴̢͕͉̤͇͊̎̉̔̏̎̀̄͊̕̚͝')
                    break
                else:
                    print('Are you sure? You seem pretty stupid to me.')
                    print('You know what, you might be a annoying little fuck but at least you have confidence.')
                    print('Too bad...')
                    print('POOR THING ENDING: GAME OVER?')
                    break
            if block == 'y':
            # Randomly assign user's outcome.
                hit = random.randint(1,3)
                if hit == 1:
                    # User block's the attack to late and loses one life.
                    print('You blocked the attack too late. The zombie attacked you.')
                    lives -= 1
                    print(f'You have {lives} lives left.')
                if hit == 2:
                    # User succesfully blocks the attack, however, does not kill the zombie.
                    print('You blocked the attack perfectly. However, did not kill it.\n The zombie is still alive.')
                    print(f'There are {zombies} zombies left.')
                if hit == 3:
                    # User succesfully blocks the attack. Kills the zombie in the process.
                    print('You blocked the attack perfectly. You killed it in the process.')
                    zombies -= 1
                    score += 1
                    print(f'There are {zombies} zombies left.')
                    print(f'Your score is now {score}.')
            if block == 'n':
            # User chooses not to block the attack at all. Results in user immediately dying.
                print('You did not block the zombie\'s attack.')
                lives -= lives
                print('STUPID ENDING: The zombie ate you alive. GAME OVER!')

            
            
            
            


