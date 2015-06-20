# -*- coding: utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup

country = {0: 'USD', 1: 'HKD', 2: 'GBP', 3: 'AUD', 4: 'CAD', 5: 'SGD', 6: 'CHF', 7: 'JPY', 8: 'SEK', 9: 'NZD', 10: 'THB', 11: 'PHP', 12: 'IDR', 13: 'EUR', 14: 'KRW', 15: 'VND', 16: 'MYR', 17: 'CNY'}

def getRate(countrystr):
	url = "http://rate.bot.com.tw/Pages/Static/UIP003.zh-TW.htm"
	soup = BeautifulSoup(urllib2.urlopen(url).read())

	table = soup.find('div', attrs={'class': 'entry-content'})
	flag = 0
	count = 0
	rate_list = []
	rows = table.findAll('tr')
	for tr in rows:
	    cols = tr.findAll('td')
	    for tr2 in cols:
	    	for tr3 in tr2:
	    		if flag == 1:
	    			rate_list.append(float(tr3))
	    			count += 1
	    			if count == 4:
	    				flag = 0
	    				break
	    		if countrystr in tr3:
	    			flag = 1
	return rate_list    		
"""
def getRate():
	url = "http://rate.bot.com.tw/Pages/Static/UIP003.zh-TW.htm"
	soup = BeautifulSoup(urllib2.urlopen(url).read())

	table = soup.find('div', attrs={'class': 'entry-content'})
	flag = 0
	count = 0
	rate_list = []
	rows = table.findAll('tr')
	for tr in rows:
    	cols = tr.findAll('td')
    	for tr2 in cols:
    		for tr3 in tr2:
    			if flag == 1:
    				rate_list.append(float(tr3))
    				count += 1
    				if count == 4:
    					flag = 0
    					break
    			if '' in tr3:
    				flag = 1

"""
def GetInformation(value):
	print country[value]
	countrystr = country[value]
	return getRate(countrystr)



