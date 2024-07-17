#pip install pyfiglet

import sys
from pyfiglet import Figlet

figlet = Figlet()

if sys.argv[1] == "-f" or sys.argv[1] == "--font":
    if len(sys.argv) == 3:
        figlet.setFont(font = sys.argv[2])
        print(figlet.renderText(input("Input: ")))# , font=sys.argv[1]     #fonts -> big, banner, slant
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
