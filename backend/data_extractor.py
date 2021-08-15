from models import SingleGetContentObj
from typing import List
import trending
import github_api

SUPPORTED_LANGUAGES = ['Python']
EXTENSION_MAPPINGS = {
    'Python': 'py'
}

def extract_files(data: List[SingleGetContentObj]) -> List[SingleGetContentObj]:
    return list(filter(lambda item: item.type == 'file', data))
    
def extract_dirs(data: List[SingleGetContentObj]) -> List[SingleGetContentObj]:
    return list(filter(lambda item: item.type == 'dir', data))

def extract_all_language_files(data: List[SingleGetContentObj], language: str) -> List[SingleGetContentObj]:
    language_files = []
    
    for f in data:
        split_url = f.download_url.split('.')
        extension = split_url[-1]
        
        if extension == EXTENSION_MAPPINGS[language]:
            language_files.append(f)     
            
    return language_files

            
def get_repos_with_supported_languages() -> List[trending.Repository]:
    all_repos = trending.extract_trending_repos()
    supported_repos = list(filter(lambda repo: repo.language in SUPPORTED_LANGUAGES, all_repos))
    return supported_repos
    
def get_all_files(repo: trending.Repository) -> List[SingleGetContentObj]:
    content = github_api.get_repo_contents(repo.owner, repo.name)
    dirs = extract_dirs(content)
    files = extract_files(content)
    
    if len(dirs) == 0:
        return files
        
    while dirs != []:
        current_dir = dirs.pop()
        print('current_dir: ', current_dir.name)
        new_content = github_api.get_content(current_dir.url)
        new_dirs = extract_dirs(new_content)
        new_files = extract_files(new_content)
        files += new_files
        dirs += new_dirs
        
    return files    
