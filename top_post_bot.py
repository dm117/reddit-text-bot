import praw
import time

mylist = []

def authenticate():
    print("Attempting to authenticate...")
    #'toppost' peramenter is a reference to the reddit credentials used in praw.ini 
    reddit = praw.Reddit('toppost', user_agent = "Daniel's bot")
    print("Authenticated!\n")

    return reddit

def run_bot(reddit,mylist):
    text = ""
    for posts in reddit.subreddit('nba').hot(limit=3):
        text = posts.title+": "+"https://reddit.com"+posts.permalink
        mylist.append(text)
    print("Here are the results: \n"+", ".join(mylist))


def main():
    reddit = authenticate()
    run_bot(reddit,mylist)
    # while True:
    #     run_bot(reddit)

if __name__ == '__main__':
    main()