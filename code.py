import pandas as pd
df=pd.read_csv("calculated.csv")
mass=df["mass"].tolist()
radius=df["radius"].tolist()
gravity=df["gravity"].tolist()
newGravity=[]
for i in gravity:
    if(i>=50 and i<=100):
        newGravity.append(i)
newDf=pd.DataFrame({"Gravity":newGravity})
newDf.to_csv("newCsv.csv")
