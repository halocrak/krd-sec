import os
import random
from colorama import Fore, Back, Style
list_rangakan = [Fore.GREEN, Fore.YELLOW, Fore.RED ,Fore.BLUE,Fore.MAGENTA]
os.system("rm -fr sql.txt")
os.system("clear")
mrx=random.choice(list_rangakan)
mrx1=random.choice(list_rangakan)
logo=mrx+'''

 ██ ▄█▀ ██▀███  ▓█████▄      ██████ ▓█████  ▄████▄  
 ██▄█▒ ▓██ ▒ ██▒▒██▀ ██▌   ▒██    ▒ ▓█   ▀ ▒██▀ ▀█  
▓███▄░ ▓██ ░▄█ ▒░██   █▌   ░ ▓██▄   ▒███   ▒▓█    ▄ 
▓██ █▄ ▒██▀▀█▄  ░▓█▄   ▌     ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒
▒██▒ █▄░██▓ ▒██▒░▒████▓    ▒██████▒▒░▒████▒▒ ▓███▀ ░
▒ ▒▒ ▓▒░ ▒▓ ░▒▓░ ▒▒▓  ▒    ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░
░ ░▒ ▒░  ░▒ ░ ▒░ ░ ▒  ▒    ░ ░▒  ░ ░ ░ ░  ░  ░  ▒   
░ ░░ ░   ░░   ░  ░ ░  ░    ░  ░  ░     ░   ░        
░  ░      ░        ░             ░     ░  ░░ ░      
                 ░                         ░        
                 TELEGRAM : i4m_mrx
                 SNAPCHAT : mrx_coder
                 INSTAGRAM : mrx_cod4r 
'''
print(logo)
halo=input(mrx1+"URL : ")
os.system(f"waybackurls {halo} > sql.txt")
os.system("bash sql.sh")