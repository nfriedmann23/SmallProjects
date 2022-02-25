import sys
import datetime
import random
from termcolor import colored

class numgenerator():
    def __init__(self):
        self.getnum()
    
    def getnum(self):
        self.datenow = str(datetime.date.today()).replace('-','')
        random.seed(int(self.datenow))
        self.anstoday =  str(random.randint(1000, 9999))
        return self.anstoday


class guesssystem():
    def __init__(self):
        self.todaysstring = numgenerator().getnum()
        print(self.todaysstring)
        self.user_input()

    def user_input(self, i=4):
        if i == -1:
            print('Sorry, you tried!')
            sys.exit()
        self.usrinput = input('Please enter a 4 digit number, you have 5 attempts: ')
        while len(self.usrinput) != 4 or self.usrinput.isnumeric() is False:
            if self.usrinput.isnumeric() is False:
                self.usrinput = input('Please only enter 4 digit numbers, no letters: ')
            elif len(self.usrinput) > 4:
                self.usrinput = input('Your number is too long, please enter a 4 digit number: ')
            elif len(self.usrinput) < 4:
                self.usrinput = input('Your number is too short, please enter a 4 digit number: ')
            else:
                pass
        self.comparitor(self.usrinput, i)
    
    def comparitor(self, userguess, i):
        if userguess == self.todaysstring:
            print(colored(userguess, 'green') + '\nCongratulations! You guessed correct!')
            pass
        else:
            self.guesslist = list(userguess)
            self.anslist = list(self.todaysstring)
            self.output = ''
            pos = 0
            for num in self.guesslist:
                if num in self.anslist and self.anslist[pos] == self.guesslist[pos]:
                    self.output = self.output + colored(num, 'green')
                elif num in self.anslist and self.anslist[pos] != self.guesslist[pos]:
                    self.output = self.output + colored(num, 'yellow')
                elif num not in self.anslist:
                    self.output = self.output + colored(num, 'red')
                pos = pos + 1
            print(f'You selected \n' + self.output + f'\n{i} guesses remaining')
            i = i - 1
            self.user_input(i)

guesssystem()
