import math,re,json
import os.path
import time

from learnEng.utils import web,log,dir

def get_total_pages(url:str):
    text = web.get_text(url)
    if text == '':
        return -1
    num,per = map(int,re.search('共(\d+)条记录 每页显示(\d+)条',text).groups())
    return math.ceil(num/per)

def download_phrases(level:int):
    url = f'http://phrase.qsbdc.com/wl.php?level={level}&&tag=all&&page_id=1'
    total_pages = get_total_pages(url)
    if total_pages <= 0:
        return
    res = []
    for page in range(1,total_pages+1):
        url = f'http://phrase.qsbdc.com/wl.php?level={level}&&tag=all&&page_id={page}'
        soup = web.get_soup(url)
        if soup is None:
            log.log(url+' soup is None')
            continue
        table = soup.select('body > div:nth-child(6) > div.index_r.f_r.r_bian > table')[0]
        for item in table.children:
            if item.name is None or len(item.contents) < 6: continue
            if item.contents[1].string.startswith('N'): continue

            ans = {'phrase': item.contents[5].contents[0].contents[0].string,
                   'explanation_ch': item.contents[11].contents[0].contents[0].string,
                   'examples': item.contents[13].contents[0].attrs['title'].split('||||')[1:],
                   'level':level,
                   'state':0}
            res.append(ans)
        log.log(url+f' add {len(res)} item for level {level}')
    return res

def save_res(ans:list,level:int):
    filename = os.path.join('phrase',f'level_{level}.txt')
    dir.ensure_file(filename)
    with open(filename,'w',encoding='utf-8') as f:
        for item in ans:
            res = json.dumps(item, ensure_ascii=False)
            print(res,file=f)
if __name__ == '__main__':
    for i in range(1,11):
        res = download_phrases(i)
        save_res(res,i)