import pandas as pd

file_to_read = "/Users/sgourav/Library/CloudStorage/OneDrive-VMware,Inc/myCodes/vdk/datajobs/horizon-cloud-customer-grouping/customer_grouping.csv"
def run():
    df = pd.read_csv(file_to_read)

    for rows, columns in df.iterrows():
        if columns['customer_group'] == '0':
            columns['customer_group'] = columns['customer_name']
    # df.drop(['customer_name', 'customer_type'], axis=1, inplace=True)
    df = df.groupby('customer_id').apply(lambda x: x.dropna(subset=['ea_account']) if x['ea_account'].notnull().any() else x)
    df = df.reset_index(drop=True)
    lst = df[['customer_group', 'customer_id', 'ea_account']].values.tolist()
    print(lst[0])
    print(lst[-1])
run()