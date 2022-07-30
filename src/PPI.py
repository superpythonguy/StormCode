ver = 1.0 #announce to clients
print(f'''
      +---------------------------------------------------+\n
      Welcome to the Easy Python package installer (PPI)\n
      {ver}\n
      +---------------------------------------------------+            
      ''')
import os
import platform
import psutil
import colorama
from colorama import *

colorama.init(autoreset=True)
OS = platform.system()

print(psutil.sensors_battery())
print("")

def list():
    list = os.system(f'cmd /k "pip list"')
    print("Curently installed packages "+list)

mode = input(Fore.GREEN+"Enter what you want to do?\nInstall a package = 1\nuninstall a package = 2\nlist all packages = 3\nPython version = 4\nSearch for new packages = 5\nQuit = 6\n")
if mode == "1":
    print(Fore.BLUE+"Operating System: "+OS)
    package=input(Fore.GREEN+"Enter package you want to install >>>\n")
    os.system(f'cmd /k "pip install {package}"')
    Fore.RESET
elif mode == "2":
    print(Fore.BLUE+"Operating System: "+OS)
    package=input(Fore.GREEN+"Enter package you want to uninstall >>>\n")
    Fore.RESET
elif mode == "3":
    os.system(f'cmd /k "pip list"')
elif mode == "4":
    print(f"Python version is "+platform.python_version())

elif mode == "5":
    print(Fore.BLUE+"Operating System: "+OS)
    package=input(Fore.GREEN+"Enter package(s) you want to search for >>>\n")
    os.system(f"cmd /k pip search {package}")