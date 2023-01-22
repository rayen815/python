import pandas as pd
import numpy as np

class game:
    def __init__(self,moves):
        self.moves=moves

    def splt(self,moves):
        numove=0
        for i in range(len(moves)):
            if moves[i]==".":
                numove+=1

        listm={i:None for i in range(1,numove+1)}

        for i in range(1,numove+1):
            if i<10:
                listm[i]=moves[moves.find(str(i)+".")+2:moves.find(str(i+1)+".")]
            elif 10<=i<=99:
                listm[i]=moves[moves.find(str(i)+".")+3:moves.find(str(i+1)+".")]
            elif 99<i<=999:
                listm[i]=moves[moves.find(str(i)+".")+4:moves.find(str(i+1)+".")]

        for i in range(1,numove+1):
            listm[i]=listm[i].split()
            if len(listm[i])>2:
                if "$" in listm[i][1]:
                    listm[i][0]=listm[i][0],listm[i][1]
                    listm[i].remove(listm[i][1])
                elif "$" in listm[i][2]:
                    listm[i][1]=listm[i][1],listm[i][2]
                    listm[i].remove(listm[i][2])
            if len(listm[i])==1:
                listm[i].append("dead")
            if (type(listm[i][0]) != tuple )and(type(listm[i][1]) != tuple ):
                listm[i][0]=listm[i][0],None
                listm[i][1]=listm[i][1],None
            elif (type(listm[i][0]) != tuple )and(type(listm[i][1]) == tuple ):
                listm[i][0]=listm[i][0],None
            elif (type(listm[i][0]) == tuple )and(type(listm[i][1]) != tuple ):
                listm[i][1]=listm[i][1],None

        return listm
    
    def show(self,moves):
        for i in range(1,len(moves)+1):
            print(moves[i])
            print()

    def board(self,idxn=[1,2,3,4,5,6,7,8],idxl=["A","B","C","D","E","F","G","H"]):
        global pos
        i=0
        fileb="board.xlsx"
        board=pd.read_excel(fileb,index_col="NL")
        for n in idxn:
            for l in idxl:
                pos.append(board.loc[n,l][3:])
                i+=1
                board.loc[n,l]=board.loc[n,l][0:2]
        pos=np.array(pos)
        print(board)
    
    def coccect_moves(self,moves):
        for i in range(1,len(moves)+1):
            for j in range(2):
                if len(moves[i][j][0])==2:
                    if j==0:
                        listt=list(moves[i][j])[0]="wp"+moves[i][j][0],None
                    else:
                        listt=list(moves[i][j])[0]="bp"+moves[i][j][0],None
                    moves[i][j]=listt
        return moves




file=open("moves.txt","r")
moves=""
pos=[]

for line in file:
    moves=moves+line
moves=moves[moves.find("1. "):moves.find("#")+1]
game1=game(moves)
game1.moves=game1.splt(game1.moves)
game1.moves=game1.coccect_moves(game1.moves)
game1.show(game1.moves)
game1.board()
pos=pos.reshape(8,8)
pos=np.flip(pos,axis=0)
print("--------------------------------------------------------------------------")
print(pos)

