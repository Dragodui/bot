from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
num = []


def get_url1(name):
    url = 'https://www.youtube.com/results?search_query=' + name
    found_title(url)
    return res2, f


def found_title(url):
    global res2, f
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    results = driver.find_elements_by_id(
        'video-title')
    # //a[@id = "video-title"][@class = "yt-simple-endpoint style-scope ytd-video-renderer"]
    # res1 = res.get_attribute('title')

    # //yt-formatted-string[@class = "style-scope ytd-video-renderer"][@aria-label]
    # res1 = res.get_attribute('innerHTML')
    f = ''
    for res in results[:1]:
        res2 = res.get_attribute('href')
        num.append(res2)
        res1 = res.get_attribute('title')
        f += res1
    return res2, f


