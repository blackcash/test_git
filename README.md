# 利用scrapy 來爬取蘋果新聞的前十頁的即時新聞
> item1.csv -->產生出來新聞的資料 <br>
> item.py --> scrapy 的item物件（資料）<br>
> pipelines.py --> scrapy的資料儲存和處理的地方<br>
> setting.py --> scrapy的設定值，其中要使用pipelines也必須從這設定中打開 <br>
>> ITEM_PIPELINES = {  <br>
>>    'apple.pipelines.ApplePipeline': 300, <br>
>> }  <br>
> AppleCrawler.py --> 資料取得的地方其中name即是要呼叫時使用，在此的name = 'apple' <br>
>> scrapy crawl apple  <br>
