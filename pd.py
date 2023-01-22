import pandas as pd

file="board.xlsx"
idxn=[1,2,3,4,5,6,7,8]
idxl=["A","B","C","D","E","F","G","H"]
df=pd.read_excel(file,index_col="NL")
for n in idxn:
    for l in idxl:
        if df.loc[n,l] !="_._":
            df.loc[n,l]=df.loc[n,l][0:2]
print(df)
