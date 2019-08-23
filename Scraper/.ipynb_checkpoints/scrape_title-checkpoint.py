import bs4
import pandas as pd
import requests as r
import time
import random

iteration = '1'
export_file_name = 'Github_Title_' + iteration +'.csv'

title = []
href = []
current_page = ''

url = 'https://github.com'
page = '/pandas-dev/pandas/pulls?q=is%3Apr+is%3Aclosed'

header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

res = r.get(url + page, headers=header)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)

def scrape(tag, inline_tag, inline_tag_name):
    
    # Get title and href
    soup_target = soup.find_all(tag, {inline_tag: inline_tag_name})
    
    # Loop through the length soup_target and append to list
    for i in range(len(soup_target)):
        
        title.append(soup_target[i].text)

        href.append(soup_target[i].get('href'))

def request_soup(url, page):

    # Request page
    res = r.get(url + page, headers=header)

    # Raise status
    res.raise_for_status()

    # Return html code of that page
    return bs4.BeautifulSoup(res.text)

while True:
    # Time delay
    if current_page != '':
        # Choose a random page to scrape
        choice = random.choice([5, 7, 9])
        int(current_page)%choice==0
        
        # Delay by seconds
        random_number = random.randint(1,5)
        time.sleep(random_number)
    
    # Get html page
    soup = request_soup(url, page)
    
    # Next page
    next_page = soup.select('a[rel=next]')
    
    # Current page
    current_page = soup.select('em[class=current]')[0].text
    
    # If there is a next page
    if next_page != []:
       
        # Scrape title and href
        scrape('a', 'class', 'h4')

        # Get next page
        page = soup.select('a[rel=next]')[0].get('href')
        
        print('Scraped Page: ' + current_page)

    # If there's no next page
    else:
       
        soup = request_soup(url, page)

        # Scrape title and href
        scrape('a', 'class', 'h4')
        
        print('Scraped Page: ' + current_page)

        break

# Change list into series
s1 = pd.Series(title, name='title')
s2 = pd.Series(href, name='href')
        
# Concat series into a dataframe
df = pd.concat([s1,s2], axis=1)

# Export a csv file
df.to_csv(export_file_name, index=False)

print('Done')