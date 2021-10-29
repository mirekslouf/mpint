# Gradual appending of new rows to pd.DataFrame
# ADDITIONALLY we require that index of the new row = name of datafile

# This test was created according to:
# https://stackoverflow.com/q/16824607

import pandas as pd

# Initial empty dataframe
df = pd.DataFrame()

# Data for model row #1
datafile = 'mirek1.txt'
indexes = {'OI': 5, 'VI': 6}
# Prepare data for appending to dataframe
# (convert dict to pd.Series + add name of series
# (reason: series name becomes index of the new row in dataframe
new_row = pd.Series(indexes)
new_row.name = datafile
# Append row #1 to dataframe
df = df.append(new_row)

# Data for model row #2
datafile = 'mirek2.txt'
indexes = {'OI': 50, 'VI': 60}
# Prepare data for appending like above...
new_row = pd.Series(indexes)
new_row.name = datafile
# Append row #2 to dataframe
df = df.append(new_row)

# Print final dataframe
print(df)