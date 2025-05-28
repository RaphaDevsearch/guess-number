import random as rd

class NumberGuessing:
    def __init__(self, min_number, max_number):
        self.min = min_number
        self.max = max_number
        self.secretNumber = self.min + self.max
        self.trie = 0
        self.life = 4
        
    def is_right(self, guess):
        return guess == self.secretNumber
    
    def msg(self, message):
        print(message)
    
    def msg_scor(self):
        self.msg(f"trie = {self.trie}")
        self.msg(f"life = {self.life - self.trie} left")
    
    def help(self, guess):
        if guess <= self.min :
            self.msg("too low, move right")
        elif guess >= self.max:
            self.msg("Too hight, move left")
        elif self.min < guess < self.max:
            self.msg("on way")
            if guess > self.secretNumber:
                self.msg("move left")
            else:
                self.msg("Move right")
    
    def play(self):
        guess = int(input("guess : ")) # input user
        self.trie = 1
        # self.help(guess)
        
        
        while True :
            if not self.is_right(guess):
                self.help(guess)
                guess = int(input("guess again ")) # input user
                
                
                self.trie += 1
                
                if self.trie - self.life == 0:
                    self.msg(f"Lose :(, the truth is {self.secretNumber}")
                    self.msg_scor()
                    break
            
            else :
                self.msg("Bravo :)")
                self.msg_scor()
                break
            
            


if __name__ == "__main__":
    g = NumberGuessing(2,6)
    g.play()