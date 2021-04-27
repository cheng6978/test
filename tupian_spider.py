import requests
import re
from spider import ipprencoding

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

def get_tupian(name,nums):
    res=[]
    pages=(int(nums)-1)//30+1
    #url='https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word='+name
    for page in range(pages):
        url='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word={}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={}&rn=30&gsm=1e&1585409958640='.format(name,name,page*30)
        html=requests.get(url,headers=headers)
        html.encoding=html.apparent_encoding
        tag=re.compile('"objURL":"(.*?)"')#thumbURL格式是标清
        img_url=re.findall(tag,html.text)
        ipprencoding.url_list=[]
        for objurl in img_url:
            ipprencoding.encoding(objurl)
        img_url=ipprencoding.url_list
        res+=img_url
    return (res)
