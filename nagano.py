import scrapy
from scrapy.shell import inspect_response
from urllib import parse
from os import environ
from urllib.request import urlopen
import json

api_key = environ.get('GMAPS_API_KEY')

class NaganoSpider(scrapy.Spider):
    
    name = "nagano"

    start_urls = [
        'http://nagano-akiyabank.jp/search/'
    ]

    def parse(self, response):
        for item in response.css('.rakuenakiyaBukken'):
            images = item.css('.photoBox img::attr(src)').getall()
            price = int(float(item.css('.price .num::text').get()) * 10000)
            location = item.css('h3 a::text').get()
            yield {
                "location": location,
                "prize": price,
                "image1": images[0],
                "image2": images[1],
                "image3": images[2],
            }
            print(f"https://maps.googleapis.com/maps/api/geocode/json?address={parse.quote(location)}&key={api_key}")


# https://maps.googleapis.com/maps/api/geocode/json?address

# https://maps.googleapis.com/maps/api/geocode/json?address=長野市信州新町日原東1644-1

# def read_address():
