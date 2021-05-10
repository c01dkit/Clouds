
import requests
import threading
import os
from datetime import *
from learnEng.utils import log
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

def handle_file_name(ori:str):
    if not ori.endswith('.txt'):
        ori += '.txt'
    # ori = ori.replace(' ', '_')
    return ori

def download(url:str,localsaved:str):
    response = requests.get(url,headers=headers)
    dirpath = os.path.join(os.path.curdir,'ebooks')
    if not os.path.exists('ebooks'):
        os.mkdir('ebooks')
    if response.status_code == 200:
        bookname = handle_file_name(localsaved)
        with open(os.path.join(dirpath,bookname),'wb') as f:
            f.write(response.content)
    log.log(f'{url} {response.status_code} {response.reason}\n')


class multi_download(threading.Thread):
    def __init__(self,target:str,localname:str):
        threading.Thread.__init__(self)
        self.target = target
        self.name = handle_file_name(localname)

    def run(self) -> None:
        response = requests.get(self.target,headers=headers)
        if response.status_code == 200:
            with open(self.name,'wb') as f:
                f.write(response.content)
        else:
            print(response.reason)

if __name__ == '__main__':
    # book1 = multi_download('https://www.gutenberg.org/files/65276/65276-0.txt','A History of Sculpture')
    # book1.start()
    download('https://www.gutenberg.org/files/65276/65276-0.txt','A History of Sculpture')