#function saisir
def saisir(a,b):
    n=int(input("Donner n: "))
    while not(a<=n<=b):
        n=int(input("Donner n: "))
    return n

#function prime
def prime(n):
    i=2
    while i<=n//2 and n%i!=0:
        i+=1
    return i>n//2 and n>1
    
#function super
def super(n):
    while n!=0 and prime(n):
        n=n//10
    return n==0

#function remplir
def remplir(n,f):
    f.write("les numbers sont:"+"\n")
    for i in range(2,n+1):
        if super(i):
            f.write(str(i)+"\n")
    f.close()
   
#pp
n=saisir(20000,60000)
f=open("sup_prem.txt","w")
remplir(n,f)