from pydantic.tools import parse_obj_as
from models import SingleGetContentObj
import requests
from typing import List
from dotenv import load_dotenv
import os 
import logging

load_dotenv()

BASE_URL = 'https://api.github.com'
GITHUB_ACCESS_TOKEN = os.environ['GITHUB_ACCESS_TOKEN']
GITHUB_USERNAME = os.environ['GITHUB_USERNAME']

def _make_get_request(url: str): 
    return requests.get(url, auth=(GITHUB_USERNAME, GITHUB_ACCESS_TOKEN))    

def get_repo_contents(owner: str, repo_name: str, folder_path='') -> List[SingleGetContentObj]:
    logging.info(f'getting data for: {BASE_URL}/repos/{owner}/{repo_name}/contents/{folder_path}')
    data = _make_get_request(f'{BASE_URL}/repos/{owner}/{repo_name}/contents/{folder_path}')    
    if not data.ok:
        logging.error('data not ok: ', data.text)
        return []
    
    return parse_obj_as(List[SingleGetContentObj], data.json())
    
def get_content(url: str) -> List[SingleGetContentObj]:
    data = _make_get_request(url)
    try:
        content = parse_obj_as(List[SingleGetContentObj], data.json())
    except Exception as e:
        logging.error('get_content failed', e)
        content = []
    
    return content
        

def get_raw_data(url: str):
    data = _make_get_request(url)
    return data.text
    
def get_trending_page():
    data = _make_get_request('https://github.com/trending/python?since=daily&spoken_language_code=en') #TODO: Fix this when more than 1 language is supported
    return data.text
