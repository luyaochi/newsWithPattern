#!/usr/bin/python
#coding:utf-8
import urllib,re

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

class getPageContent:
	def __init__(self):
		self.mainPath = self.getPath()
		self.PathVar = self.getPathVar()
		self.Pattern = self.getPattern()
		self.crawlPath = self.getCrawlPath()

	def getMainPath(self):
		mainPath = 'http://www.nchu.edu.tw/'
		return mainPath

	def getPattern(self):
		Pattern = {
			'Pattern':'<font color="#999999">(.+?)</font>'
		}
		return Pattern

	def getPathVar(self):
		PathVar = ['news.php?type=1&id=1','&page=0']
		return PathVar

	def getCrawlPath(self):
		return selt.mainPath + self.PathVar[0] + self.PathVar[1]

	def crawlingPage(self):
		print 'crawlingPage'
	def printPath(self):
		print self

class NewsTypeInfoList:
	def __init__(self,NewsSource):
		self.NewsSource = NewsSource
		self.mainPath = ''
		self.PathVar = ''
		self.IDsOfNewsList = [0]
		self.NewsListNames = ['']
		self.numOfNews = []
		self.totalNumOfNews = []

	def setNewsTypeListInfo(self):
		self.mainPath,self.PathVar = self.getNewTypeListPathInfoFromDb()
		self.NewsListNames = self.getNewTypeListNameFromDb()
		self.IDsOfNewsList = range(1,len(self.NewsListNames)+1)
		self.numOfNews = []
		self.totalNumOfNews = []

	def updateNewsTypeListInfo(self):
		self.setNewsTypeListInfo()
		self.numOfNews = ['not update here']
		self.totalNumOfNews = self.crawlNewsList()

	def saveNewsTypeListInfo(self):
		NewsItem = {
			"NewsListNames":selfNewsListNames[i],
			"IDsOfNewsList":self.IDsOfNewsList[i],
			"numOfNews":self.numOfNews,
			"totalNumOfNews":self.totalNumOfNews
		}
		return NewsItem
	def getNewTypeListNameFromDb(self):
	 	NewsListNames = [ 
			'一般新聞',
			'興新聞',
			'榮譽榜',
			'研討會。演講',
			'獎學金。貸款',
			'招生。徵才。就業',
			'活動消息'
			]# 7 items
		return NewsListNames

	def getNewTypeListPathInfoFromDb(self):
		mainPath = 'http://www.nchu.edu.tw/'
		PathVar = ['news.php?type=1&id=','&page=0']
		return mainPath,PathVar

	def getPattern(self):
		totalNumOfNewsPattern = {
			'totalNum_dict':'<font color="#999999">(.+?)</font>'
		}
		return totalNumOfNewsPattern

	def crawlNewsList(self):
		PathA = self.mainPath + self.PathVar[0]
		PathB = str(self.IDsOfNewsList[0]) + self.PathVar[1]
		crawlPath = PathA + PathB
		htmlCode_Undecode = urllib.urlopen(crawlPath)
		htmlCode_Decode = htmlCode_Undecode.read().decode('utf8', 'ignore')
		NumOfNews = htmlCode_Regxfilter(htmlCode_Decode,self.getPattern()['totalNum_dict'])
		NumOfNews = NumOfNews[0][1:len(NumOfNews[0])-4]
		NumOfNews = NumOfNews.split(',')
		NumOfNews = NumOfNewsFun(NumOfNews)
		return NumOfNews

	def printNewsTypeInfo(self):
		print self.NewsSource
		print self.mainPath
		print self.PathVar
		for i in range(len(self.IDsOfNewsList)):
			print self.IDsOfNewsList[i]
			print self.NewsListNames[i]
			print self.numOfNews
			print self.totalNumOfNews
	






ContentOfNews = NewsTypeInfoList('NCHU')
ContentOfNews.printNewsTypeInfo()

ContentOfNews.setNewsTypeListInfo()
ContentOfNews.printNewsTypeInfo()

ContentOfNews.updateNewsTypeListInfo()
ContentOfNews.printNewsTypeInfo()
