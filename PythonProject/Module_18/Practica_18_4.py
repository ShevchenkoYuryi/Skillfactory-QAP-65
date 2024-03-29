import requests
import lxml.html
from lxml import etree

# Парсинг при помощи XPATH

html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта Python
tree = lxml.html.document_fromstring(html)
title = tree.xpath('/html/head/title/text()')  # забираем текст тега <title> из тега <head> который лежит в свою очередь
# внутри тега <html> (в этом невидимом теге <head> у нас хранится основная информация о страничке.
# Её название и инструкции по отображению в браузере.

print(title)

# Парсинг при помощи функции parse и заранее скаченной HTML-странички

# создадим объект ElementTree. Он возвращается функцией parse()
tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())  # попытаемся спарсить наш файл с помощью
# HTML-парсера. Сам HTML — это то, что мы скачали и поместили в папку из браузера.

ul = tree.findall('//*[@id="content"]/div/section/div[3]/div[1]/div/ul/li')  # помещаем в аргумент методу findall
# скопированный xpath. Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)

for li in ul:
    a = li.find('a')  # в каждом элементе находим, где хранится заголовок новости. У нас это тег <a>. Т.е. гиперссылка,
    # на которую нужно нажать, чтобы перейти на страницу с новостью. Гиперссылки в HTML — это всегда тэг <a>.
    print(a.text)



# 18.4.4

html = ''' <html>
 <head> <title> Some title </title> </head>
 <body>
  <tag1> some text
     <tag2> MY TEXT </tag2>
   </tag1>
 </body>
</html>
'''

tree = lxml.html.document_fromstring(html)

text = tree.xpath('/html/body/tag1/tag2/text()')

print(text)


# 18.4.5

tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())

ul = tree.findall('//*[@id="content"]/div/section/div[3]/div[1]/div/ul/li')

for li in ul:
    t = li.find('time')
    a = li.find('a')
    print(t.get('datetime'), a.text)
