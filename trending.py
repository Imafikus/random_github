from bs4 import BeautifulSoup
import api


def extract_trending_repos():
    raw_html = api.get_trending_page()
    
    soup = BeautifulSoup(raw_html, 'html.parser')
    
    for article in soup.find_all('article', class_='Box-row'):
        repo = article.find_next('h1', class_='h3 lh-condensed')
        repo_link = repo.find_next('a').get('href')
        
        language_obj = article.find_next('span',itemprop="programmingLanguage")
        if language_obj == None:
            continue
        
        language = language_obj.text
        
        print(repo_link)
        print(language)
        print()
    
    # for repo in soup.find_all("h1", class_="h3 lh-condensed"):
    #     data = repo.find_next('a')
    #     print(data.get('href'))