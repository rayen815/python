import pandas as pd
import numpy as np

index=[("rayen",2014),("rayen",2022),
    ("ela",2014),("ela",2022),
    ("oussama",2014),("oussama",2022)
]

num=[11,12,
    10,15,
    14,10
]

good=["no","yes",
    "no","yes",
    "yes","no"
]

pets=[5,2,
    0,2,
    0,1
]

index=pd.MultiIndex.from_tuples(index)
r=pd.Series(num,index=index)
print(r)
df=pd.DataFrame({"num":r,"good":good,"pets":pets})
print(df)