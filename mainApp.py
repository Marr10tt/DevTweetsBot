import tweepy
import requests
from bs4 import BeautifulSoup
import config

auth = None

#the main function that will handle everything
def __main__ ():
    global auth
    fileName = "tweets.txt"

    #this function will scrape the web every time the bot is run to completely overwrite a txt
    #progress in the file will not be lost as i will keep track within another file of the bots position in the file
    def webScraper():
        soup = None

        #saves url - requests information from url - converts into readable html using html5 parser
        url = "https://betterprogramming.pub/101-funny-programmer-quotes-76c7f335b92d"
        urlRequest = requests.get(url)
        soup = BeautifulSoup(urlRequest.content, 'html5lib')

        #opens the file needed to store all tweets in
        tweetFile = open(fileName, 'w')

        #finds all ordered lists in the website - this is where all quotes are stored
        listsList = soup.findAll('ol')
        i=0
        #loops through each list
        for ol in listsList:
            tweets = listsList[i].findChildren('li', recursive=False)
            #loops through each lists children with tag li and writes clean data to text file
            for child in tweets:
                #cleans up data by replacing the end phrase with nothing 
                tweetText = (child.text).replace(' (source)', '')
                tweetFile.write(tweetText+'\n')
            i+=1

        #closes the text file after use
        tweetFile.close()

    #this function configures the tweepy API with the correct credentials
    def tweepyConfig():
        #sets handler using consumer key and secret
        auth = tweepy.OAuthHandler(config.consumerToken, config.consumerSecret)
        #sets access token with access token and token secret
        auth.set_access_token(config.accessToken, config.accessSecret)

        #creates object for API use
        api = tweepy.API(auth)

        #this function will send out a given tweet based on the bots current location in the txt file
        #this will be done every x time, where x may be either a period of time or a specified time of day
        #variable tweetContent should be passed as string
        def tweet(tweetContent):
            api.update_status(tweetContent)
        
        tweet("hello world")
        
    #most functions will be called here
    webScraper()
    tweepyConfig()

    #this function will likely be in an infinite loop - with the loop pausing every x seconds (until a tweet needs to be sent)

__main__()