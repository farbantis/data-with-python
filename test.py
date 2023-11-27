import pandas as pd
import numpy as np
# Creating a sample Series with some duplicate and missing values
data = {
    'month': ['jan', 'feb', 'march', 'april', 'may', 'june', 'july'],
    'sales': [1, 2, 3, 'NA', 1, 1, 3]
}
df = pd.DataFrame(data)

result = df['sales'].value_counts()
print(result)
