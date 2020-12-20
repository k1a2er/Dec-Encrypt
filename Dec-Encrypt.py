import compileall
import os,sys,time
from datetime import datetime
os.system('pip install uncompyle6')
a = datetime.now().strftime('%Y-%m-%d %H:%M')
os.system('git pull')
def jalan (z):
    for e in z +'\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.02)
logo = """
\033[1;36m███████╗███╗░░██╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗  \033[1;31m░█████╗░███╗░░██╗██████╗░
\033[1;36m██╔════╝████╗░██║██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝  \033[1;31m██╔══██╗████╗░██║██╔══██╗
\033[1;36m█████╗░░██╔██╗██║██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░  \033[1;31m███████║██╔██╗██║██║░░██║
\033[1;36m██╔══╝░░██║╚████║██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░  \033[1;31m██╔══██║██║╚████║██║░░██║
\033[1;36m███████╗██║░╚███║╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░  \033[1;31m██║░░██║██║░╚███║██████╔╝
\033[1;36m╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░  \033[1;31m╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░

\033[1;35m██████╗░███████╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗
\033[1;35m██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝
\033[1;35m██║░░██║█████╗░░██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░
\033[1;35m██║░░██║██╔══╝░░██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░
\033[1;35m██████╔╝███████╗╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░
\033[1;35m╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░

"""
os.system('clear')
jalan("\033[1;32mPlease subscribe to my YouTube channel to learn more about hackers and programming")
time.sleep(00000.08)
os.system('xdg-open www.youtube.com/c/sniper9nine')
print(logo)
print('\033[1;36m+++++++++++++++++++++++++++++++++++++++++++++++++++++++'),time.sleep(0.3)
print('\033[1;31m[1] \033[1;36mEncrypt | py to pyc'),time.sleep(0.3)
print('\033[1;31m[2] \033[1;35mDecode  | pyc to py'),time.sleep(0.3)
print('\033[1;36m+++++++++++++++++++++++++++++++++++++++'+a),time.sleep(0.3)
choose =input('\n\033[1;31m[?]Choose : \033[1;37m')
if choose =='1':
    file_py = input("\n\033[1;32mFile >\033[1;37m")
    compileall.compile_file(file_py)
    print('\033[1;31msuccess encrypt')
    print("\033[1;36mSave to __pycache__")
elif choose =='2':
    file_pyc = input('\n\033[1;32mFile >\033[1;37m')
    com = f'uncompyle6 {file_pyc} > dec.py'
    os.system(com)
    print('\033[1;31mdecoding success')
else:
    print('\033[1;31mplease choose 1 or 2 !')
