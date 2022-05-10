# wellcome this is a basic web scrapper that gather address
# from google maps and save it in txt file
# let us start now
import json

from time import sleep
from selenium import webdriver
from extract_addresses import extract_addresses
from store_into_a_database import storeInADatabase
def look_up_google_maps():
    queries = extract_addresses()
    # [{"name":"John Doe","address":"Empire State Building","google_maps_address":""},{"name":"Jane Doe","address":"Flatiron Building","google_maps_address":""}]
    url = 'https://google.com/maps/'
    browser = webdriver.Chrome()
    browser.get(url)
    for query in range(len(queries)):
        browser.find_element_by_xpath('//*[@id="searchboxinput"]').send_keys(f"{queries[query]['address']}")
        browser.find_element_by_xpath('//*[@id="searchbox-searchbutton"]').click()
        sleep(15)
        google_result_plus_zip_code = browser.find_element_by_xpath('//div[@jsan="7.QSFF4-text,7.gm2-body-2"]').text
        queries[query]["google_maps_address"] = google_result_plus_zip_code
        browser.find_element_by_xpath('//*[@id="sb_cb50"]').click()
        print(queries[query]["google_maps_address"])
    return queries

#saving the resulted addresses from google maps in a json file for reuse (hint databases)
results = look_up_google_maps()
with open('./results.json','w+') as result:
    result.writelines(json.dumps(results))
print(results)
storeInADatabase()
