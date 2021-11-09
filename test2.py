
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://kttc.ru/wot/ru/user/Matvey_0001/")

results = driver.find_elements_by_xpath('//div[@id="ORE_PARAMS"]')

for result in results:
    r = result.find_element_by_xpath('.//span').get_attribute('text')
    print(str(r))


driver.quit()