from selenium import webdriver

chrome_wedriver_path= "/us"
driver = webdriver.Chrome(executable_path=chrome_wedriver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count= driver.find_elements_by_css_selector("#articlecount a")