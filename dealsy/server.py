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
titles=soup.select('.rgHvZc')
prices=soup.find_all('span',{'class':'HRLxBb'})
stores=soup.find_all('div',class_=re.compile('dD8iuc$'))
#print(shops)
#print(len(soup.select('.rgHvZc')))
#print(soup.select('.dD8iuc')[0])
#print(len(soup.find_all('div',{'class':'dD8iuc'})))
print(len(soup.find_all('span',{'class':'HRLxBb'})))


#@app.route('/')

def scrape():
	
	for idx, item in enumerate(titles):
		title=titles[idx].getText()
		price=prices[idx].getText()
		store=stores[idx].getText()
 

		arr.append({'title':title,'price':price, 'store':" ".join(store.split(' ')[2:])})
	pprint.pprint(arr)
	#print(len(arr))
	#print("len of prices"+str(len(prices)))

scrape()
