from bs4 import BeautifulSoup
import urllib
import urllib2
import requests

urlInput = raw_input("enter a url which you wish to find all the URLs on\n") #this adds an option for user input
lookingFor = raw_input("what are you looking for?\n")
url = urlInput
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content)
for link in soup.find_all('a'):
    print(link.get('href'))#displays the URLS
    
print(soup.title.string)#reads the title
print(soup.find_all(text=re.compile(lookingFor)))#will display everything inolving python



