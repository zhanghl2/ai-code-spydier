import requests
from lxml import etree

from cookies import get_cookies


def GetHtml():
    headers ={
       'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X)',
       'Host':"www.di-code.com"
    }
    cookkk = get_cookies()
    cookies = {
       'sessionid': cookkk
    }
    url = 'http://www.di-code.com/home/forum/solutions?page=1&page_size=8&problem_id=1008'
    page_text = requests.get(url).text
    print(page_text)
    #tree = etree.HTML(page_text)
    #html_data = tree.xpath('//div[@class="Solutions_header"]/ul')
    #print(html_data)


GetHtml()
