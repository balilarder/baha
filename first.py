from bs4 import BeautifulSoup
import requests
import pandas as pd

class Anime():

    def __init__(self):
        pass
        # anime name
        # anime update
        # season: spring, summer...
        # entrance: url

def get_anime_from_file(file_name):
    try:
        df = pd.read_csv(file_name) # this should cause except when no file
        anime2url = {}
        titles = df['Anime title'].tolist()
        # print(df.head())
        urls = df['url'].tolist()
        for i, j in zip(titles, urls):
            anime2url[i] = j
        return anime2url
    except:
        return {}
        

def main():
    print("main function")
    url = "https://ani.gamer.com.tw/" 
    resource = requests.get(url)
    # print(resource.text) 

    soup = BeautifulSoup(resource.text, 'html.parser')
    result = soup.find('div','index_season view-grid')

    print("loops")
    contents = result.find_all('a', 'newanime__content')

    file_name = '6-23_scrape.csv'
    
    # read file and return dictionaty
    anime2url = get_anime_from_file(file_name)
    # print("anime2url", anime2url)

    for index, i in enumerate(contents):
        name = i.find('p').text
        url = i['href']
        if name.encode('utf-8') not in anime2url:
            # anime2url[name] = url
            print("create an entry {}".format(name.encode('utf-8')))
            anime2url[name.encode('utf-8')] = url
        else:
            print("{} has in the file".format(name.encode('utf-8')))
        # check the anime update or not (no matter new or old anime)
    
    write_frame = pd.DataFrame(anime2url.items(), columns=['Anime title', 'url'])
    write_frame.to_csv(file_name)


if __name__ == '__main__':
    main()