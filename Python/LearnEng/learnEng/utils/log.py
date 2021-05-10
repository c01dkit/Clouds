import os
from datetime import *

def log(sth:str):
    print(sth)
    sth = f'[{datetime.now()}]\t' + sth
    if not os.path.exists(os.path.join(os.path.curdir,'log.txt')):
        file = open('log.txt','w',encoding='utf-8')
        print(sth,file=file)
        file.close()
    else :
        with open('log.txt','a',encoding='utf-8') as f:
            print(sth,file=f)