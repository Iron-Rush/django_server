# CramTaobaoPrice.py
import requests
from bs4 import BeautifulSoup
import re
# 获取url网页内容
# 由于淘宝设置了登陆拦截，因此匿名搜索返回的为登陆界面，无法解析到搜索结果
def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, timeout=30, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.encoding)
        return r.text
    except:
        print('页面解析出错')
        return ''

def formatHTML(html):
    soup = BeautifulSoup(html, 'html.parser')
    allDIv = soup.find_all('div', attrs={"class" : 'w-full md:w-1/4 flex flex-col py-6 md:p-6'})
    for div in allDIv:
        print(div.find('img').get('src'))
        print(div.find('lottie-listings').get('src'))
        print(div.find('h3').string.strip())
    print(len(allDIv))
    return soup.prettify()

# 解析获得的页面
# 页面中为键值对形式给出，根据键找到值
# "raw_title":"日本书包"
# "view_price" "127.00" "raw_title" "书包***"
def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print('')


# 输出商品信息
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count, g[0], g[1]))

def writeHTML(path, txt):
    f = open(path, 'w+', encoding='utf-8')
    f.write(txt)
    f.close()
def readHTML(path):
    f = open(path, 'r', encoding='utf-8')
    txt = f.read()
    f.close()
    return txt

def main():
    type = ['featured', 'recent', 'popular']
    depth = 5

    # goods = '书包'
    # depth = 2
    # start_url = 'https://s.taobao.com/search?q=' + goods
    # infoList = []
    # for i in range(depth):
    #     try:
    #         url = start_url + '&s=' + str(44*i)
    #         html = getHTMLText(url)
    #         writeHTML("Taobao.html",html)
    #         parsePage(infoList, html)
    #     except:
    #         print('error')
    #         continue
    # printGoodsList(infoList)

    url = 'https://lottiefiles.com/featured?page=1'
    # html = getHTMLText(url)
    html = readHTML('lottie.html')
    html = formatHTML(html)
    # writeHTML('lottie.html', html)
main()
