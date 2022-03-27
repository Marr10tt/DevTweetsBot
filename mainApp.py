import tweepy
import requests

#the main function that will handle everything
def __main__ ():
    print("Hello World!")

    #this function will scrape the web every time the bot is run to completely overwrite a txt
    #progress in the file will not be lost as i will keep track within another file of the bots position in the file
    def webScraper():
        print("will scrape the web")

    #this function will send out a given tweet based on the bots current location in the txt file
    #this will be done every x time, where x may be either a period of time or a specified time of day
    def tweet():
        print("will handle the sending of tweets")
    
    #most functions will be called here
    webScraper()

    #this function will likely be in an infinite loop - with the loop pausing every x seconds (until a tweet needs to be sent)
    tweet()

__main__()