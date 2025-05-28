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
    
    def play(self):
        guess = int(input("guess : ")) # input user
        
        while True :
            if not self.is_right(guess):
                guess = int(input("guess again ")) # input user
                
                self.trie += 1
                if self.trie >= self.life -1 :
                    print("Lose :(")
                    break
            
            else :
                print("Bravo :)")
                break
            
        
        # while not self.check_guess(guess) and self.life > 1:
        #     guess = int(input(f"guess again :{self.life} left : "))
        #     self.life -= 1
        


if __name__ == "__main__":
    g = NumberGuessing(2,6)
    g.play()