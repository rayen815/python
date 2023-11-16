from numpy import array
from random import randint
from pickle import dump,load

#function saisir
def saisir(ch):
    n=int(input("Donner "+ch+": "))
    while not(2<=n<=20):
        n=int(input("Donner "+ch+": "))
    return n

#function remplirm
def remplirm(l,c,m):
    for i in range(l):
        for j in range(c):
            m[i,j]=chr(randint(ord("A"),ord("Z")))

def exist(ch,m,i,c):
    j=0
    while j<=c-1 and ch!="":
        if ch[0]==m[i,j]:
            ch=ch[1:len(ch)]
        j+=1
    return ch==""
               
#function remplirf
def remplirf(f,f1,l):
    ch=f.readline()
    while ch!="":
        ch=ch[:len(ch)-1]
        for i in range(l):
            if exist(ch,m,i,c):
                e=dict()
                e["mot"]=ch
                e["ligne"]=i
                print(e)
                dump(e,f1)
        ch=f.readline()
                
#pp
e=dict(mot=str(),ligne=int())
m=array([[str()]*20]*20)
l=saisir("ligne")
c=saisir("colonnes")
remplirm(l,c,m)
f=open("mots.txt","w")
f.write("BAC\nALGO\n")
f=open("mots.txt","r")
f1=open("res.dat","w")
print(m)
remplirf(f,f1,l)