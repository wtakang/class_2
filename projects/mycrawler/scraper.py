#!/home/tanyi/development/pythonclass/class_2/projects/mycrawlerbin/python3


from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import sys

setlist = set()
def getUrls(url):
    global setlist
    linkresults = [] # this list will hold the links that will be found
    try:
        html = urlopen(url) #open the initial url
    except HTTPError as e:
        return None
    
    try:
        bsObj = BeautifulSoup(html.read(), features="lxml") #read the content of the web page
        links = bsObj.findAll('a') # select all links
        links = filter(lambda x: x.has_attr('href'), links) # remove empty links
    except AttributeError as e:
        return None
    else:
        if links == None: # check if no links were found
            print('there were no links on the initial website')
        else: 
            for link in links:
                linkresults.append(link.attrs['href']) # add the found links to the 'linkresults' list
            #print(a)
    regexlist = []
    pattern = re.compile(r'https?://(www\.)?\w+\.\w+') # create a regex to search for particular links eg www.google.com
    b = ''.join(linkresults) # join the values in the list to form a single string to facilitate the regex search
    matches = pattern.finditer(b)
    #print(matches)
    for link in matches:
        setlist.add(link.group(0))# add the regex search results to the setlist to eliminate repetition
    
getUrls("https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains") # u can change the link here to try other links

for i in setlist:
    print(i) # display the found links
         
sys.exit()




# class BrickSetSpider(scrapy.Spider):
#     name = 'brickset_spider'
#     start_url = ['http://brickset.com/sets/year-2016']
    
#     def parse(self,respose):
#         pass

# n = BrickSetSpider()
# print(n.name)