#!/usr/bin/python
#coding:utf-8

import urllib,re
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
nchuNews_db = client.nchuNewsDb
nchuNews_list = nchuNews_db.nchuNewsList
nchuNewsInfo_list = nchuNews_db.nchuNewsInfo_list

def htmlCode_Regxfilter(htmlCode,RegxPattern):
	pattern = re.compile(RegxPattern)
	htmlCode_Filted = pattern.findall(htmlCode)
	return htmlCode_Filted

mainPath = 'http://www.nchu.edu.tw/'
A = ['news.php?type=1&id=','&page=']

pattern = {
		'content':'\'<div id="ind-news">(.+?)</div>\', re.S',
		'date':'<span class="date-right">(.+?)</span>',
		'link':'<a href="(.+?)">(.+?)</a>'
		}

CurrentNum = 0
totalNum = 0

for nchuNewsitem in nchuNewsInfo_list.find({},{'_id':0}):
	NewsListNameIDs = ''
	for x in  nchuNewsitem:
		if x == 'NewsListNameIDs':
			NewsListNameIDs = nchuNewsitem[x]
		elif x == 'CurrentNum':
			CurrentNum = nchuNewsitem[x]
		elif x == 'NumOfNews':
			NumOfNews = nchuNewsitem[x]
		elif x == 'NewsListNames':
			NewsListNames = nchuNewsitem[x]
		else:
			pass

		for i in range(CurrentNum-2,CurrentNum):
			crawlPath = mainPath + A[0] + str(NewsListNameIDs) + A[1] + str(i)
			htmlCode_Undecode = urllib.urlopen(crawlPath)
			htmlCode_Decode = htmlCode_Undecode.read().decode('utf8', 'ignore')

			content = htmlCode_Regxfilter(htmlCode_Decode,pattern['content'])
			date = htmlCode_Regxfilter(htmlCode_Decode,pattern['date'])
			link = htmlCode_Regxfilter(htmlCode_Decode,pattern['link'])

			for i in range(len(date)):
				if nchuNews_list.find({"newsTitle":link[i][1]}).count() == 0:
					nchuNews_list.insert({"date":date[i],"url":mainPath + link[i][0],"newsTitle":link[i][1]})
					print date[i]
					print mainPath + link[i][0]
					print link[i][1]

		CurrentNum = CurrentNum-2

client.close()


