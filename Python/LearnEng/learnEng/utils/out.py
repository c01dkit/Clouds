
def print_phrase(dic:dict):
    try:
        print(dic['phrase'],f' 等级{dic["level"]}')
        print(dic['explanation_ch'])
        for sen in dic['examples']:
            print(sen)
        print()
    except:
        return

def print_translate(dic:dict):
    try:
        print(dic['query'])
        print(dic['pronounce'],f' 等级{dic["level"]}')
        print(dic['explanation_ch'])
        print(dic['examples'])
        print()
    except:
        return