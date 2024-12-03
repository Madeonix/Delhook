import requests
import os
from colorama import Fore
import time

os.system('cls')

print(Fore.BLUE + """
▓█████▄ ▓█████  ██▓     ██░ ██  ▒█████   ▒█████   ██ ▄█▀
▒██▀ ██▌▓█   ▀ ▓██▒    ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒ 
░██   █▌▒███   ▒██░    ▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░ 
░▓█▄   ▌▒▓█  ▄ ▒██░    ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄ 
░▒████▓ ░▒████▒░██████▒░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄
 ▒▒▓  ▒ ░░ ▒░ ░░ ▒░▓  ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒
 ░ ▒  ▒  ░ ░  ░░ ░ ▒  ░ ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░
 ░ ░  ░    ░     ░ ░    ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░ 
   ░       ░  ░    ░  ░ ░  ░  ░    ░ ░      ░ ░  ░  ░   
 ░                                                      
""")

print(Fore.GREEN + "Paste Your Webhook To Delete It")
hook = input()
time.sleep(1)

requests.delete(hook)

print(Fore.GREEN + "Succesfully Deleted")

input()