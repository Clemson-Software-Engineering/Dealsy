from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
api = Api(app)

CORS(app)

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate',
	'DNT': '1',
	'Connection': 'keep-alive',
	'Upgrade-Insecure-Requests': '1'
}

GOOGLE_SHOPPING_REQUEST_URL = "https://www.google.com/search?psb=1&tbm=shop&q="

@app.route("/")

class Deals(Resource):
    def get(self, search_query):
        print('Search Query:' + search_query)

        results = []

        session = requests.Session()
        url = GOOGLE_SHOPPING_REQUEST_URL + search_query + '&ie=utf-8&oe=utf-8'
        response = session.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")

        results_table = soup.find_all("div", {"class": "xcR77"})
        if results_table is not None:
            for result in results_table:
                link = result.find("div", {"class": "rgHvZc"})
                if link is not None and link.find("a") is not None:
                    store = "https://" + link.find("a")['href'].split('/')[3] if len(link.find("a")["href"].split('/')) >= 3 else "#"
                    product = link.find("a").text
                    brand = product.split(" ")[0]
                    image = result.find("img")["src"]
                    stars = result.find("div", {"class": "m0amQc DApVsf"})
                    rating = stars["aria-label"].split(' ')[0] if stars is not None else 0
                    reviews = result.findAll("span")[0].text.replace('(', '').replace(')', '')
                    price = result.findAll("span")[1].text
                    shipping = "FREE" if len(result.findAll("span")) > 3 else "NOT FREE"
                    condition = "NEW"
                    results.append({
                        "store": store,
                        "product": product,
                        "brand": brand,
                        "image": image,
                        "rating": rating,
                        "reviews": reviews,
                        "price": price,
                        "shipping": shipping,
                        "condition": condition
                    })
        return jsonify(results)

api.add_resource(Deals, '/deals/<search_query>')