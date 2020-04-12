import requests
import pymysql
from bs4 import BeautifulSoup
import re
class spyder():
    def __init__(self):
        # self.conn = pymysql.connect(host="47.107.67.23/localhost", port=3306, database='crawl', user='root', password='qq654321')
        self.conn = pymysql.connect(host="47.107.67.23", port=3306, database='lottie', user='root', password='caren6211430')
        self.jpgUrl = ''
        self.jsonUrl = ''
        self.auth = ''
        self.info_list = []

    # 获取url网页内容
    # 由于淘宝设置了登陆拦截，因此匿名搜索返回的为登陆界面，无法解析到搜索结果
    def getHTMLText(self,url):
        try:
            kv = {'user-agent': 'Mozilla/5.0'}
            r = requests.get(url, timeout=30, headers=kv)
            r.raise_for_status()
            r.encoding = 'utf-8'
            return r.text
        except:
            print('页面获取出错')
            return ''

    def formatHTML(self, html, page, type):
        id = page*16
        ls = []
        if type == 'recent':
            id += 30000
        elif type == 'popular':
            id += 15000
        try:
            soup = BeautifulSoup(html, 'html.parser')
            allDIv = soup.find_all('div', attrs={"class" : 'w-full md:w-1/4 flex flex-col py-6 md:p-6'})
            # f = open("parseHTML.html", 'a', encoding='utf-8')
            for div in allDIv:
                id += 1
                self.jpgUrl = div.find('img').get('src')
                self.jsonUrl = div.find('lottie-listings').get('src')
                self.auth = div.find('h3').string.strip()
                ls.append([id, type, self.jpgUrl, self.jsonUrl,self.auth])
            return ls
                # self.info_list.append([id, type, self.jpgUrl, self.jsonUrl,self.auth])
        except:
            print('页面解析出错')
            pass

if __name__ == "__main__":
    Spyder = spyder()
    # types = ['featured', 'recent', 'popular'] #50,600,18
    types = {'featured':50,'recent':600,'popular':18}
    sql = ''
    url = 'https://lottiefiles.com/featured?page=1'
    cs = Spyder.conn.cursor()
    try:
        for type in types:
            for i in range(types.get(type)):
                try:
                    url = 'https://lottiefiles.com/'+type+'?page='+str(i+1)
                    print(url)
                    html = Spyder.getHTMLText(url)
                    htmlUni = html.encode('utf-8','ignore')
                    html = htmlUni.decode("GBK", 'ignore')
                    temp_list = Spyder.formatHTML(html,i,type)
                    for temp in temp_list:
                        sql = "REPLACE INTO myapp_allinfo(lottieid, type, userimg, lottie, username) values({},'{}','{}','{}','{}')".format(temp[0],temp[1],temp[2],temp[3],temp[4])
                        cs.execute(sql)
                        Spyder.conn.commit()
                except Exception as e:
                    print('编码/写入出错')
                    pass

    except:
        print('数据写入出错')
        pass
    finally:
        cs.close()
        Spyder.conn.close()