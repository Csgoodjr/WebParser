'''
    CJ Good
    Jul 15, 2019
    Wiki Finder
''' 

import os
import sys
import wikipedia

class WikiFinder:

    def __init__(self,topic):
        self.__topic = topic

    def getTopic(self):
        return self.__topic

    def getSummary(self,num_sentences=1):
        try:
            summary = wikipedia.summary(self.__topic,sentences=num_sentences)
            return summary
        except:
            return "Error finding information about that topic"

    def getInfo(self):
        try:
            info = wikipedia.page(self.__topic)
            return info
        except:
            return "Error finding information about that topic"

    def getRelatedLinks(self):


