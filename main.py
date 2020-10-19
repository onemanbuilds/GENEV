from xeger import Xeger
from string import ascii_letters,ascii_lowercase,ascii_uppercase,digits
from random import choice
from re import sub
import os
from colorama import init,Fore


class Main:

    def clear(self):
        if os.name == 'posix':
            os.system('clear')
        elif os.name in ('ce', 'nt', 'dos'):
            os.system('cls')
        else:
            print("\n") * 120

    def SetTitle(self,title_name:str):
        os.system("title {0}".format(title_name))

    def __init__(self):
        init(convert=True)
        self.clear()
        self.SetTitle('One Man Builds Customizable Gen Tool')
        title = Fore.YELLOW+"""
                                
                        ____ _  _ ____ ___ ____ _  _ _ ___  ____ ___  _    ____    ____ ____ _  _ 
                        |    |  | [__   |  |  | |\/| |   /  |__| |__] |    |___    | __ |___ |\ | 
                        |___ |__| ___]  |  |__| |  | |  /__ |  | |__] |___ |___    |__] |___ | \| 
                                                                                                
                                
        """
        print(title)
        self.option = int(input(Fore.YELLOW+'['+Fore.WHITE+'>'+Fore.YELLOW+'] Would you like to use [1]Custom Pattern [0]Custom Regex: '))
        self.amount = int(input(Fore.YELLOW+'['+Fore.WHITE+'>'+Fore.YELLOW+'] Enter the amount: '))

    def CustomPattern(self,custom_pattern):
        if 'C' in custom_pattern:
            custom_pattern = sub('C', lambda m: choice(ascii_uppercase), custom_pattern)
        if 'S' in custom_pattern:
            custom_pattern = sub('S', lambda m: choice(ascii_lowercase), custom_pattern)
        if 'N' in custom_pattern:
            custom_pattern = sub('N', lambda m: choice(digits), custom_pattern)
        if 'X' in custom_pattern:
            custom_pattern = sub('X', lambda m: choice(ascii_letters), custom_pattern)
        if 'Y' in custom_pattern:
            custom_pattern = sub('Y', lambda m: choice(ascii_uppercase + digits), custom_pattern)
        if 'V' in custom_pattern:
            custom_pattern = sub('V', lambda m: choice(ascii_lowercase + digits), custom_pattern)
        if 'A' in custom_pattern:
            custom_pattern = sub('A', lambda m: choice(ascii_letters + digits), custom_pattern)

        return custom_pattern

    def CustomRegex(self,regex_pattern):
        x = Xeger()
        code = x.xeger(regex_pattern)

        return code

    def CustomPatternGenerator(self,amount,custom_pattern):
        counter = 0
        for i in range(amount):
            code = self.CustomPattern(custom_pattern)
            counter = counter+1

            print(Fore.LIGHTGREEN_EX+'['+Fore.WHITE+f'{counter}'+Fore.LIGHTGREEN_EX+f'] {code}')

            with open('custom_pattern_generated.txt','a',encoding='utf8') as f:
                f.write(code+"\n")

    def CustomRegexGenerator(self,amount,regex_pattern):
        counter = 0
        for i in range(amount):
            code = self.CustomRegex(regex_pattern)
            counter = counter+1

            print(Fore.LIGHTGREEN_EX+'['+Fore.WHITE+f'{counter}'+Fore.LIGHTGREEN_EX+f'] {code}')

            with open('custom_regex_generated.txt','a',encoding='utf8') as f:
                f.write(code+"\n")

    def Start(self):
        if self.option == 1:
            print('')

            print(Fore.LIGHTGREEN_EX+'['+Fore.WHITE+'!'+Fore.LIGHTGREEN_EX+'] EXAMPLE: CSNXYV-CSYVXA-NXYVSC-YVXASC')
            print(Fore.LIGHTGREEN_EX+'['+Fore.WHITE+'!'+Fore.LIGHTGREEN_EX+'] C = CAPITAL LETTER | S = SMALL LETTER | N = NUMBER | X = CAPITAL OR SMALL LETTER')
            print(Fore.LIGHTGREEN_EX+'['+Fore.WHITE+'!'+Fore.LIGHTGREEN_EX+'] Y = CAPITAL LETTER OR NUMBER V = SMALL LETTER OR NUMBER | A = LETTER AND NUMBER')

            print('')
            custom_pattern = str(input(Fore.YELLOW+'['+Fore.WHITE+'>'+Fore.YELLOW+'] Enter your custom pattern: ')).upper()
            print('')
            self.CustomPatternGenerator(self.amount,custom_pattern)
        else:
            print('')
            regex_pattern = str(input(Fore.YELLOW+'['+Fore.WHITE+'>'+Fore.YELLOW+'] Enter your custom regex pattern: '))
            print('')
            self.CustomRegexGenerator(self.amount,regex_pattern)
        
        self.Start()

if __name__ == '__main__':
    main = Main()
    main.Start()