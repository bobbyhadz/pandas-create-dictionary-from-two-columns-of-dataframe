# Pandas: Create a Dictionary from two DataFrame Columns

import pandas as pd

df = pd.DataFrame({
    'digit': [1, 2, 3],
    'day_name': ['Monday', 'Tuesday', 'Wednesday']
})

print(df)

print('-' * 50)

a_dict = pd.Series(
    df['day_name'].values,
    index=df['digit']
).to_dict()

print(a_dict)