import pysnowball as ball

with open('/SZ(or SH).txt','r',encoding='utf-8') as f:                    #create a folder to record data
    alldata=f.read()
    print(alldata)
    b=all.split()
    c = []
    for x in b:
        ball.set_token('xqat=bbcf3************************;')  # taken of snowball
        aa = ball.quotec('SZ(or SH)' + x)
        qudata = aa['data']
        aimdic = qudata[0]
        c.append(aimdic)


with open('RESZ(or RZSH).txt','w',encoding='utf-8') as g:                 #
    for d in c:                                                           #
        for xx, y in d.items():

            if xx == 'volume':
                g.write(str(y) + '\n')









