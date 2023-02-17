#wap to print Gussing game
winning_num = 43
guess =1
num  = input("Guess a Num Between 1 to 100:")
num = int(num)
game_over = False

while not game_over:
    if num == winning_num:
        #user win 
        print(f"You Win and You Gessed This num in {guess} time")
        game_over = True
    else:
        if num >winning_num:
            print("too Low")

            guess+=1
        else:
            print("Too High")

            guess +=1
        num =int(input("Guess Angain?"))