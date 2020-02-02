'''
    CJ Good
    Jul 15, 2019
    Web Page Parser and Analyer
    Uses:
    - Get Default Browser
    - Find All Elements by Type
    - Get All Links on a Page
    Externals/APIs:
    - BeautifulSoup
    - Webbrowser (Built-in)
    - Requests (Built-in)
    Synopsis:
    Use this tool to gather information from webpages for external uses (such as page analysis). Designed for personal, non-intrusive
    purposes to crawl the web from other scripts to automate web searches to gather more useful information.
'''

import bs4
import webbrowser
import requests

class WebPageParser:

    #Init
    def __init__(self,url=None):
        self.__url = url
        self.__page_content = bs4.BeautifulSoup(requests.get(url).content,features="html.parser")

    #Print Class
    #Return Type: Str
    def __str__(self):
        return self.__url

    #Return the default browser
    #Return Type: Str
    def get_user_default_browser(self):
        return self.__default_browser

    #Return the page HTML
    #Return Type: Str
    def get_page_content(self):
        return self.__page_content

    #Return a list of all specified elements on a page
    #Return Type: List
    def find_all_element_of_type(self,element):
        return self.__page_content.find_all(element)
        
    #Return a dictionary of all links on a page
    #Return Type: Dictionary
    def find_all_links(self):
        link_dict = {}
        for i in self.__page_content.find_all('a'):
            link_content = ''
            try:
                if len(i.contents[0]) > 1:
                    try:
                        if len(i['href']) > 1:
                            link_dict[i.contents[0].lower()] = self.__url + i['href']
                    except:
                        continue
            except:
                continue
        return link_dict

''' Test Parser '''
if __name__ == "__main__":
    #Preset a URL
    test_url_list = [
        'https://www.visionlearning.com/en/glossary',
        'http://mentalfloss.com/article/58254/13-scientific-terms-even-smart-people-misuse',
        'https://www.dictionary.com/e/s/science-vocab/#element',
        'https://www.eufic.org/en/understanding-science/category/scientific-terms'
    ]

    list_of_master_links = []

    for i in test_url_list:
        #Test Object
        testpage = WebPageParser(i)
        #print(testpage.find_all_element_of_type('a'))
        list_of_master_links.append(testpage.find_all_links())

    ''' Where is this useful? '''
    ''' I want links about science from some sites '''
    for i in list_of_master_links:
        for j in i:
            if 'science' in j:
                print(i[j])


    