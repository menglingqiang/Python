# coding=UTF-8
import codecs
import json
from  bs4 import BeautifulSoup
import bs4
from pip._vendor.appdirs import unicode
import requests
import urllib.request

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
#     id = input("请输入您想要获取的云音乐列表 id:\n")
#     tplt = "\t{:80}\t{:80}\t{:80}"
#     print(tplt.format("歌曲", "歌手", "专辑"))
#     id=""
#     url = 'http://music.163.com/playlist?id='+id
#     html = downloadHtml(url)
#     soup = BeautifulSoup(html,'html.parser')
#     summary_node = soup.find('textarea') #得到所有歌曲的json串
#     musicJson = summary_node.get_text()
#     data = json.loads(musicJson)
#     count = len(data)
#     for i in range(count):
#         print(tplt.format(data[i]['name'],data[i]['artists'][0]['name'],data[i]['album']['name']))
    f = urllib.request.urlopen('http://m10.music.126.net/20170604134656/4d5a8e553045cad820afcc665b0c92f7/ymusic/9a1b/954a/4b1a/5e7c012e7a6e44690794486d1be90531.mp3')    
    data = f.read()    
    with open('C:\\Users\\mlq\\Desktop\\downmusic\\download.mp3', 'wb') as code:    
        code.write(data)  
    #data = json.loads(html)
    #print(data)
    #file_object = open('test.txt','wb')
    #with open('test.txt', 'w',encoding="utf-8") as f:
    #    f.write(tplt.format("歌曲", "歌手", "专辑")+'\n')
    #    for i in range(count):
        #    str = unicode(tplt.format(data[i]['name'],data[i]['artists'][0]['name'],data[i]['album']['name']),"utf-8")
    #        f.write(tplt.format(data[i]['name'],data[i]['artists'][0]['name'],data[i]['album']['name'])+'\n')
    #    f.close( )
    #    all_the_text = file_object.read( ).decode('utf-8')
    #    print(all_the_text)
    #finally:
    #     file_object.close( )
    #with open('test.txt', 'rb') as f:
    #    data = json.load(f)
main()    
    
#+"歌手:"
#       +data[i]['artists']['name']+"专辑:"+data[i]['album']['name']   
    
    
    
    
        