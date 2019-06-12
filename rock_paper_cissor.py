u=1
c=1
turn = 10
game_on=True
user_choice = input('enter your choice: rock,paper or cissor : ')
import random
while turn > 0:
    
    comp_choice = random.randint(1,3)
    if comp_choice==1:
        comp_choice='rock'
    elif comp_choice==2:
        comp_choice='paper'
    elif comp_choice==3:
        comp_choice='cissor'

    if user_choice=='rock' and comp_choice=='cissor':
        print(f"you win \n computer choose {comp_choice}")
        
        u+=1
        turn-=1
        user_choice = input('enter again : ')
    elif user_choice=='paper' and comp_choice=='rock':
        print(f"you win \n computer choose {comp_choice}")
       
        u+=1
        turn-=1
        user_choice = input('enter again : ')
    elif user_choice=='cissor' and comp_choice=='paper':
        print(f"you win \n computer choose {comp_choice}")
        
        u+=1
        turn-=1
        user_choice = input('enter again : ')

    elif comp_choice=='rock' and user_choice=='cissor':
        print(f"computer win \n computer choose {comp_choice}")
        
        c+=1
        turn-=1
        user_choice = input('enter again : ')
    elif comp_choice=='paper' and user_choice=='rock':
        print(f"computer win \n computer choose {comp_choice}")
       
        c+=1
        turn-=1
        user_choice = input('enter again : ')
    elif comp_choice=='cissor' and user_choice=='paper':
        print(f"computer win \n computer choose {comp_choice}")
        
        c+=1
        turn-=1
        user_choice = input('enter again : ')

    elif comp_choice==user_choice:
        turn-=1
        user_choice = input(f'draw\ncomputer choose {comp_choice} \n enter again : ')


print(f'you win {u} times \ncomputer wins {c} times')