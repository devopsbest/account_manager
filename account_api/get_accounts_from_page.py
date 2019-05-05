import pandas as pd
import requests


from .globals import username,password,CONFLUENCE_LOGIN_URL,CONFLUENCE_ACCOUNT_TRACKING_URL

def get_account_from_conflunce():

    s = requests.session()

    s.post(CONFLUENCE_LOGIN_URL, data={"os_username": username, "os_password": password}, verify=False)

    result = s.get(CONFLUENCE_ACCOUNT_TRACKING_URL, verify=False).content

    table = pd.read_html(result)
    #print(table[0])
    result = table[0]
    # android_device = table[0]

    #print(result.columns)


    result1=result.drop(0)
    print(result1.iloc[:,3])
    return (result1.iloc[:,3])