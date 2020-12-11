from xeger import Xeger
from string import ascii_letters,ascii_lowercase,ascii_uppercase,digits
from random import choice
from re import sub
from os import name,system
from sys import stdout
from threading import Thread,Lock,active_count
from time import sleep

def clear():
    if name == 'posix':
        system('clear')
    elif name in ('ce', 'nt', 'dos'):
        system('cls')
    else:
        print("\n") * 120

def SetTitle(title:str):
    if name == 'posix':
        stdout.write(f"\x1b]2;{title}\x07")
    elif name in ('ce', 'nt', 'dos'):
        system(f'title {title}')
    else:
        stdout.write(f"\x1b]2;{title}\x07")

class PatternGen: #some lines are missing at the end with faster method
    def __init__(self):
        SetTitle('[One Man Builds Customizable Gen] ^| [PATTERN GENERATION]')
        clear()
        self.title = """
                         ╔═════════════════════════════════════════════════════════════════╗
                                 ╔═╗╔═╗╔╦╗╔╦╗╔═╗╦═╗╔╗╔  ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╦╔═╗╔╗╔
                                 ╠═╝╠═╣ ║  ║ ║╣ ╠╦╝║║║  ║ ╦║╣ ║║║║╣ ╠╦╝╠═╣ ║ ║║ ║║║║
                                 ╩  ╩ ╩ ╩  ╩ ╚═╝╩╚═╝╚╝  ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩ ╩ ╩╚═╝╝╚╝
                         ╚═════════════════════════════════════════════════════════════════╝
                 ═══════════════════════════════════════════════════════════════════════════════════
                  [C] CAPITAL LETTER | [S] SMALL LETTER | [N] NUMBER | [X] CAPITAL OR SMALL LETTER
                  [Y] CAPITAL LETTER OR NUMBER | [V] SMALL LETTER OR NUMBER | [A] LETTER AND NUMBER
                 ═══════════════════════════════════════════════════════════════════════════════════
        """
        print(self.title)
        self.method = int(input('\t\t\t [>] [1]Faster [2]Accurate: '))
        self.threads = 1

        if self.method == 1:
            self.threads = int(input('\t\t\t [>] Threads: '))

        self.amount = int(input('\t\t\t [>] Amount (0 for unlimited): '))
        self.pattern = str(input('\t\t\t [>] Pattern: '))
        self.generated = 0
        print('')

    def PatternGen(self):
        try:
            string = self.pattern
            if 'C' in string:
                string = sub('C', lambda m: choice(ascii_uppercase), string)
            if 'S' in string:
                string = sub('S', lambda m: choice(ascii_lowercase), string)
            if 'N' in string:
                string = sub('N', lambda m: choice(digits), string)
            if 'X' in string:
                string = sub('X', lambda m: choice(ascii_letters), string)
            if 'Y' in string:
                string = sub('Y', lambda m: choice(ascii_uppercase + digits), string)
            if 'V' in string:
                string = sub('V', lambda m: choice(ascii_lowercase + digits), string)
            if 'A' in string:
                string = sub('A', lambda m: choice(ascii_letters + digits), string)

            self.generated += 1
            print(f'\t\t\t [{self.generated}] {string}')
            with open('pattern_generated.txt','a',encoding='utf8') as f:
                f.write(string+'\n')
        except:
            self.PatternGen()

    def Start(self):
        if self.method == 1:
            if self.amount > 0:
                threads = []
                for i in range(self.amount):
                    Run = True
                    while Run:
                        if active_count() <= self.threads:
                            thread = Thread(target=self.PatternGen)
                            threads.append(thread)
                            thread.start()
                            Run = False
        
                for x in threads:
                    x.join()

                print('')
                print('\t\t\t [#] PATTERN GENERATION DONE! RETURNING TO MENU')
                sleep(2)
            else:
                while True:
                    if active_count() <= self.threads:
                        Thread(target=self.PatternGen).start()
        else:
            if self.amount > 0:
                for i in range(self.amount):
                    self.PatternGen()
                print('')
                print('\t\t\t [#] PATTERN GENERATION DONE! RETURNING TO MENU')
                sleep(2)
            else:
                while True:
                    self.PatternGen()

class RegexGen: #some lines are missing at the end with faster method
    def __init__(self):
        SetTitle('[One Man Builds Customizable Gen] ^| [REGEX GENERATION]')
        clear()
        self.title = """
                         ╔═════════════════════════════════════════════════════════════════╗
                                   ╦═╗╔═╗╔═╗╔═╗═╗ ╦  ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╦╔═╗╔╗╔
                                   ╠╦╝║╣ ║ ╦║╣ ╔╩╦╝  ║ ╦║╣ ║║║║╣ ╠╦╝╠═╣ ║ ║║ ║║║║
                                   ╩╚═╚═╝╚═╝╚═╝╩ ╚═  ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩ ╩ ╩╚═╝╝╚╝
                         ╚═════════════════════════════════════════════════════════════════╝
        """
        print(self.title)
        self.method = int(input('\t\t\t [>] [1]Faster [2]Accurate: '))
        self.threads = 1

        if self.method == 1:
            self.threads = int(input('\t\t\t [>] Threads: '))

        self.amount = int(input('\t\t\t [>] Amount (0 for unlimited): '))
        self.pattern = str(input('\t\t\t [>] Pattern: '))
        self.x = Xeger()
        self.generated = 0
        print('')

    def RegexGen(self):
        try:
            string = self.x.xeger(self.pattern)
            self.generated += 1
            print(f'\t\t\t [{self.generated}] {string}')
            with open('regex_generated.txt','a',encoding='utf8') as f:
                f.write(string+'\n')
        except:
            self.RegexGen()

    def Start(self):
        if self.method == 1:
            if self.amount > 0:
                threads = []
                for i in range(self.amount):
                    Run = True
                    while Run:
                        if active_count() <= self.threads:
                            thread = Thread(target=self.RegexGen)
                            threads.append(thread)
                            thread.start()
                            Run = False
        
                for x in threads:
                    x.join()

                print('')
                print('\t\t\t [#] REGEX GENERATION DONE! RETURNING TO MENU')
                sleep(2)
            else:
                while True:
                    if active_count() <= self.threads:
                        Thread(target=self.RegexGen).start()
        else:
            if self.amount > 0:
                for i in range(self.amount):
                    self.RegexGen()
                print('')
                print('\t\t\t [#] REGEX GENERATION DONE! RETURNING TO MENU')
                sleep(2)
            else:
                while True:
                    self.RegexGen()

class Main:
    def __init__(self):
        SetTitle('[One Man Builds Customizable Gen] ^| [MENU]')
        clear()
        self.title = """
                         ╔═════════════════════════════════════════════════════════════════╗
                                                     ╔╦╗╔═╗╔╗╔╦ ╦
                                                     ║║║║╣ ║║║║ ║
                                                     ╩ ╩╚═╝╝╚╝╚═╝
                         ╚═════════════════════════════════════════════════════════════════╝
        """
        print(self.title)

    def Menu(self):
        SetTitle('[One Man Builds Customizable Gen] ^| [MENU]')
        clear()
        print(self.title)
        functions = ['Pattern Generation','Regex Generation']
        counter = 0
        for function in functions:
            counter += 1
            print(f'\t\t\t [{counter}] {function}')

        print('')
        option = int(input('\t\t\t [>] Choose something: '))
        print('')

        if option == 1:
            pattern_gen = PatternGen()
            pattern_gen.Start()
            self.Menu()
        elif option == 2:
            regex_gen = RegexGen()
            regex_gen.Start()
            self.Menu()
        else:
            self.Menu()

if __name__ == "__main__":
    main = Main()
    main.Menu()