import os
import scrapy

url = os.environ['url']

class quotes_spider(scrapy.Spider):
  name="quotes"
  start_urls=[url]

  def parse(self,response):
    
    
      yield from response.follow_all(response.css('div.content div.list-film-item a::attr(href)').getall(),callback=self.parse)
      yield {
        "url":response.css('a::attr(href)').re(r'.+mp4$'),
        "name":response.css('h1.title-inside::text').get()
        
      }

      yield from response.follow_all(css="li.next a", callback=self.parse)