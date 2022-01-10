from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
num = []


def get_url1(name):
    url = 'https://www.youtube.com/results?search_query=' + name
    found_title(url)
    return res1, f


def found_title(url):
    global res1, f
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    result = driver.find_elements_by_id(
        'video-title')
    f = ''
    res = result[0]
    res1 = res.get_attribute('href')
    res2 = res.get_attribute('title')
    f += res2
    return res1, f


d = get_url1("erika")
print(d)
