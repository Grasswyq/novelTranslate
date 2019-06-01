import requests
import random
import re
import hashlib
import urllib
import json
from bs4 import BeautifulSoup
id=45
while 1:
    fp=open(str(id)+'.txt','w',encoding='utf-8')
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
    t=requests.get('https://ncode.syosetu.com/n5742ca/'+str(id)+'/',headers=headers)
    soup = BeautifulSoup(t.text, "html.parser")
    pt=soup.find_all('p')
    res=''
    fr='jp'
    to='zh'
    appid='20190602000304129'
    key='He_K8Coi9d0RUFysPaRt'
    for pi in pt:
       t=re.sub('\\<.*?\\>','',str(pi))
       if t!='':
            salt=random.randint(1000000000,9999999999)
            src=appid+t+str(salt)+key
            m1=hashlib.md5()
            m1.update(src.encode('utf-8'))
            at=requests.get('http://api.fanyi.baidu.com/api/trans/vip/translate?q='+urllib.parse.quote(t)+'&from='+fr+'&to='+to+'&appid='+appid+'&salt='+str(salt)+'&sign='+m1.hexdigest())
            atdict=json.loads(at.text)
            atdata=atdict['trans_result']
            atdata=atdata[0]
            dst=atdata['dst']+'\n'
            #dst=dst.encode('utf-8')
            print(str(id)+':   '+dst)
            fp.write(dst)
            fp.flush()
    fp.close()
    id=id+1
    if(id==55):
        break
    
    




