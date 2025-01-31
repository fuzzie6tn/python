from selenium import webdriver

chrome_driver_path = ""
driver = webdriver.Chrome(chrome_driver_path)

driver.get("hthttps://en.wikipedia.org/wiki/Main_Page")
article_count= driver.find_element_by_css_selector("#article a")

all_portals= driver.find_element_by_link_text("All portals")

search = driver.find_element_by_link_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)