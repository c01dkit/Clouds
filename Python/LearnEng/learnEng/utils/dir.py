import os

def ensure_dir(dirname:str):
    target = os.path.join(os.path.curdir,dirname)
    if not os.path.exists(target):
        os.mkdir(target)

def ensure_file(filename:str):
    target = filename.split(os.path.sep)
    if len(target)>1:
        for index,dirname in enumerate(target[:-1]):
            d = os.path.sep.join(target[:index+1])
            if not os.path.exists(d):
                os.mkdir(d)
    if not os.path.exists(filename):
        f = open(filename,'w',encoding='utf-8')
        f.close()
