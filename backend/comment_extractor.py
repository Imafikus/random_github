from models import ChoosenComment
from typing import List
import re
import data_extractor
import github_api
import os
import random

from dotenv import load_dotenv

load_dotenv()


MAX_COMMENT_NUMBER = int(os.environ['MAX_COMMENT_NUMBER'])
CURRENT_ENV = os.environ['ENV']

test_comments = [
    'Just for testing',
    'Not real stuff',
    'Whatever',
    'Lorem ipsum',
    'Testeroni testing test'
]

def extract_python_comments(file_content, file_url) -> List[ChoosenComment]:
    comments = re.findall(r'#.*', file_content)
    cleaned_comments = []
    
    for comment in comments:
        clean_part = comment.split('#')[1].strip()
        if clean_part != '':
            comment = ChoosenComment(
                content=clean_part,
                url=file_url
            )
            cleaned_comments.append(comment)
    
    return cleaned_comments
    

    
def get_comment() -> ChoosenComment:
    
    # if CURRENT_ENV == 'test':
    #     return random.choice(test_comments)
    
    chosen_comments = []
    
    repos = data_extractor.get_repos_with_supported_languages()
    for repo in repos:
        files = data_extractor.get_all_files(repo)
        language_specific_files = data_extractor.extract_all_language_files(files, repo.language)
        for f in language_specific_files:
            
            file_content = github_api.get_raw_data(f.download_url)
            chosen_comments += extract_python_comments(file_content, f.html_url)
        
        if len(chosen_comments) >= MAX_COMMENT_NUMBER:
            break
    return random.choice(chosen_comments)