from flask import Flask, render_template 
import requests
from bs4 import BeautifulSoup
import pprint
import re
import sys


app=Flask(__name__)


#keyword='microwave'
url= 'https://shopping.google.com/search?q='+' '.join(sys.argv[1:])
print(url)
arr=[]
	
res=requests.get(url)
#print(res.text)
soup=BeautifulSoup(res.text, 'html.parser')

#print(soup.prettify())

#element=soup.findAll('div',class_ =re.compile('xcr77'))
elements=soup.findAll(class_='xcR77')
#print(elements)
#print("\n\n".join("{} {}".format(el['class'],el.get_text()) for el in elements ))
i=0
shoplink=''
for el in elements:
	i+=1
	#titles=soup.select('.rgHvZc')
	prices=el.find('span',{'class':'HRLxBb'})
	rating=el.find('div',class_=re.compile('m0amQc DApVsf'))
	freeshiping = el.find('span',{'class':'dD8iuc'})
	link_img = el.find('a')
	#link = get_link(link_img)
	
	print(i)
	print(prices)
	print(rating)
	print(freeshiping)
	print(link_img)
	print(shoplink)
	print("\n\n")


#def get_link(link):
#
#	link.get('href')
#	try:
#		m = re.search("(?P<url>https?://[^\s]+)", link)
#		n = m.group(0)
#		rul = n.split('&')[0]
#		domain = urlparse(rul)
#		if(re.search('google.com', domain.netloc)):
#			continue
#		else:
#			shoplink = rul
#	except:
#		continue
	
#	except Exception as ex:
#		print(str(ex))
#		print("into except")
#	finally:
#		return shoplink



#titles=soup.select('.rgHvZc')
#prices=soup.find_all('span',{'class':'HRLxBb'})
#stores=soup.find_all('div',class_=re.compile('dD8iuc$'))
#print(shops)
#print(len(soup.select('.rgHvZc')))
#print(soup.select('.dD8iuc')[0])
#print(len(soup.find_all('div',{'class':'dD8iuc'})))
#print(len(soup.find_all('span',{'class':'HRLxBb'})))


#@app.route('/')

#def scrape():
#	
#	for idx, item in enumerate(titles):
#		title=titles[idx].getText()
#		price=prices[idx].getText()
#		store=stores[idx].getText()
#
#		arr.append({'title':title,'price':price, 'store':" ".join(store.split(' ')[2:])})
#	pprint.pprint(arr)
	#print(len(arr))
	#print("len of prices"+str(len(prices)))

#scrape()
