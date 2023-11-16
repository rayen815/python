#function remplir1
def remplir1(f):
    rep="O"
    while rep.upper()=="O":
        code=input("donner code: ")
        while not("1000"<=code<="9999"):
            code=input("donner code: ")
    
        qu=int(input("donner quantite:"))
        while qu<=0:
            qu=int(input("donner quantite:"))
    
        pr=float(input("donner prix: "))
        while pr<=0:
            pr=float(input("donner prix: "))
    
        ch=code +" "+str(qu)+" "+str(pr)
        f.write(ch+"\n")
        
        rep=input("autre O/N: ")
        while not(rep.upper() in["N","O"]):
            rep=input("autre O/N: ")
    f.close()

#function remplir2
def remplir2(f,f1):
    ch=f.readline()
    while ch!="":
        ch=ch[:len(ch)-1]
        code=ch[:4]
        ch=ch[5:len(ch)]
        p=ch.find(" ")
        qu=int(ch[:p])
        pr=float(ch[p+1:])
        ch=code+" "+str(qu*pr)
            
        f1.write(ch+"\n")
        ch=f.readline()
    f.close()
    f1.close()

#pp
f=open("command.txt","w")
remplir1(f)
f=open("command.txt","r")
f1=open("facture.txt","w")
remplir2(f,f1)