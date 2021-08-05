from bs4 import BeautifulSoup
import api


def extract_trending_repos():
    raw_html = api.get_trending_page()
    
    soup = BeautifulSoup(raw_html, 'html.parser')
    
    # for article in soup.find_all('article'):
    #     for link in article.get('a'):
    #         print(link)
    
    for repo in soup.find_all("h1", class_="h3 lh-condensed"):
        data = repo.find_next('a')
        print(data.get('href'))