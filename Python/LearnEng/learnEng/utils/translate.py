from learnEng.utils import web
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

def handle_parse(soup)->dict:
    ans = {}

    try:
        table = soup.select('body > div:nth-child(6) > div.index_r.f_r.r_bian > table')[0]
        if str(table).find('单词查询结果为空！') != -1:
            return ans
    except:
        return ans
    res = soup.select('#nobian > div')[0]
    for item in res.children:
        if item.name == 'div':
            if 'style' in item.attrs.keys() and item.attrs['style'].startswith('border'):
                raw = str(item)
                start = raw.find('[')
                end = raw.find(']')+1
                ans['pronounce'] = raw[start:end]
                continue
            if item.attrs['class'] == ['dict_p']:
                raw = str(item)
                if '词组级别' in raw:
                    ans['level'] = item.contents[3].string
                    continue
                if '基本释义' in raw:
                    start = raw.find('</h3>')+5
                    end = raw.find('</div>')
                    ans['explanation_ch'] = raw[start:end]\
                        .replace('\r\n','\n')\
                        .replace('<br/>','\n')\
                        .replace('&amp;','&')\
                        .strip('\n')
                    continue
                if '英英释义' in raw:
                    ans['explanation_en'] = item.contents[3].string.replace('\r\n','\n').replace('<br/>','\n')
                    continue
                if '参考例句' in raw:
                    start = raw.find('</h3>')+5
                    end = raw.find('</div>')
                    ans['examples'] = raw[start:end]\
                        .replace('\r\n','\n')\
                        .replace('<br/>','\n')\
                        .replace('&amp;','&')\
                        .strip('\n')
                    continue

    return ans


def search(sth:str):

    query = sth.replace(' ','+').replace('[','').replace(']','')
    url = f'http://dict.qsbdc.com/{query}'
    soup = web.get_soup(url)
    if soup is not None:
        res = handle_parse(soup)
        res['query'] = sth
        return res
    else:
        return None

def translate(item:str):
    return search(item)