from typing import List
from bs4 import BeautifulSoup
import github_api

class Repository:
    def __init__(self, owner, name, language) -> None:
        self.owner = owner
        self.name = name 
        self.language = language
    
    def __str__(self):
        return f'owner: {self.owner}\nname: {self.name}\nlanguage: {self.language}\n'
    
    
def extract_trending_repos() -> List[Repository]:
    raw_html = github_api.get_trending_page()
    
    soup = BeautifulSoup(raw_html, 'html.parser')
    
    repos = []
    
    for article in soup.find_all('article', class_='Box-row'):
        repo = article.find_next('h1', class_='h3 lh-condensed')
        repo_link = repo.find_next('a').get('href')
        
        repo_language_obj = article.find_next('span',itemprop="programmingLanguage")
        if repo_language_obj == None:
            continue
        
        split_repo_link = repo_link.split('/')
        repo_owner = split_repo_link[1]
        repo_name = split_repo_link[2]
        repo_language = repo_language_obj.text
        
        repos.append(
            Repository(repo_owner, repo_name, repo_language)
        )
    
    return repos