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
# titles=soup.select('.rgHvZc')
# prices=soup.find_all('span',{'class':'HRLxBb'})
stores=soup.find_all('div',class_=re.compile('dD8iuc$'))
#elements=soup.findAll(class_='xcR77')
elements=soup.findAll(class_='u30d4')
#print(shops)
#print(len(soup.select('.rgHvZc')))
#print(soup.select('.dD8iuc')[0])
#print(len(soup.find_all('div',{'class':'dD8iuc'})))
print(len(soup.find_all('span',{'class':'HRLxBb'})))


#@app.route('/')

def scrape():
	
	for el in elements:
			#pprint.pprint(el)
		if(el.find('span',{'class':'HRLxBb'}) != None):
			titles=el.select('.rgHvZc')
		
		#print(titles)
			#if(titles[0]!= None):
			title=titles[0].text
			#print(title)
			prices=el.find('span',{'class':'HRLxBb'})
			#if(prices != None):
			price=prices.text
			#print(price)
			if(el.find('div',class_='m0amQc DApVsf') != None):
				ratings=el.find('div',class_='m0amQc DApVsf')["aria-label"]
			else:
				ratings= "Not Rated!"

			if(el.find('span',{'class':'dD8iuc'}) != None):
				freeshiping = el.find('span',{'class':'dD8iuc'})
				freeshiping=freeshiping.text
			else:
				freeshiping = "Shipping details unavailable!"
			image= el.find('div',class_='oR27Gd')
			image=image.img["src"]
			arr.append({'title':title,'price':price, "rating":ratings, "freeshiping":freeshiping, "image":image, })
			

	
	# for idx, item in enumerate(titles):
	# 	title=titles[idx].getText()
	# 	price=prices[idx].getText()
	# 	store=stores[idx].getText()
 

		
	pprint.pprint(arr)
	#print(len(arr))
	#print("len of prices"+str(len(prices)))

scrape()
