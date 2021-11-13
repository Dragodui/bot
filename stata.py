from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True


def get_url(options, nickname):
    url = 'https://kttc.ru/wot/ru/user/'
    url_nick = url + nickname + '/'
    if len(url_nick) > 29:
        find_count_matches(url_nick, options)
        return t


def find_count_matches(url_nick, options):
    global t
    n = 0
    t = ""
    stat = ["Кол-во боёв: ", "Рейтинг Wn8: ", "% Побед: ", "Средний урон: "]
    urls = ('div[3]/span[@style]', 'div[12]/span[@title]', 'div[18]', 'div[26]')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(url_nick)
    for url in urls:
        results = driver.find_elements_by_xpath('/html/body/div[@class = "page-wrapper"]/div[@id = '
                                                '"content_wrapper"]/div[@id = "content"]/div[@class = '
                                                '"account_wrapper"]/div[@class = "account_content"]/div[@class = '
                                                '"main_stat_table"]/span[@class = "center"]/span[@class = "el"]/' + url)
        for res in results[:1]:
            res1 = res.get_attribute('innerHTML')
            stat[n] += res1
            stat[n] += '\n'
            t +=stat[n]
            n+=1
    driver.quit()
    return t


