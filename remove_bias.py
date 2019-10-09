"""
1. Read file.
2. For daytime values only, subtract twice the total bias.
3. Write out new file.
"""


import pandas as pd

raw_fx = pd.read_csv('gfs_oasis_may_sept.csv', comment='#',
                     parse_dates=True, index_col='timestamp')

total_bias = -27.676

nighttime_mask = raw_fx < 50

# estimate subtract twice the total bias because bias at night is 0
bias_subtracted = raw_fx - 2*total_bias

corrected_fx = raw_fx.where(nighttime_mask, other=bias_subtracted)

corrected_fx.to_csv('gfs_oasis_may_sept_bias_corrected.csv')
