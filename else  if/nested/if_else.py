#num Gussing Game 
#make a var, like winning_num and assing any num to it
#ask user to guess a num 
#if user gussed correctly then print  "You Win!!!"
#if user did't guessed correctly then : 
#if num them print "too Lower"
#if user guessed higher then actual num then print "too Hight"

#google "how to generate randome num in python" to generated randome
#wining num 

#solve 

winning_num =24

guess_num = int(input("Guess The num between 1 to 100"))

if guess_num == winning_num:
    print("You Win!!!")
else:
    if guess_num>winning_num:
      print("Too High")
    else:
      print(" Too Lower ")