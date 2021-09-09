# python-excel setup
import itertools
import pandas as pd
df = pd.DataFrame()

# list of possible roles
a = ['V', 'F', 'P']

# function to turn a list of ['V', 'F', 'P] into a list of 'VFP'
def tup_to_s(list_of_tups):
    output = []
    for tup in list_of_tups:
        output.append(''.join(tup))
    return output

# Possible arrangements for "repeat" speakers
two = tup_to_s([p for p in itertools.product(a, repeat=2)])
three = tup_to_s([p for p in itertools.product(a, repeat=3)])
four = tup_to_s([p for p in itertools.product(a, repeat=4)])
five = tup_to_s([p for p in itertools.product(a, repeat=5)])
six = tup_to_s([p for p in itertools.product(a, repeat=6)])

# creating the columns
df['six'] = pd.Series(six) # need to add the largest first for the dataframe to be large enough
df['five'] = pd.Series(five)
df['four'] = pd.Series(four)
df['three'] = pd.Series(three)
df['two'] = pd.Series(two)

# Converting to excel
df.to_excel('forbea.xlsx', index = False)

# To run