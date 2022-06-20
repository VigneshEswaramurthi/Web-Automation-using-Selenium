from lib2to3.pgen2.driver import Driver
from selenium import webdriver
from selenium.webdriver.support.ui import Select


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#edgeBrowser = webdriver.Edge(r"D:\Edge-driver\msedgedriver.exe")

driver = webdriver.Chrome(options=options,executable_path=r'<Chrome-driver>')

#driver.maximize_window()


url1="<ENDPOINT>"

driver.get(url1)

 
#Login into web page using selenium

user_block = driver.find_element("name", "username")
pw_block = driver.find_element_by_name("password")

user_block.send_keys("Admin")
pw_block.send_keys("Admin123")

html_list = driver.find_element_by_id("sessionLocation")
items = html_list.find_elements_by_tag_name("li")
for item in items:
    text = item.text
    if(text=="Laboratory"):
        clickingUl=driver.find_element_by_id(text)
        clickingUl.click()
    print(text)

submit_button = driver.find_element_by_xpath("//input[@type='submit']")

submit_button.click()



ddelement= Select(driver.find_element_by_id('id_contact'))
ddelement.select_by_index(1)


email = driver.find_element("id", "email")
email.send_keys("test@gmail.com")
orderReference=driver.find_element("id", "id_order")
orderReference.send_keys("Admin")
Message=driver.find_element("name", "message")
Message.send_keys("ok")


submit_button = driver.find_element("id", "submitMessage")
submit_button.click()

driver.get_screenshot_as_file("capture.png")