# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import csv

class ApplePipeline(object):

    def __init__(self):
        self.fileJson = open('items.json', 'w')
        self.fileCsv1 = open('items1.csv', 'w')
        self.fieldnames1 = ['time','kind','title', 'url','content']
        self.writer1 = csv.DictWriter(self.fileCsv1, fieldnames=self.fieldnames1)
        self.writer1.writeheader()     
        self.itemName = []
    def process_item(self, item, spider):
        print (item)
        line = json.dumps(dict(item)) + "\n"
        self.fileJson.write(line)

        #print (dict(item))
        dictionary = dict(item)
        if 'name' in dictionary.keys():
            self.itemName.append(dictionary)
            print('add dic OK!!')
            #print(self.itemName)
        else:
            print ("========================")
            #print (self.itemName)
            for n in self.itemName: 
                if 'url' in n.keys() and 'url' in dictionary.keys():
                    print('name dict url OK!!')
                    if (n['url'] == dictionary['url']):
                        dictionary['time'] = n['time']
                        dictionary['kind'] = n['kind']
                        self.writer1.writerow(dictionary)

        return item