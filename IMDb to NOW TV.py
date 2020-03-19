import csv
import re
import time
from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 

print("Filtering your IMDb watchlist for NOW TV availability.")
print("-"*20)
print("https://github.com/xjxckk/IMDb-watchlist-filtered-for-NOW-TV-availability")

config = open("config.txt", "r+").read().splitlines()
email = config[1]
password = config[3]

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)

# Non-headless webdriver for debugging.
# driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("https://www.imdb.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.imdb.com%2Fregistration%2Fap-signin-handler%2Fimdb_us&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=imdb_us&openid.mode=checkid_setup&siteState=eyJvcGVuaWQuYXNzb2NfaGFuZGxlIjoiaW1kYl91cyIsInJlZGlyZWN0VG8iOiJodHRwczovL3d3dy5pbWRiLmNvbS8_cmVmXz1sb2dpbiJ9&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&tag=imdbtag_reg-20")

driver.find_element_by_id("ap_email").send_keys(email)
time.sleep(1)
driver.find_element_by_id("ap_password").send_keys(password)
time.sleep(1)
driver.find_element_by_id("signInSubmit").click()
driver.get("https://www.imdb.com/list/create?ref_=uspf_cr_ls_wdg")
driver.find_element_by_id("list-create-name").send_keys("NOW TV Watchlist")
driver.find_element_by_id("list-create-description").send_keys("Your IMDb watchlist filtered for NOW TV availability.\n\nhttps://github.com/xjxckk/IMDb-watchlist-filtered-for-NOW-TV-availability")
driver.find_element_by_css_selector("#list-create-form > button").click()

with open("A:\\Downloads\\watchlist.csv") as watchlist:
    reader = csv.reader(watchlist)
    next(reader)
    for row in reader:
        title = row[5]
        print("Searching for:", title)
        search = re.sub("[^A-Za-z0-9 ]+", " ", title)
        search = search.replace(" ", "_")
        url = "https://nowtv.maft.uk/catalogue/search/"+search
        response = get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        type(soup)

        count = 0
        match = soup.select_one(".wrapper > section:nth-child(4) > em:nth-child(2) > strong:nth-child(1)").text
        if match == "1 match":
            print("Found", match)
            driver.find_element_by_id("add-to-list-search").send_keys(title)
            time.sleep(3)
            print(driver.find_element_by_class_name("search_item").text)
            driver.find_element_by_class_name("search_item").click()
            count = count + 1

print("Finished, added", count, 'items to your new list called "NOW TV Watchlist".')
driver.quit()