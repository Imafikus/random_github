from pydantic.tools import parse_obj_as
from models import SingleGetContentObj
import requests
from typing import List


BASE_URL = 'https://api.github.com'


def get_repo_contents(owner: str, repo_name: str, folder_path='') -> List[SingleGetContentObj]:
    print(f'getting data for: {BASE_URL}/repos/{owner}/{repo_name}/contents/{folder_path}')
    data = requests.get(f'{BASE_URL}/repos/{owner}/{repo_name}/contents/{folder_path}')    
    if not data.ok:
        return []
    
    return parse_obj_as(List[SingleGetContentObj], data.json())
    
def get_content(url: str) -> List[SingleGetContentObj]:
    data = requests.get(url)
    return parse_obj_as(List[SingleGetContentObj], data.json())

def get_raw_data(url: str):
    data = requests.get(url)
    return data.text
    
def get_trending_page():
    data = requests.get('https://github.com/trending?spoken_language_code=en')
    return data.text