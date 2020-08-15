class Game:


    def __init__(self, word):

        self.guessed = []
        self.lives = 6
        self.word = word
        self.display = ['_' for _ in self.word]
        self.alive = True
        self.win = False
        self.message = ""


    def __str__(self):

        s = '\n' * 25
        s += "Lives: {} \nLetters Guessed: {} \n\nWord: {}\n".format(self.lives, self.guessed, self.display)
        s += self.message + '\n'

        return s

    def clean_guess(self, c):

        if type(c) == str and len(c) == 1:
            if c in self.guessed:
                self.message = 'You have already guessed ' + c + '.'
                return None
            return c
        elif len(c) > 1:
            self.message = 'Guess must be 1 letter only.'
            return None
        else:
            self.message = 'Guess was ' + type(c) + ' but it must be a character.'
            return None

    def success(self, c):
        ## update display
        for i in range(len(self.word)):

            if c == self.word[i]:
                self.display[i] = c

        if list(self.word) == self.display:
            self.win = True

        self.message = "There is a " + c

    def lose_life(self):

        self.lives -= 1

        if self.lives <= 0:
            self.alive = False
            self.message += "\n\nYou have been hanged."

    def fail(self, c):

        self.guessed.append(c)
        self.lose_life()
        self.message = "There is no " + c

    def process_guess(self, c):

        letter = self.clean_guess(c)

        if letter is not None:
            if letter in self.word:
                self.success(letter)
            else:
                self.fail(letter)
