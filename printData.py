import pandas as pd
import json

with open('3.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data['employee'])
print(df)