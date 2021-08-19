
import random,os,json
from learnEng.utils import out,translate
def get_phrases(level:int=-1):
    dirname = os.path.join('data','phrase')
    li = []
    if 0<level<11:
        filename = os.path.join(dirname,f'level_{level}.txt')
    else:
        filename = os.path.join(dirname,f'level_{random.randint(1,10)}.txt')
    if not os.path.exists(filename):
        return li
    with open(filename,'r',encoding='utf-8') as f:
        for line in f.readlines():
            li.append(json.loads(line))
    return li

def learn_phrase():
    hint = """输入数字以设定词组等级:[1,10]之间的整数 
-1表示随机 
0表示退出
回车表示和上一次输出等级相同（默认随机）"""
    print(hint)
    old = -1
    while True:
        try:
            choice = int(input())
            old = choice
            if choice == 0:
                break
            else:
                out.print_phrase(random.choice(get_phrases(choice)))
        except:
            out.print_phrase(random.choice(get_phrases(old)))

def learn_eng():
    while True:
        try:
            item = input()
            out.print_translate(translate.translate(item))
        except:
            pass

if __name__ == '__main__':
    # learn_phrase()
    learn_eng()