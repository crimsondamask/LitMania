
from selenium import webdriver
from qbittorrent import Client

url = 'https://thepiratebay.org/search.php?q=user:workerbee'
p = 0 
Links_to_Download = []
while p < 10:
    COUNT = 1
    browser = webdriver.Firefox()
    browser.get(url)
    print('Downloading page %s...' % url)
    Links = browser.find_elements_by_xpath("//a[@href]")
    for a in Links:
        link = a.get_attribute('href')
        if link.startswith('magnet'):
            Links_to_Download.append(link)
            COUNT += 1
    print('%s links found' %COUNT)
    p += 1
    print('Page ==> %s' %p)
    url = 'https://thepiratebay.org/search.php?q=user:workerbee:%s' %p 
    browser.close()

qb = Client('http://127.0.0.1:8080/')

qb.login('admin', 'crimsondamask')

dl_path = '/media/crimsondamask/Lonelyblackhole/Crimsondamask/Books/workbee'
COUNT2 = 0
for link in Links_to_Download:
    qb.download_from_link(str(link), savepath=dl_path)
    COUNT2 += 1
    print('Added torrent number %s' %COUNT2)
print('%s torrents are downloading' %COUNT2)



