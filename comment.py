from bs4 import BeautifulSoup
import requests
import pandas as pd
import json

def main():
    # read an entry from csv, get a {anime: sn}
    file_name = "6-23_scrape.csv"
    entrance = 'https://ani.gamer.com.tw/ajax/danmuGet.php'
    df = pd.read_csv(file_name)
    # random choose an anime
    data = df.iloc[15]
    name = data["Anime title"]
    url = data["url"]
    # use id to fetch comment
    id = url.split("sn=")[1]
    comments = fetch_all_comments(entrance, id)
    # d = json.loads(comments)
    # print(d)
    # print(type(d))
    # for i in d:
    #     print(i)
    # print(type(comments.encode('utf-8')))
    # d = json.loads(comments.encode('utf-8'))
    # print(d)
    # print(type(d))


    print(type(comments))
    d_list = json.loads(comments)
    # print(type(d_list))
    # j = json.dumps(d_list)
    # print(j)
    # print(comments)
    # print(d_list)
    # print(len(d_list))
    # print(type(d_list))
    print(d_list[13])
    print(type(d_list[13]))
    # print(json.dumps(d_list[9]))
    print(json.dumps(d_list[13]))
    print(type(json.dumps(d_list[13])))
    # print(comments)


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
def fetch_all_comments(url, anime_id):
    # resource = requests.get(url)
    resource = requests.post(url, data={'sn':anime_id}) 
    # resource = requests.post(url)
    # print(type(resource))
    # print(resource.text) ###
    # soup = BeautifulSoup(resource.text, 'html.parser')
    # print(soup.prettify().encode('utf-8'))

    # print(type(soup.prettify()))
    # print(soup.prettify())
    # with open('test', 'r') as f:
    #     f.write(soup.prettify().)
    
    # comments = resource.json()

    # for i in range(20):
    #     print("this is {} comment".format(i))
    #     comments.append(i)
    # return comments
    # return comments

    return resource.text

# for example: new sakura battle
# entrance = "https://ani.gamer.com.tw/animeVideo.php?sn=15922"
# entrance = 'https://ani.gamer.com.tw/animeVideo.php?sn=15922#ani-tab-content-1'
# entrance = 'https://i2.bahamut.com.tw/js/anime.js?v=1593503917'

# entrance = 'https://ani.gamer.com.tw/ajax/danmuGet.php'
# comments = fetch_all_comments(entrance)

# print("finish")
# print(comments)

if __name__ == '__main__':
    main()