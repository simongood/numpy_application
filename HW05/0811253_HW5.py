import pandas as pd

df1 = pd.read_excel("employee.xlsx")                 # sheet1
#print(df1)
df2 = pd.read_excel("employee.xlsx", sheet_name=1)   # sheet2
#print(df2)

D = df1.merge(df2, on=['ID1', 'ID2'], how='outer').fillna(0)
print('inner merge:\n', D)

G = D.groupby(['ID1'])
print(G['salary'].mean())
# items = G.size().items()
# for key, n in items:
#    print('key:', key, ', n:', n)
#    g = G.get_group(key)
#    #mean = np.mean(g['salary'])
#    print(g)

