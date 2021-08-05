from api import get_repo_contents
from models import SingleGetContentObj
from typing import List
import trending

SUPPORTED_LANGUAGES = ['Python']
EXTENSION_MAPPINGS = {
    'Python': 'md' #FIXME
}

def get_all_raw_file_urls(data: List[SingleGetContentObj]):
    
    raw_urls = []
    
    for item in data:
        if item.type == 'file':
            raw_urls.append(item.download_url)
    return raw_urls
            
def get_repos_with_supported_languages() -> List[trending.Repository]:
    all_repos = trending.extract_trending_repos()
    supported_repos = list(filter(lambda repo: repo.language in SUPPORTED_LANGUAGES, all_repos))
    return supported_repos
    
def get_all_files(repo: trending.Repository, file_list = []):
    pass

def extract_all_language_files(repo: trending.Repository) -> List[str]:
    data = get_repo_contents(repo.owner, repo.name)
    raw_urls = get_all_raw_file_urls(data)
    
    language_files = []
    
    for url in raw_urls:
        split_url = url.split('.')
        extension = split_url[-1]
        print(f'extension: {extension}')
        print(extension == EXTENSION_MAPPINGS[repo.language])
        
        if extension == EXTENSION_MAPPINGS[repo.language]:
            language_files.append(url)     
            
    return language_files
    
    