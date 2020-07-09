from bs4 import BeautifulSoup
import requests
import pandas as pd

def main():
    pass


def get_episode_list(func):
    def wrap(*args, **kargs):
        # get the #episode
        comments = func(*args, **kargs)
        # scrape the other episode
        for i in range(12):
            if not i == 8:
                print("the {}th episode is ...".format(i))
        return comments, i
    return wrap

# prime function to get comment
# @get_episode_list
def fetch_all_comments(url):
    # resource = requests.get(url)
    resource = requests.post(url, data={'sn':'15922'})
    # resource = requests.post(url)
    print(resource.text)
    # soup = BeautifulSoup(resource.text, 'html.parser')
    # print(soup.prettify().encode('utf-8'))

    # print(type(soup.prettify()))
    # print(soup.prettify())
    # with open('test', 'r') as f:
    #     f.write(soup.prettify().)
    
    comments = []
    # for i in range(20):
    #     print("this is {} comment".format(i))
    #     comments.append(i)
    return comments

# for example: new sakura battle
# entrance = "https://ani.gamer.com.tw/animeVideo.php?sn=15922"
# entrance = 'https://ani.gamer.com.tw/animeVideo.php?sn=15922#ani-tab-content-1'
# entrance = 'https://i2.bahamut.com.tw/js/anime.js?v=1593503917'
entrance = 'https://ani.gamer.com.tw/ajax/danmuGet.php'
comments = fetch_all_comments(entrance)
# print("finish")
# print(comments)

if __name__ == '__main__':
    main()