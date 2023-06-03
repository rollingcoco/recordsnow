import pysnowball as ball

with open('SH(or SZ).txt','r',encoding='utf-8') as f:
    all=f.read()
    print(all)
    b=all.split()
    c = []
    for x in b:
        ball.set_token('xxqat=bbcf3**********************;')  # taken of snowball
        aa = ball.quotec('SH(or SZ)' + x)
        qudata = aa['data']
        aimdic = qudata[0]
        c.append(aimdic)


with open('RESH(or RESZ).txt','w',encoding='utf-8') as g:
    for d in c:
        for xx, y in d.items():
            if xx == 'symbol':
                g.write(str(y) + '\n')
            if xx == 'current':
                g.write(str(y) + '\n')
            if xx == 'percent':
                g.write(str(y) + '\n')
            if xx == 'volume':
                g.write(str(y) + '\n')
            if xx == 'amount':
                g.write(str(y) + '\n' + '\n')
