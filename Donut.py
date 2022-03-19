#] Start of Imports
from encodings import utf_8
from math import sin, cos
import json, os, logging, sys
#] End of Imports

#] Start of Configuration
if not os.path.isfile("config.json"):
    logging.warning("[!] FATAL: Failed To Load. config.json not found!")
    sys.exit("[!] config.json not found!")

with open("Donut/config.json") as file:
    Config = json.load(file)
    SpinSpeed_1, SpinSpeed_2, SpinSpeed_3, SpinSpeed_4 = Config["spinSpeed"]
    TermWidth, TermHight = Config["termWidth"], Config["termHight"]
    DonutCharacters = Config["characters"]
    Pi = Config["pi"]
#] End of Configuration

Banner = '''
          [38;2;99;65;128m██████╗  ██████╗ ███╗   ██╗██╗   ██╗████████╗  ██████╗ ██╗   ██╗
          [38;2;105;66;129m██╔══██╗██╔═══██╗████╗  ██║██║   ██║╚══██╔══╝  ██╔══██╗╚██╗ ██╔╝
          [38;2;111;68;130m██║  ██║██║   ██║██╔██╗ ██║██║   ██║   ██║     ██████╔╝ ╚████╔╝
          [38;2;118;69;131m██║  ██║██║   ██║██║╚██╗██║██║   ██║   ██║     ██╔═══╝   ╚██╔╝
          [38;2;124;71;132m██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝   ██║ ██╗ ██║        ██║
          [38;2;130;73;133m╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝    ╚═╝ ╚═╝ ╚═╝        ╚═╝
                               🍩  \x1b[1m\x1b[35mMade\x1b[0m \x1b[1mBy\x1b[0m \x1b[1m\x1b[36mBLU3\x1b[0m 🍩
    '''

def main() -> None:
    Set = Set2 = 0

    while 1:
        BackSize_1, BackSize_2 = [' '] * TermHight * TermWidth, [0] * 4 * TermHight * TermWidth

        Set3 = 0
        while Set3 < Pi:
            Set3 += SpinSpeed_3
            Set4 = 0

            while Set4 < Pi: #] Lots O' Math
                Set4 += SpinSpeed_4

                do, blu3, nut, el, heke, ez, hello, haxor = (
                    *map(sin, (Set, Set2, Set3, Set4)), *map(cos, (Set, Set2, Set3, Set4))
                )

                py, lol = 1/(nut*(haxor+2)*do+el*heke+5), nut*(haxor+2)*heke-el*do

                MeshWorker = int(
                    (x := int(TermWidth/2+30*py*(hello*(haxor+2)*ez-lol*blu3)))
                    + TermWidth * (y := int(TermHight/2+15*py*(hello*(haxor+2)*blu3+lol*ez)))
                )

                if 0 < y < TermHight and 0 < x < TermWidth and BackSize_2[MeshWorker] < py:
                    Glaze = int(8*((el*do-nut*haxor*heke)*ez-nut*haxor*do-el*heke-hello*haxor*blu3))

                    BackSize_2[MeshWorker] = py
                    BackSize_1[MeshWorker] = DonutCharacters[max(Glaze, 0)]

        print(TerminalController(BackSize_1))

        #] Increments
        Set += SpinSpeed_1
        Set2 += SpinSpeed_2

#] Terminal & Cursor Control
def TerminalController(term: list[str]) -> str:
    return (
        ']\33[?25l'
        ']\33[H'
        ']\033[2J\033[H'
        f'{Banner}'
        '[0m'
        '[1m'
) + ''.join('\n' if Do % TermWidth == 0 else Nut for Do, Nut in enumerate(term)) 
#] Using Essential Terminal Control Sequences & Fun Banner

main() #] Donut :)