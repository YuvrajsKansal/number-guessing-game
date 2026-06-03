from random import randint
def play_game():
    number = randint(1,100)
    difficulty = 0
    
    print("Choose difficulty level\n 1)Easy   (15 tries)\n 2)Medium (10 tries)\n 3)Hard   ( 5 tries)")
    while True:
        try:
            difficulty = int(input("enter here (1,2,3): "))
            if difficulty not in [1,2,3]:
                print("Invalid input. Please enter a number (1, 2, or 3).")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")
        
    guesses=[]
    rate = lambda f,d:"Excellent" if f<=d//3 else "Great" if f<=d//2 else "Keep Going"
    guess = None
    difficulty = 20 - difficulty*5
    print("difficulty set to",difficulty,"tries")
    for i in range(1,difficulty+1):
        while True:
            try:
                guess=int(input(f"guess number {i}: "))
                break
            except ValueError:
                print("invalid input, try again..")
                continue
        guesses.append(guess)
        if guess==number:
            print(f"well done you took {i} tries",f",rating:{rate(i,difficulty)}")
            break
        if i<difficulty:
            if guess>number:
                print("lower")
            else:
                print("higher")
    if guess!=number:
        print(f"You lost the number was: {number}")
    print("Your guesses: " + ", ".join([str(g) for g in guesses]))

play_game()
while True:
    again=input("Would you like to play again(y/n)").strip().lower()
    if again!="y":
        break
    else:
        play_game()
    

