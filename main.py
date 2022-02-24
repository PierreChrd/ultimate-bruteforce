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

def section_print(title):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50 + "\n")


def menu():  
        ascii_banner = pyfiglet.figlet_format("BruteForce.PY")
        print(ascii_banner)

        x = int(input("Choose your service :\n 1. SSH.\n 2. HTTP.\n\n>"))

        if x == 1:
                section_print("SSH BruteForce")
        elif x == 2:
                section_print("HTTP BruteForce")


try:
        menu()

except KeyboardInterrupt:
        print("\n/!\ Exiting Program !")
        sys.exit()