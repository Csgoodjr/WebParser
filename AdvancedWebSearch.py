'''
    CJ Good
    Jul 15, 2019
    Advanced Web Search
'''

import bs4
import requests
import wikipedia
from WebPageParser import WebPageParser
from WikiFinder import WikiFinder

# Advanced Google Search
def advanced_web_search(topic):
    # Removes any spaces from the topic with a '+' so google can query
    search_term = topic.replace(' ','+')
    # Creates the search URL for the query
    url = 'https://www.google.com/search?q={}'.format(search_term)
    # Alerts user about what is being performed
    print("Searching for",topic,"on google...")
    print("Using the url:",url)
    # This response object holds all of the information from the http request
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        print("Request processed successfully!")
        # Init the parser for the webpage
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        results = []
        # Run through the results to find all anchor tags with references
        for result in soup.find_all('a',href=True,text=True):
            # Extract the reference
            link = result['href']
            # If the link has a proper reference append it to the result list
            if link != []:
                results.append(link)
        # Return results to the user
        return results
    else:
        print("Request failed... please try again")
        # Return NULL is response fails
        return []

# Searches webpage -- using WebPageParser plugin
# WebPageParser is a custom solution to find elements on page
def page_deep_dive(webpage):
    pass

# WikiSearcher
# Uses WebPageParser and the WikiFinder to find wiki info
def wiki_deep_dive(topic):
    pass

if __name__ == "__main__":
    # This line gathers input from the user about what to search for
    topic_input = input("Enter a topic to search...\n")
    # Calls the search function with the included topic
    searches = advanced_web_search(topic_input)
    #print(searches)

