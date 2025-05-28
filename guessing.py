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
    
    def play(self):
        guess = int(input("guess : ")) # input user
        
        while True :
            if not self.is_right(guess):
                guess = int(input("guess again ")) # input user
                
                self.trie += 1
                if self.trie >= self.life -1 :
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