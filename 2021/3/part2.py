import pandas as pd

with open('input.txt') as file:
    data = [val.strip('\n') for val in file]

expanded = [[i for i in val] for val in data]

df = pd.DataFrame(expanded)

o = df.copy()
c = df.copy()

for col in df.columns:
    if len(o) > 1:
        filter = int(o[col].astype(int).sum() // (len(o) / 2))
        o = o.loc[(o[col] == str(filter)), ].copy()
    if len(c) > 1:
        filter = int(-((c[col].astype(int).sum() // (len(c) / 2)) - 1))
        c = c.loc[(c[col] == str(filter)), ].copy()

o_rating = int(''.join(o.iloc[0]), 2)
c_rating = int(''.join(c.iloc[0]), 2)

final = o_rating * c_rating

print(final)
