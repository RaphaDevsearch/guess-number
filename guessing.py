import random as rd

class NumberGuessing:
    def __init__(self, min_number, max_number):
        self.min = min_number
        self.max = max_number
        self.secretNumber = self.min + self.max
        self.trie = 0
        
    def check_guess(self, guess):
        print('guessing ...',guess)
    
    def play(self):
        guess = 6
        print('Playing')
        self.check_guess(guess)
    

if __name__ == "__main__":
    g = NumberGuessing(2,6)
    g.play()