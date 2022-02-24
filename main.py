#!/usr/bin/env python
#
# BruteForce Script Version 1.0.0 (2022)
#
# This tool may be used for legal purposes only.  Users take full responsibility
# for any actions performed using this tool. The author accepts no liability for
# damage caused by this tool.  If these terms are not acceptable to you, then do
# not use this tool.
#
# by Pierre CHAUSSARD & Nathan TEBOUL
# 
# 24-Feb-2022 - 1.0.0 - Creating basic script.

import pyfiglet,sys


try:
    ascii_banner = pyfiglet.figlet_format("BruteForce.PY")
    print(ascii_banner)

except KeyboardInterrupt:
        print("\n/!\ Exiting Program !")
        sys.exit()