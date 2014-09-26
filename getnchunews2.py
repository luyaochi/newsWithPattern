#!/usr/bin/python
#coding:utf-8

import urllib,re
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
nchuNews_db = client.nchuNewsDb
nchuNewsInfo_list = nchuNews_db.nchuNewsInfo_list

def htmlCode_Regxfilter(htmlCode,RegxPattern):
	pattern = re.compile(RegxPattern)
	htmlCode_Filted = pattern.findall(htmlCode)
	return htmlCode_Filted

def NumOfNewsFun(NumOfNewsList):
	if len(NumOfNewsList) > 1:
		NumOfNewsList = float(NumOfNewsList[0]+NumOfNewsList[1])
		NumOfNewsList = int(NumOfNewsList) 
		NumOfNewsList = NumOfNewsList - NumOfNewsList%20
	else:
		NumOfNewsList = int(float(NumOfNewsList[0]))
		NumOfNewsList = NumOfNewsList - NumOfNewsList%20
	return NumOfNewsList


nchuNewsListNameIDs = range(1,8)
nchuNewsListNames = [ 
	'一般新聞','興新聞',
	'榮譽榜','研討會。演講',
	'獎學金。貸款','招生。徵才。就業',
	'活動消息'
	]

mainPath = 'http://www.nchu.edu.tw/'
A = ['news.php?type=1&id=','&page=0']
pattern = {
	'totalNum_dict':'<font color="#999999">(.+?)</font>'
}

if nchuNewsInfo_list.find({}).count() == 0:
	for i in range(7):
		PathA = mainPath + A[0]
		PathB = str(nchuNewsListNameIDs[i]) + A[1]
		crawlPath = PathA + PathB

		htmlCode_Undecode = urllib.urlopen(crawlPath)
		htmlCode_Decode = htmlCode_Undecode.read().decode('utf8', 'ignore')

		NumOfNews = htmlCode_Regxfilter(htmlCode_Decode,pattern['totalNum_dict'])
		NumOfNews = NumOfNews[0][1:len(NumOfNews[0])-4]
		NumOfNews = NumOfNews.split(',')
		NumOfNews = NumOfNewsFun(NumOfNews)

		CurrentNum = NumOfNews

		NewsInfoList = {
			"NewsListNames":nchuNewsListNames[i],
			"NewsListNameIDs":nchuNewsListNameIDs[i],
			"CurrentNum":CurrentNum,
			"NumOfNews":NumOfNews
		}

		nchuNewsInfo_list.insert(NewsInfoList)
		print NewsInfoList['NewsListNames']
		print NewsInfoList['NewsListNameIDs']
		print NewsInfoList['CurrentNum']
		print NewsInfoList['NumOfNews']

#nchuNewsInfo_list.drop()
client.close()



