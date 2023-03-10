def hex_to_dec(hex):
    hex=str(hex)
    dec=0
    lh=len(hex)-1
    for i in range(len(hex)):
        if hex[i] in ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]:
            if hex[i] in ["A","B","C","D","E","F"]:
                dec+=(ord(hex[i])-55)*(16**lh)
            else:
                dec+=int(hex[i])*(16**lh)
        else:
            return "input errur"
        lh-=1
    return str(dec)

def oct_to_dec(oct):
    oct=str(oct)
    dec=0
    lh=len(oct)-1
    for i in range(len(oct)):
        if oct[i] in ["0","1","2","3","4","5","6","7"]:
            dec+=int(oct[i])*(8**lh)
        else:
            return "input errur"
        lh-=1
    return str(dec)

def bin_to_dec(bin):
    bin=str(bin)
    dec=0
    lh=len(bin)-1
    for i in range(len(bin)):
        if bin[i] in ["0","1"]:
            dec+=int(bin[i])*(2**lh)
        lh-=1
    return str(dec)

def dec_to_hex(dec):
    dec=str(dec)
    r=""
    while dec !="0":
        if int(dec)%16 in [0,1,2,3,4,5,6,7,8,9]:
            r+=str(int(dec)%16)
        elif int(dec)%16 in [10,11,12,13,14,15]:
            r+=chr((int(dec)%16)+55)
        dec=str(int(dec)//16)
    r=r[::-1]
    return r
 
def dec_to_oct(dec):
    dec=str(dec)
    r=""
    while dec !="0":
        if int(dec)%8 in [0,1,2,3,4,5,6,7]:
            r+=str(int(dec)%8)
        dec=str(int(dec)//8)
    r=r[::-1]
    return r

def dec_to_bin(dec):
    dec=str(dec)
    r=""
    while dec !="0":
        if int(dec)%2 in [0,1]:
            r+=str(int(dec)%2)
        dec=str(int(dec)//2)
    r=r[::-1]
    return r

def ishex(hex):
    hex=str(hex)
    t=True
    i=0
    while t and i<len(hex):
        if not(hex[i] in  ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]):
            t=False
        i+=1
    return t

def isdec(dec):
    dec=str(dec)
    t=True
    i=0
    while t and i<len(dec):
        if not(dec[i] in  ["0","1","2","3","4","5","6","7","8","9"]):
            t=False
        i+=1
    return t

def isoct(oct):
    oct=str(oct)
    t=True
    i=0
    while t and i<len(oct):
        if not(oct[i] in  ["0","1","2","3","4","5","6","7"]):
            t=False
        i+=1
    return t

def isbin(bin):
    bin=str(bin)
    t=True
    i=0
    while t and i<len(bin):
        if not(bin[i] in  ["0","1"]):
            t=False
        i+=1
    return t

def convert(num,typenum=10,totype=10):
    if typenum==10:
        if isdec(num):
            if totype==10:
                return num
            elif totype==2:
                return dec_to_bin(num)
            elif totype==8:
                return dec_to_oct(num)
            elif totype==16:
                return dec_to_hex(num)
            else:
                return "wrong input"
        else:
            return "not valide number"
    elif typenum==2:
        if isbin(num):
            if totype==10:
                return bin_to_dec(num)
            elif totype==2:
                return num
            elif totype==8:
                return dec_to_oct(bin_to_dec(num))
            elif totype==16:
                return dec_to_hex(bin_to_dec(num))
            else:
                return "wrong input"
        else:
            return "not valide number"
    elif typenum==8:
        if isoct(num):
            if totype==10:
                return oct_to_dec(num)
            elif totype==2:
                return dec_to_bin(oct_to_dec(num))
            elif totype==8:
                return num
            elif totype==16:
                return dec_to_hex(oct_to_dec(num))
            else:
                return "wrong input"
        else:
            return "not valide number"
    elif typenum==16:
        if ishex(num):
            if totype==10:
                return hex_to_dec(num)
            elif totype==2:
                return dec_to_bin(hex_to_dec(num))
            elif totype==8:
                return dec_to_oct(hex_to_dec(num))
            elif totype==16:
                return num
            else:
                return "wrong input"
        else:
            return "not valide number"
            
def add(num1,num2,type):
    if type==10:
        return num1+num2
    elif type ==2:
        dec1=bin_to_dec(num1)
        dec2=bin_to_dec(num2)
        return dec_to_bin(dec1+dec2)
    elif type ==8:
        dec1=oct_to_dec(num1)
        dec2=oct_to_dec(num2)
        return dec_to_oct(dec1+dec2)
    elif type ==16:
        dec1=hex_to_dec(num1)
        dec2=hex_to_dec(num2)
        return dec_to_hex(dec1+dec2)
    
def multi(num1,num2,type):
    if type==10:
        return num1*num2
    elif type ==2:
        dec1=bin_to_dec(num1)
        dec2=bin_to_dec(num2)
        return dec_to_bin(dec1*dec2)
    elif type ==8:
        dec1=oct_to_dec(num1)
        dec2=oct_to_dec(num2)
        return dec_to_oct(dec1*dec2)
    elif type ==16:
        dec1=bin_to_hex(num1)
        dec2=bin_to_hex(num2)
        return dec_to_hex(dec1*dec2)
        
def minus(num1,num2,type):
    if type==10:
        return num1-num2
    elif type ==2:
        dec1=bin_to_dec(num1)
        dec2=bin_to_dec(num2)
        return dec_to_bin(dec1-dec2)
    elif type ==8:
        dec1=oct_to_dec(num1)
        dec2=oct_to_dec(num2)
        return dec_to_oct(dec1-dec2)
    elif type ==16:
        dec1=hex_to_dec(num1)
        dec2=hex_to_dec(num2)
        return dec_to_hex(dec1-dec2)
        
def div(num1,num2,type):
    if type==10:
        return num1//num2
    elif type ==2:
        dec1=bin_to_dec(num1)
        dec2=bin_to_dec(num2)
        return dec_to_bin(dec1//dec2)
    elif type ==8:
        dec1=oct_to_dec(num1)
        dec2=oct_to_dec(num2)
        return dec_to_oct(dec1//dec2)
    elif type ==16:
        dec1=hex_to_dev(num1)
        dec2=hex_to_dec(num2)
        return dec_to_hex(dec1//dec2)

def pow(num1,num2,type):
    if type==10:
        return num1**num2
    elif type ==2:
        dec1=bin_to_dec(num1)
        dec2=bin_to_dec(num2)
        return dec_to_bin(dec1**dec2)
    elif type ==8:
        dec1=oct_to_dec(num1)
        dec2=oct_to_dec(num2)
        return dec_to_oct(dec1**dec2)
    elif type ==16:
        dec1=hex_to_dec(num1)
        dec2=hex_to_dec(num2)
        return dec_to_hex(dec1**dec2)