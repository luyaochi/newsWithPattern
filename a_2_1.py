#!/usr/bin/python
#coding:utf-8
import urllib,re

class getPageHtmlCode:
	def __init__(self):
		self.MainPath = self.getMainPath()
		self.PathVar = self.getPathVar()
		self.Pattern = self.getPattern()
		self.CrawlPath = self.getCrawlPath()
		self.htmlCode = self.getHtmlCode()
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
		return self.MainPath + self.PathVar[0] + self.PathVar[1]

	def getHtmlCode(self):
		Undecode = urllib.urlopen(self.CrawlPath)
		return Undecode.read().decode('utf8', 'ignore')

	def printPath(self):
		print self.MainPath
		print self.PathVar
		print self.Pattern
		print self.CrawlPath



