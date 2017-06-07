# coding=UTF-8
import codecs
import json
import re
import urllib.request

from  bs4 import BeautifulSoup
import bs4
from pip._vendor.appdirs import unicode
import requests


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
def check_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False
def main():
    id = input("请输入您想要获取的云音乐列表 id:\n")
    tplt = "\t{:80}\t{:80}\t{:80}"
#     print(tplt.format("歌曲", "歌手", "专辑"))
    url = 'http://music.163.com/playlist?id='+id
    html = downloadHtml(url)
    soup = BeautifulSoup(html,'html.parser')
    summary_node = soup.find('textarea') #得到所有歌曲的json串
    musicJson = summary_node.get_text()
    data = json.loads(musicJson)
    count = len(data)
#     for i in range(count):
#         print(tplt.format(data[i]['name'],data[i]['artists'][0]['name'],data[i]['album']['name']))
#     f = urllib.request.urlopen('http://m10.music.126.net/20170604134656/4d5a8e553045cad820afcc665b0c92f7/ymusic/9a1b/954a/4b1a/5e7c012e7a6e44690794486d1be90531.mp3')    
#     data = f.read()    
#     with open('C:\\Users\\mlq\\Desktop\\downmusic\\download.mp3', 'wb') as code:    
#         code.write(data)  
#     data = json.loads(html)
#     print(data)
    cMusic =0  #中文歌曲数量
    eMusic =0  #英文歌曲数量
    oMusic =0  #其他国家歌曲数量
    
    ePattern = re.compile(r'[a-zA-Z\.()0-9]+')  #英文正则,全是英文，下滑线，括号，空格就是英文  
#    file_object = open('test.txt','wb')
    with open('test.txt', 'w',encoding="utf-8") as f:
        f.write(tplt.format("歌曲", "歌手", "专辑")+'\n')
        for i in range(count):
            #cMatch = cPattern.match(data[i]['name'])
            eMatch = ePattern.match(data[i]['name'])
            
            if(check_contain_chinese(data[i]['name'])):    
                cMusic +=1
            elif(eMatch):
                print(data[i]['name'])
                eMusic +=1
            else:
                oMusic +=1   
            #str = unicode(tplt.format(data[i]['name'],data[i]['artists'][0]['name'],data[i]['album']['name']),"utf-8")
            f.write(tplt.format(data[i]['name'],data[i]['artists'][0]['name'],data[i]['album']['name'])+'\n')
        f.write('中文歌曲：'+str(cMusic)+'\n'+'英文歌曲：'+str(eMusic)+'\n'+'其他国家歌曲：'+str(oMusic))
        f.close()
#        all_the_text = file_object.read( ).decode('utf-8')
#        print(all_the_text)
#     finally:
#        file_object.close()
    #每次读取一行判断是否中文，英文，其他语言并进行总结
    
main()    
      
    
    
    
    
        