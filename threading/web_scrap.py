"""
Web scraping in Python is the process of extracting data 
from websites using Python libraries and tools. It allows you to automate
 the retrieval of information from web pages, which can be useful for
 data analysis, research, or automation.
"""
"https://www.langchain.com/langchain"
"https://python.langchain.com/docs/tutorials/"
"https://python.langchain.com/docs/integrations/providers/"

import threading
import requests
from bs4 import BeautifulSoup

urls=[
    'https://python.langchain.com/docs/integrations/providers/',
    'https://python.langchain.com/docs/tutorials/',
    'https://www.langchain.com/langchain'
]

def fetch_content(url):
    response =requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f"fetched {(len(soup.text))} characters from {url} ")
    print(soup) #printing all the contents we get from the urls

threads=[]
for url in urls:
        thread=threading.Thread(target=fetch_content,args=(url,))
        threads.append(thread)
        thread.start()
for thread in threads:
        thread.join()    
print("All webpages have been fetched")
        
    

