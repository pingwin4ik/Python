
def encrypt():
    a=raw_input("word:")
    number=input("shift:")
    b=list(a)
    str(b)
    c=[ord(x)for x in(b)]
    d=[]
    for i in c:
        d.append(i+number)
    e=[chr(i) for i in (d)]
    e="".join(e)
    print "Caesar  code is:",e,

run=encrypt()


