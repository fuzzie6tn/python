from selenium import webdriver

chrome_driver_path = "/Users/"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_bar =  driver.find_element_by_name("q")
# print(search_bar.tag_name("placeholder"))



driver.quit()