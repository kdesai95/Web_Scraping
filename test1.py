from bs4 import BeautifulSoup
import urllib
import urllib2
import requests
import re


urlInput = raw_input("enter a url which you wish to find all the URLs on\n") #this adds an option for user input
lookingFor = raw_input("what are you looking for?\n")


def runSoup(urlInput, lookingFor):#defines the function
    url = urlInput
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)
    print("The title of this page is "+soup.title.string+"\n")#reads the title
    print ("This page links to:\n")
    for link in soup.find_all('a'):
        print(link.get('href'))#displays the URLS  
    print ("\n")
    print("Your Search Returned"+ "\n")
    results=(soup.findAll(text=re.compile(lookingFor)))#will display everything inolving python
    print(results)
    return


runSoup(urlInput,lookingFor)#runs the function
