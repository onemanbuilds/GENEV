from modules.helpers import _initTitle,_writeFile,_print,_printInfo
from threading import Thread,active_count
from pystyle import Colors
from xeger import Xeger

class RegexGen:
    def __init__(self,config) -> None:
        _initTitle('GENEV [REGEX]')
        _printInfo(2)
        self.method = config['method']
        self.threads = config['threads']+20
        self.amount = config['amount']
        self.x = Xeger()
        self.created = 0
        self.pattern = str(input(f'{Colors.cyan}[{Colors.yellow}>{Colors.cyan}] {Colors.cyan}Enter your pattern:{Colors.yellow} '))
        print('')

    def _generate(self):
        try:
            final_pattern = self.x.xeger(self.pattern)
            self.created += 1
            _print(Colors.cyan,Colors.green,str(self.created),final_pattern)
            _writeFile('saved/regex_gen.txt',final_pattern)
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
