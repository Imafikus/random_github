from pydantic.tools import parse_obj_as
from models import SingleGetContentObj
import requests
from typing import List
from dotenv import load_dotenv
import os 

load_dotenv()

BASE_URL = 'https://api.github.com'
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
USER = os.environ['USER']

def _make_get_request(url: str): 
    return requests.get(url, auth=(USER, ACCESS_TOKEN))    

def get_repo_contents(owner: str, repo_name: str, folder_path='') -> List[SingleGetContentObj]:
    print(f'getting data for: {BASE_URL}/repos/{owner}/{repo_name}/contents/{folder_path}')
    data = _make_get_request(f'{BASE_URL}/repos/{owner}/{repo_name}/contents/{folder_path}')    
    if not data.ok:
        print('data not ok: ', data.text)
        return []
    
    return parse_obj_as(List[SingleGetContentObj], data.json())
    
def get_content(url: str) -> List[SingleGetContentObj]:
    data = _make_get_request(url)
    try:
        content = parse_obj_as(List[SingleGetContentObj], data.json())
    except Exception as e:
        print(e)
        content = []
    
    return content
        

def get_raw_data(url: str):
    data = _make_get_request(url)
    return data.text
    
def get_trending_page():
    data = _make_get_request('https://github.com/trending?spoken_language_code=en')
    return data.text