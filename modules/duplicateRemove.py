from modules.helpers import _initTitle,_print,_readFile
from pystyle import Colors
from time import sleep

class DuplicateRemove:
    def __init__(self) -> None:
        _initTitle('GENEV [DUPLICATE REMOVE]')
        self.remove_from_path = str(input(f'{Colors.cyan}[{Colors.yellow}>{Colors.cyan}] {Colors.cyan}Path to file:{Colors.yellow} '))
        print('')

    def _remove(self):
        try:
            content = _readFile(self.remove_from_path,'r',1)
            started_length = len(content)
            output_set = set(content)
            
            with open('saved/no_dupes.txt','w+',encoding='utf8') as f:
                f.write('\n'.join(output_set))

            final_length = len(output_set)
            removed_lines = started_length-final_length

            _print(Colors.cyan,Colors.green,'FINISH',f'START LENGTH <{started_length}> - FINAL LENGTH <{final_length}> - REMOVED <{removed_lines}>')
            sleep(2)
        except Exception:
            pass

    def _start(self):
        self._remove()

        print('')
        _print(Colors.cyan,Colors.yellow,'FINISH','Process done!')
