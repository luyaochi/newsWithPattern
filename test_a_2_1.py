#!/usr/bin/python
#coding:utf-8
import unittest
import sys,urllib,re
from StringIO import StringIO

from a_2_1 import getPageHtmlCode
class TestgetPageHtmlCode(unittest.TestCase):
	def setUp(self):
		self.PageHtmlCode = getPageHtmlCode()

	def test_getMainPath(self):
		Unit1 = self.PageHtmlCode.getMainPath()
		Unit2 = self.PageHtmlCode.MainPath
		self.assertEqual(Unit1,Unit2)

	def test_getPathVar(self):
		Unit1 = self.PageHtmlCode.getPathVar()
		Unit2 = self.PageHtmlCode.PathVar
		self.assertEqual(Unit1,Unit2)

	def test_getPattern(self):
		Unit1 = self.PageHtmlCode.getPattern()
		Unit2 = self.PageHtmlCode.Pattern
		self.assertEqual(Unit1,Unit2)

	def test_getCrawlPath(self):
		Unit1 = self.PageHtmlCode.getCrawlPath()
		Unit2 = self.PageHtmlCode.CrawlPath
		self.assertEqual(Unit1,Unit2)

	def test_getHtmlCode(self):
		self.assertEqual(self.PageHtmlCode.getHtmlCode(),self.PageHtmlCode.htmlCode)

	def test_printPath(self):
		saved_stdout = sys.stdout
		try:
			out = StringIO()
			sys.stdout = out
			self.PageHtmlCode.printPath()
			output = out.getvalue().strip()
			assert output == 'http://www.nchu.edu.tw/\n["news.php?type=1&id=1","&page=0"\n{"Pattern":"<font color="#999999">(.+?)</font>"}http://www.nchu.edu.tw/news.php?type=1&id=1&page=0"'
		finally:
			sys.stdout = saved_stdout

if __name__ == '__main__':
	#unittest.main()
	suite = unittest.TestLoader().loadTestsFromTestCase(TestgetPageHtmlCode)
	unittest.TextTestRunner(verbosity=2).run(suite)

