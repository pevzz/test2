from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

my_driver = webdriver.Chrome(executable_path='c:\\chromedriver.exe')
my_driver.get('C:\\Users\\Hhh36\\Downloads\\tip_calc\\index.html')


my_driver.find_element(By.ID, "billamt").send_keys("100")
my_driver.find_element(By.XPATH, '//*[@id="serviceQual"]/option[3]').click()
# select = Select(my_driver.find_element(By.ID,'serviceQual'))
# select.select_by_visible_text("20% - Good")
my_driver.find_element(By.ID, "peopleamt").send_keys("4")
my_driver.find_element(By.ID, "calculate").click()

tip_result = my_driver.find_element(By.ID, "tip").text
assert tip_result == "5.00"

# print(tip_result)



input()