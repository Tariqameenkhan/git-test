

TOTAL_ROUNDS = 5
import random

def game():
  print("Welcome to high low game.")
  print("-------------------------")
  round = 0
  score = 0 
  while round < TOTAL_ROUNDS:
    round = round + 1
    print(f"\nRound {round}")

    user_number = random.randint(1,100)
    computer_number = random.randint(1,100)
    print(f"your number is {user_number}")
    challenge = input("Do you think your number is higher or lower than computer number (higher/lower): ")
    if (challenge == "higher" and computer_number <user_number ) or (challenge == "lower" and computer_number> user_number):
        score = score + 1

        print(f"congrats ,the computer number is {computer_number}")
        print(f"Your score is {score}")
    else:
        print(f"Your answer is incorrect. the computer number is {computer_number}")
  print(f"your final score is {score}")


game()

# oop
import random
TOTAL_ROUNDS : int = 5

class Game():
    def __init__(self):
       pass
      
    def start(self):
        print("Welcome to high low game.")
        print("-------------------------") 
        round : int = 0
        score : int = 0
        while round < TOTAL_ROUNDS:
            self.user_number = random.randint(1,100)
            self.computer_number = random.randint(1,100)
            round = round + 1
            print(f"\nRound {round}")
            print(f"Your number is {self.user_number}")
            try:
              challenge = input("Do you think your number is higher or lower than computer number (higher/lower): ")
              if (challenge == "higher" and self.computer_number < self.user_number ) or (challenge == "lower" and self.computer_number> self.user_number):
                score = score + 1
                print(f"congrats ,the computer number is {self.computer_number}")
                print(f"Your score is {score}")
              else:
                print(f"Your answer is incorrect. the computer number is {self.computer_number}")
            except ValueError as e:
              print(f"Error occured {e}")
        print(f"your final score is {score}")

game = Game()
game.start()



# 3
# Milestone 1
def planet_weight():
    weight_on_earth : int = int(input("What is your weight on earth?: "))
    Mars_Weight = 0.37
    weight_on_mars = weight_on_earth * Mars_Weight
    print(f"your weight on mars is {weight_on_mars}")
planet_weight()

# Milestone 2
Mercury = 37.6

Venus =  88.9

Mars = 37.8

Jupiter = 236.0

Saturn = 08.1

Uranus = 81.5

Neptune = 114.0

def planet_weight():
    weight_on_earth : int = int(input("What is your weight on earth?: "))
    mercury = (weight_on_earth /100 ) * 37.6
    venus = (weight_on_earth / 100) * 88.9
    mars = (weight_on_earth / 100) * 37.8
    jupiter = (weight_on_earth / 100) * 236.0
    saturn = (weight_on_earth / 100) * 08.1
    uranus = (weight_on_earth / 100) * 81.5
    neptune = (weight_on_earth / 100) * 114.0
    which_planet : str = input("from which planet do calculate your weight: ")
    if which_planet == "Mercury":
        print("Your weight on mercury is ", mercury)
    elif which_planet == "Venus":
        print("Your weight on venus is ", venus)
    elif which_planet == "Mars":
        print("Your weight on mars is ", mars)
    elif which_planet == "Jupiter":
        print("Your weight on jupiter is ", jupiter)
    elif which_planet == "Saturn":
        print("Your weight on saturn is ", saturn)
    elif which_planet == "Uranus":
        print("Your weight on uranus is ", uranus)
    elif which_planet == "Neptune":
        print("Your weight on neptune is ", neptune)
    else:
        print("Invalid choice")
planet_weight()

