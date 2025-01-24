import random 

random_number = random.randint(1, 100)

game_count = 1

while True:
    try:
        my_number = int(input("Please guess a number between 1~100: "))
        
        if my_number > random_number:
            print("Down")
        elif my_number < random_number:
            print("up")
        elif my_number == random_number:
            print(f"Congrats!! \nGame_count: {game_count}!!!")
            break
        
    except:
        print("Please enter a valid number")
        continue

    game_count = game_count + 1