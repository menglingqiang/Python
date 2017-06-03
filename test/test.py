# coding=UTF-8
import requests
import json
from  bs4 import BeautifulSoup
import bs4
def downloadHtml(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url,headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "exception"
def parse(html,ulist):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbpdy').children:
        if(isinstance(tr, bs4.element.Tag)):
            tds = tr('td')
            ulist.append([tds[0].string])
def main():
    url = 'http://music.163.com/playlist?id=86379700'
    html = downloadHtml(url)
    soup = BeautifulSoup(html,'html.parser')
    summary_node = soup.find('textarea') #得到所有歌曲的json串
    musicJson = summary_node.get_text()
    data = json.loads(musicJson)
    count = len(data)
    for i in range(count):
        print(data[i]['name'])
    #data = json.loads(html)
    #print(data)
    #file_object = open('test.txt','rb')
    #try:
    #     all_the_text = file_object.read( ).decode('utf-8')
    #     print(all_the_text)
    #finally:
    #     file_object.close( )
    #with open('test.txt', 'rb') as f:
    #    data = json.load(f)
main()    
    
    
    
    
    
    
        