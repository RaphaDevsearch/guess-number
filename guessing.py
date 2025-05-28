import random as rd

class NumberGuessing:
    def __init__(self, min_number, max_number):
        self.min = min_number
        self.max = max_number
        self.secretNumber = self.min + self.max
        self.trie = 0
        self.life = 4
        
    def check_guess(self, guess):
        print('guessing ...',guess)
        return guess == self.secretNumber
    
    def play(self):
        guess = int(input("guess : ")) # input user
        
        while not self.check_guess(guess):
            guess = int(input("guess again : "))
        

        print("ok you know ...")

if __name__ == "__main__":
    g = NumberGuessing(2,6)
    g.play()