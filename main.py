import pandas as pd

# create example dataframe
df = pd.DataFrame({
    'DATE': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04'],
    'SECTOR': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
    'PRODUCT_GROUP': ['X', 'X', 'Y', 'Y', 'X', 'X', 'Y', 'Y'],
    'BRAND': ['P', 'Q', 'P', 'Q', 'P', 'Q', 'P', 'Q'],
    'SALES_ONLINE': [10, 20, 30, 40, 50, 60, 70, 80],
    'SALES_OFFLINE': [100, 200, 300, 400, 500, 600, 700, 800],
    'SALES_TOTAL': [0, 100, 200, 300, 0, 400, 500, 600]
})

# define custom function to remove beginning rows with SALES_TOTAL=0
def remove_starting_zero_rows(group):
    if group.iloc[0]['SALES_TOTAL'] == 0:
        return group[group['SALES_TOTAL'] != 0]
    else:
        return group

# group dataframe by SECTOR, PRODUCT_GROUP, and BRAND and apply custom function
grouped = df.groupby(['SECTOR', 'PRODUCT_GROUP', 'BRAND']).apply(remove_starting_zero_rows)

# concatenate resulting groups back together
result = pd.concat(grouped)

print(result)