# -*- coding:utf8 -*-
import requests
import re


headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

# def transfer_gb2312(name):
#     name=str(name.encode('gb2312')).replace('\\x','%')
#     return name[2:-1]

def get_downloadlink(url):
    content=requests.get(url,headers=headers).text
    tag=re.compile('<a href="(magnet.*?)".*?>(.*?)</a></li>')
    link=re.findall(tag,content)
    return link

def notonepage(text):
    tag=re.compile('下一页')
    judge=re.search(tag,text)
    return judge!=None


# c=file_name.encode('gb2312')
# c=transfer_gb2312(file_name)

#print('http://s.ygdy8.com/plus/so1.php?typeid=1&keyword=%s'%c)
#url=requests.get('http://s.ygdy8.com/plus/so1.php?typeid=1&keyword=%D6%A9%D6%EB%CF%C0',headers=headers)
#url.encoding=url.apparent_encoding
def getmovie_link(name):
    base_url='https://www.bttiantangok.com'
    url='https://www.bttiantangok.com/e/search/new.php'
    data={'keyboard':name}
    search_url=[]
    i=0
    search_url+=[requests.post(url,data).text]
    movie_url=[]
    tag = re.compile('<a href="(.*?)" class="zoom" rel="bookmark" target="_blank" title="(.*?)">')
    tag_next=re.compile('<a href="([\S]*?)">下一页')
    while notonepage(search_url[i]):
        movie_url+=re.findall(tag,search_url[i])
        tmp=re.findall(tag_next,search_url[i])
        search_url.append(requests.get((base_url+tmp[0]).replace('amp;',''),headers=headers).text)
        i+=1
    movie_url+=re.findall(tag,search_url[i])
    return [base_url+i[0] for i in movie_url],[i[1] for i in movie_url]
    # res={}
    # for i in movie_url:
    #     content=get_downloadlink(base_url+i)
    #     for j,k in content:
    #         res[k]=j
    # return res

if __name__=='__main__':
    movie_name='复仇者'
    link,title=getmovie_link(movie_name)
    count=0
    for i in title:
        print('[%s]'%count,i)
        print('\n')
        count+=1
    print('which one you need:')
    num=int(input())
    downloadlink=get_downloadlink(link[num])



# z=base_url+movie_url[0][0]
# a=get_downloadlink(z)