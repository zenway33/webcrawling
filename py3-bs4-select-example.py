find_all 相关实例

soup.find_all("a")
soup.find("a")
soup.a.get("href")
soup.a.string
soup.p.find_all("a")
soup.find_all("a", class_="link", href="/link")
soup.find_all("a", attrs={"class": "link", "href": "/link"})
soup.find_all(class_="link", href="/link")
soup.find_all(attrs={"class": "link", "href": "/link"})
soup.find_all('ul', class_='clearfix')

#
soup.find_all("table", attrs={"width": "100%"})
bookstar = subsoup.find('span',attrs={"class": "rating_nums"}).string # 图书星级：9.0
bookcommentnum = subsoup.find('span',attrs={"class": "pl"}).string.strip('\r\n ()人评价') # 评价人数：190325

# 正则相关
import re
soup.find_all(re.compile("^b"))
soup.find_all(href=re.compile("link"))
soup.find_all("a", text=re.compile("hello"))

# Beautiful Soup CSS selector
from pprint import pprint
from bs4 import BeautifulSoup

html_content = open('bs_sample3.html')
# http://dl.dropbox.com/u/49962071/blog/python/resource/bs_sample3.html
soup = BeautifulSoup(html_content) # making soap

pprint(soup.select("title")) # get title tag
pprint(soup.select("body a")) # all a tag inside body
pprint(soup.select("html head title")) # html->head->title
pprint(soup.select("head > title")) # head->title
pprint(soup.select("p > a")) # all a tag that inside p
pprint(soup.select("body > a")) # all a tag inside body
pprint(soup.select(".sister")) # select by class
pprint(soup.select("#link1")) # select by id
pprint(soup.select('a[href="http://example.com/elsie"]'))
# find tags by attribute value
pprint(soup.select('a[href^="http://example.com/"]'))
# find tags by attribute value, all contains 'http://example.com/'
pprint(soup.select('p[lang|=en]')) # Match language codes


# css
soup.select("#link1")
soup.select('a[href^="http://"]')
soup.prettify()

#
titles = soup.select('div.property_title > a[target="_blank"]')
imgs = soup.select('img[width="160"]')
cates = soup.select('div.p13n_reasoning_v2  ')

for title,img,cate in zip(titles,imgs,cates):
    data = {
        'title': title.get_text(),
        'img': img.get('src'),
        'cate': list(cate.stripped_strings)
        }
    print(data)

# 获取数字的函数
def trans2numbers(string):
    return int(''.join(a for a in string.strip() if a.isdigit()))

def get_numbers(read):
    result = []
    for i in read:
        result.append(trans2numbers(i.string))
    return result



# soup.select 后定处理定义一个列表:
def get_pdf_urls():
    pdf_urls=[]
    for pdf_url in pdfs:
        pdf = pdf_url.get('href').strip('#')
        pdf_urls.append(pdf)
    return pdf_urls
urls = get_pdf_urls()

#取列表的奇数位:
[j for i , j in enumerate(['a', 'b','c']) if not i%2]

#定义列表,获取奇数列
def carrier_list():
    carrier_list = []
    list_a = [j for i, j in enumerate(carriers) if not i%2]
    for i in list_a:
        carrier_list.append(i)
    return carrier_list

carriers = carrier_list()

# 编辑器快捷键
https://www.zhihu.com/question/38946886
右移,选中代码块，按Tab。
要是想往左移，就按Shift + Tab

#数据分析工具
1. 在线分词工具：基于深度学习的中文在线抽词-PullWord (梁斌penny)
2. 在线词云生成工具：TAGUL - WORD CLOUD ART
3. 图表：ECharts
4. 数据爬取：Python Scrapy开发程序

#
