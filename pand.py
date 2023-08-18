import pandas as pd

Sample_data ={'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}

data=pd.DataFrame(Sample_data,index="A B C B D".split())

print(data)