#Dry --> don't repeat your self

winning_num = 43

guess = 1

game_over = False
num = int(input("Please Guess The Num of 1 to 100:"))

while not game_over:
    if num == winning_num:
        print(f"you Win! , and You Guessed this num in:{guess} time")
        game_over= True
    else:
        if num>winning_num:
            print("Too Low")
        else:
            print("Too Hight")
    guess +=1
    num = int(input("Try Again??"))