import random
import time

print('CHOOSE YOUR OWN ADVENTURE!')

user_name = input('Please enter your name: ')
user_health = 100

while (user_health > 0):
    print(f'Long ago in a distant land, there lived a brave adventurer named {user_name}. One day, {user_name} decided to embark on a quest to find a hidden treasure.')
    print(f'As {user_name} journeyed through the dense forest, they encountered a fork in the road.')
    
    choice_1 = input('Which way would you like to go? (left/right): ').lower()

    if choice_1 == 'left':
        print(f'{user_name} took the left path and soon found themselves face to face with a wild goblin!')
        action = input('Do you want to fight the goblin or run away?: (fight/run)').lower()
        
        if action == 'fight':
            goblin_health = 50
            while ((goblin_health > 0) and (user_health > 0)):
                fight = input('What would you like to do?: (attack/item/heal)').lower()
                if (fight == 'attack'):
                    user_damage = random.randint(10, 30)
                    goblin_health -= user_damage
                    if (goblin_health <= 0):
                        print(f'You attacked the goblin and dealt {user_damage} damage! Goblin health is now 0.')
                        time.sleep(1.7)
                        print('The goblin has been defeated! You found a treasure chest filled with gold coins!')
                        break
                    else:
                        print(f'You attacked the goblin and dealt {user_damage} damage! Goblin health is now {goblin_health}.')
                        time.sleep(1.7)
                        print('The goblin is preparing to attack...')
                        time.sleep(1.7)
                        goblin_damage = random.randint(15, 25)
                        user_health -= goblin_damage
                        print(f'The goblin attacked you and dealt {goblin_damage} damage! Your health is now {user_health}.')
                elif (fight == 'item'):
                    print('You have nothing in your inventory!')
                    print('The goblin laughs.')
                elif (fight == 'heal'):
                    print('You have nothing in your inventory!')
                    print('The goblin is preparing to attack...')
                    time.sleep(1.7)
                    goblin_damage = random.randint(15, 25)
                    user_health -= goblin_damage
                    print(f'The goblin attacked you and dealt {goblin_damage} damage! Your health is now {user_health}.')
            
            if (user_health <= 0):
                break
        
        elif action == 'run':
            run_chance = random.randint(1, 2)
            if run_chance == 1:
                print(f'{user_name} successfully ran away from the goblin and escaped back to the fork in the road.')
            else:
                goblin_damage = random.randint(15, 25)
                user_health -= goblin_damage
                print(f'{user_name} failed to escape! The goblin pounced and stabbed you while you tried to get away! You lose.')
                break
                    
    if choice_1 == 'right':
        print(f'{user_name} took the right path and found a peaceful clearing filled with beautiful flowers. They decided to rest here for a while, enjoying the tranquility of nature.')
        time.sleep(2)
        print(f'{user_name} is allergic to flowers!!')
        time.sleep(2)
        user_health -= 100
        print(f'{user_name} died! Game over.')
        
