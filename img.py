import os
import random
import webbrowser
import time
while 1==1:
    find=input('通过文件类型=y;通过文件type=n')

    if find=='y':
        wjlx=input('find:')

        m='for /r img %i in (*.'+wjlx+') do @echo %i'
    if find=='n':
        typ=input('find:')

        m='for /r img %i in (*'+typ+'*) do @echo %i'
        

    if find=='all':

        m='for /r img %i in (*) do @echo %i'
    
    lii=open('index.html','w')
    lii.truncate()
    file1 = open("man.html","r")

    file2 = open("index.html","w")

    s = file1.read()

    w = file2.write(s)

    file1.close()

    file2.close()

    c=os.popen(m)
    f=c.read()
    str2=''
    print(f)

    date=f.split('\n')
    del date[-1]
    print(date)


    winner = random.choice(date)


    file = open('index.html','r')
    content = file.read()
    post = content.find('url=')
    if post != -1:
        content = content[:post+len('url=')]+winner+content[post+len('url='):]
        file = open('index.html','w')
        file.write(content)
    file.close()

    webbrowser.open('index.html')
    time.sleep(2)



