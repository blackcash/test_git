import scrapy
from bs4 import BeautifulSoup
from apple.items import AppleItem
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.linkextractors import LinkExtractor

class AppleCrawler(CrawlSpider):
	start_urls = [
	'https://tw.appledaily.com/new/realtime/',
	]
	domains = ['tw.appledaily.com']
	name = 'apple'
	def parse(self,response):
		if response.url.index('https://tw.appledaily.com/new/realtime/') >= 0:	
				res = BeautifulSoup(response.body,'lxml')
				for news in res.select('.rtddt'):
					item = AppleItem()
					item['name'] = news.select('h1')[0].text
					item['url'] = news.select('a')[0]['href']
					item['time'] = news.select('time')[0].text
					print ('----------',item['time'])
					item['kind'] = news.select('h2')[0].text
					print ('----------',item['kind'])
					yield item
					#print (news.select('h1')[0].text,news.select('a')[0]['href'])	
					yield scrapy.Request(news.select('a')[0]['href'],self.parse_detail)

				for page in range(2,10): 
					yield scrapy.Request('https://tw.appledaily.com/new/realtime/'+str(page),self.parse_list)

	def parse_list(self,response):
		res = BeautifulSoup(response.body,'lxml')
		for news in res.select('.rtddt'):
			item = AppleItem()
			item['name'] = news.select('h1')[0].text
			item['url'] = news.select('a')[0]['href']
			item['time'] = news.select('time')[0].text
			print ('----------',item['time'])
			item['kind'] = news.select('h2')[0].text
			print ('----------',item['kind'])
			yield item
			#print (news.select('h1')[0].text,news.select('a')[0]['href'])	
			yield scrapy.Request(news.select('a')[0]['href'],self.parse_detail)

	def parse_detail(self,response):
		item = AppleItem()
		res = BeautifulSoup(response.body,'lxml')
		#print (res.select('.ndArticle_leftColumn')[0].select('h1')[0].text)
		#print (res.select('.ndArticle_margin')[0].select('p')[0].text)
		item['title'] = res.select('.ndArticle_leftColumn')[0].select('h1')[0].text
		item['content'] = res.select('.ndArticle_margin')[0].select('p')[0].text
		item['url'] = response.url
		yield item

