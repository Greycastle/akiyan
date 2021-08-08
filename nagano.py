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
            location_raw = item.css('h3 a::text').get()

            location_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={parse.quote(location_raw)}&key={api_key}"
            location_data = json.load(urlopen(location_url))['results'][0]
            coordinates = location_data['geometry']['location']

            yield {
                "locationRaw": location_raw,
                "longitude": coordinates['lng'],
                "latitude": coordinates['lat'],
                "prize": price,
                "image1": images[0],
                "image2": images[1],
                "image3": images[2],
            }
            