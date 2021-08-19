import datetime as d

with open('tips.txt','a',encoding='utf-8') as f:
    while True:
        s = input()
        if s in ['q','quit','exit']:
            break
        print(f'[{d.datetime.now()}]',s,file=f)