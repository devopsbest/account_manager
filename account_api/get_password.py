from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from account_api.get_accounts_from_page import get_account_from_conflunce

option = webdriver.ChromeOptions()

option.add_argument('disable-infobars')
# option.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=option)
Max_Time_Out = 30
Time_Out = 10
Mini_Time_Out = 3
# account_name = "stest132705"


sql = """
select Password from ET_Main.dbo.Members where UserName= '{}'
"""


class live_password():
    def __init__(self):
        self.user_name_btn = "i0116"
        self.next_btn = "idSIButton9"
        self.user_name = "qa.testauto@ef.com"
        self.user_pwd_btn = "i0118"
        self.user_password = "test@456"
        # self.member_id = "11446478"
        # self.target_stage = 3
        self.check_url = "https://deepblue2.englishtown.com/dbquery/dbquery.aspx"
        self.get_sql_text_id = "TxtQuery"
        self.click_query_bottun_id = "BtnExecute"
        self.result_path = '//*[@id="Form1"]/table[4]/tbody/tr[2]/td'

    def open_url(self):
        url = self.check_url
        driver.set_page_load_timeout(Max_Time_Out)
        try:
            driver.get(url)
        except TimeoutError:
            print("cannot open the page for {} seconds".format(Max_Time_Out))
            driver.execute_script('window.stop()')

    def find_element(self, obj):
        WebDriverWait(driver, Time_Out).until(EC.visibility_of_element_located((By.ID, obj)))
        element = WebDriverWait(driver, Time_Out).until(lambda x: driver.find_element(By.ID, obj))
        return element

    def type(self, obj, value):
        self.find_element(obj).clear()
        self.find_element(obj).send_keys(value)

    def clickat(self, obj):
        WebDriverWait(driver, Time_Out).until(EC.element_to_be_clickable((By.ID, obj)))
        self.find_element(obj).click()

    def select_at(self, father, type, child):

        s = driver.find_element_by_id(father)

        if type == "value":
            Select(s).select_by_value(child)
        elif type == "index":
            Select(s).select_by_value(child)
        else:
            print("select by text")
            Select(s).select_by_visible_text(child)

    def get_cookies(self):

        cookies = driver.get_cookies()

        home_cookies = ""
        for cookie in cookies:
            print(cookie)

            if cookie['name'] == ".AspNet.Cookies" and cookie['domain'] in driver.current_url:
                print("find")
                print(cookie['name'])
                print(cookie['value'])
                home_cookies = cookie['name'] + "=" + cookie['value']
                break

        return home_cookies

    def login(self):
        self.open_url()

        self.type(self.user_name_btn, self.user_name)

        self.clickat(self.next_btn)

        self.type(self.user_pwd_btn, self.user_password)

        self.clickat(self.next_btn)

        self.clickat(self.next_btn)

    def check_login(self):
        if self.get_cookies() != "":
            print("no need to login")
        else:
            self.login()

    def get_password(self, account):

        self.check_login()

        self.open_url()
        driver.implicitly_wait(2)
        self.type(self.get_sql_text_id, sql.format(account))
        self.clickat(self.click_query_bottun_id)
        driver.implicitly_wait(1)
        # print(driver.find_element_by_xpath(self.result_path).text)
        return (driver.find_element_by_xpath(self.result_path).text).strip()


password = live_password()

passwd = []

accounts = get_account_from_conflunce()

print(accounts)

for account in accounts:
    result = password.get_password(account)
    passwd.append(result)

driver.quit()

import pandas as pd

data = {
    "username": accounts,
    "password": passwd
}

user_info = pd.DataFrame(data)
user_info.to_csv("testaccount.csv")

