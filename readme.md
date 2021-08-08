# Akiyan

Scraper for getting data of Japanese "empty houses" Akiya.


## run

First set your API key for Google Maps lookup:
```
export GMAPS_API_KEY=...
```

```shell
pipenv install
pipenv run scrapy runspider nagano.py -o nagano.csv
```

## debugging

It's easiest to simply grab the url and run it in Scrapy shell:

```shell
pipenv run scrapy shell http://nagano-akiyabank.jp/search/
```