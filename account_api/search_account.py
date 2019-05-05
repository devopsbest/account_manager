import pandas as pd
import os
def query_account(username):
    current_dir = os.path.abspath(os.curdir)
    tables = pd.DataFrame.from_csv(os.path.join(current_dir,"testaccount.csv"))
    # tables.columns = tables.columns.str.strip("\n")
    #
    # print(tables)
    # print(tables.columns)
    row_num = tables[tables['username'].isin([username])]

    result = row_num.values
    return result[0][1]

# if __name__ == "__main__":
#     aa = query_account('stest1447')
#     print(aa)