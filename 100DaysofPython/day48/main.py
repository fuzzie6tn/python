from selenium import webdriver

chrome_driver_path = "/Users/"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_bar =  driver.find_element_by_name("q")
# print(search_bar.tag_name("placeholder"))

event_times = driver.find_elements_by_css_selector(".event-widget time")
# for time in event_times:
#     print(time.text)
event_name = driver.find_elements_by_css_selector(".event-widget li a")
for name in event_name:
    print(name.text)

events = {}
for n in range(len(event_times)):
    events[n]={
        "time": event_times[n],
        "name":event_name[n]
    }

driver.quit()