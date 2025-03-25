import os, platform, time, sys
try:
 import requests

 
print(' [+] Chekking Comand update')
print('\033[1;32m') 
os.system('  git pull')
ranaxd = platform.architecture()[0]
if ranaxd == '64bit':
 print(' [+] Your Device is 64bit')
 import M64
elif ranaxd == '32bit':
 print(' [+] Your Devive is 32bit')
 import M64
 
