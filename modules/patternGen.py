from modules.helpers import _initTitle,_writeFile,_print,_printInfo
from threading import Thread,active_count
from pystyle import Colors
from random import choice
from string import ascii_uppercase,ascii_lowercase,digits,ascii_letters

class PatternGen:
    def __init__(self,config) -> None:
        _initTitle('GENEV [PATTERN]')
        _printInfo(1)
        self.method = config['method']
        self.threads = config['threads']+20
        self.amount = config['amount']
        self.created = 0
        self.pattern = str(input(f'{Colors.cyan}[{Colors.yellow}>{Colors.cyan}] {Colors.cyan}Enter your pattern:{Colors.yellow} '))
        print('')

    def _generate(self):
        final_pattern = self.pattern
        try:
            if 'C' in final_pattern:
                final_pattern = final_pattern.replace('C',choice(ascii_uppercase))
            if 'S' in final_pattern:
                final_pattern = final_pattern.replace('S',choice(ascii_lowercase))
            if 'N' in final_pattern:
                final_pattern = final_pattern.replace('N',choice(digits))
            if 'X' in final_pattern:
                final_pattern = final_pattern.replace('X',choice(ascii_letters))
            if 'Y' in final_pattern:
                final_pattern = final_pattern.replace('Y',choice(ascii_uppercase+digits))
            if 'V' in final_pattern:
                final_pattern = final_pattern.replace('V',choice(ascii_lowercase+digits))
            if 'A' in final_pattern:
                final_pattern = final_pattern.replace('A',choice(ascii_letters+digits))
            self.created += 1
            _print(Colors.cyan,Colors.green,str(self.created),final_pattern)
            _writeFile('saved/pattern_gen.txt',final_pattern)
        except Exception:
            self._generate()

    def _start(self):
        if self.method == 1:
            if self.amount > 0:
                threads = []
                for i in range(self.amount):
                    run = True
                    while run:
                        if active_count()<=self.threads:
                            thread = Thread(target=self._generate)
                            threads.append(thread)
                            thread.start()
                            run = False
                for x in threads:
                    x.join()
            else:
                run = True
                while run:
                    if active_count()<=self.threads:
                        thread = Thread(target=self._generate)
                        thread.start()
        else:
            if self.amount > 0:
                for i in range(self.amount):
                    self._generate()
            else:
                while True:
                    self._generate()
        print('')
        _print(Colors.cyan,Colors.yellow,'FINISH','Process done!')
