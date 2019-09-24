#!usr/bin/python3
from subprocess import run
from os import getcwd
file = input('\n\nEnter The Filename[ie: file.py]:');compiled = False
try:
    stack = ['pyinstaller', '-F', file]
    run(stack);compiled = True
except Exception as Ee:
    print(str(Ee))
    compiled = False
    wait = input('\n\nFailed! Mash Any Key To Exit')  
if compiled == True:
    this_dir = str(getcwd())
    nu_file = str(file.replace("py", "exe"))
    print(f"\nSuccess! Binary located @ {this_dir}\\dist\\{nu_file}")
else:
    wait1 = input('\n\nFailed! Mash Any Key To Exit')
