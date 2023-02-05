import pandas as pd
from numpy import array
from decimal import Decimal, ROUND_HALF_UP

a = array([1.1020, 2.1020, 3.1020, 4.1020])

# Criar um DataFrame com dados fictícios
df = pd.DataFrame({'col1': [1.2310, 2.34, 3.45]})

print(df)
print(df['col1'].dtype)

# df['col1'] = df['col1'].round(2).astype(str)
# df['col1'] = df['col1'].astype(str)
# df['col1'] = df['col1'].apply(lambda x: '{:.2f}'.format(x))
df['col1'] = df['col1'].apply(lambda x: Decimal(str(x)).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP))

print(df)
print(df['col1'].dtype)