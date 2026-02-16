import random 
import math
def guessing_game():
    print("Welcome to the Number Guessing Game ")
    
    try:
        low=int(input("Enter the lower bound :"))
        high=int(input("Enter the upper bound :"))
        
        if low>=high:
            print("Lower bound must be smaller than upper bound")
            return
         
    except ValueError:
        print("Invalid Input! Enter integers only")
        return
    
    num=random.randint(low,high)
    max_attempts=math.ceil(math.log2(high-low+1))
    print(f"\n You have {max_attempts} attempts")
    
    for i in range(1,max_attempts+1):
        try:
            guess=int(input(f"Enter guess {i} :"))
        except ValueError:
            print("Invalid input")
            continue
        
        if guess == num:
            print(f"Correct! You guessed in {i} attempts")
            return 
        
        elif guess < num :
            print("Too low")
        
        else:
            print("Too high")


"""
#Output 1
Welcome to the Number Guessing Game 
Enter the lower bound :5
Enter the upper bound :10

You have 3 attempts
Enter guess 1 :6
Correct! You guessed in 1 attempts


#Output 2
Welcome to the Number Guessing Game 
Enter the lower bound :1
Enter the upper bound :100

You have 7 attempts
Enter guess 1 :56
Too low
Enter guess 2 :78
Too low
Enter guess 3 :89
Too low
Enter guess 4 :90
Too low
Enter guess 5 :97
Too low
Enter guess 6 :99
Too high
Enter guess 7 :12
Too low
Game Over! The number is 98
        
    print(f"Game Over! The number is {num}")       
    
guessing_game(); 
"""

        
