#function verif
def verif(ch):
    if ch[-1]!=".":
        return False
    else:
        i=0
        while i<=len(ch)-2 and "A"<=ch[i].upper()<="Z":
            i+=1
        return i>len(ch)-2    

#function saisir
def saisir():
    ch=input("Donner ch: ")
    while len(ch)<3 and not(verif(ch)):
        ch=input("Donner ch: ")
    return ch
#function freq
def freq(c,ch):
    nb=0
    for i in range(ch.find(c),len(ch)-1):
        if ch[i]==c:
            nb+=1
    return nb        
#function remplir
def remplir(ch,f):
    for i in range(ord("A"),ord("Z")):
        c=chr(i)
        if ch.upper().find(c)!=-1:
            f=freq(c ,ch.upper())
            ch1="le frequency de "+c+" est "+str(f)
            f.write(ch1+"\n")
    f.close()        
#pp
ch=saisir()
f=open("freq.txt","w")
remplir(ch,f)