from modules.helpers import _initTitle,_readJson,_print
from modules.patternGen import PatternGen
from modules.regexGen import RegexGen
from modules.duplicateRemove import DuplicateRemove
from time import sleep
from pystyle import Colors

class Menu:
    def __init__(self) -> None:
        _initTitle('GENEV [MENU]')

    def _menu(self):        
        _initTitle('GENEV [MENU]')

        self.config = _readJson('config/config.json','r')

        options = ['Pattern Gen','Regex Gen','Duplicate Remove']
        counter = 0
        for option in options:
            counter+=1
            _print(Colors.cyan,Colors.yellow,str(counter),option)
        print('')

        selected = int(input(f'{Colors.cyan}[{Colors.yellow}>{Colors.cyan}] {Colors.cyan}Select something:{Colors.yellow} '))

        if selected == 1:
            PatternGen(self.config)._start()
            sleep(2)
            self._menu()
        elif selected == 2:
            RegexGen(self.config)._start()
            sleep(2)
            self._menu()
        elif selected == 3:
            DuplicateRemove()._start()
            sleep(2)
            self._menu()
        else:
            self._menu()