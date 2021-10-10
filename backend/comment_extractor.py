from models import ChoosenComment
from typing import List, Optional
import re
import data_extractor
import github_api
import os
import random
import datastore_db as db
import logging

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(format='[%(levelname)s]: %(asctime)s @ %(filename)s/%(funcName)s:%(lineno)d - %(message)s ', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)


MAX_COMMENT_NUMBER_PER_REPO = int(os.environ['MAX_COMMENT_NUMBER_PER_REPO'])
MAX_COMMENT_NUMBER_GLOBAL = int(os.environ['MAX_COMMENT_NUMBER_GLOBAL'])
CURRENT_ENV = os.environ['ENV']

test_comments = [
    ChoosenComment(
        content='Just for testing',
        url='https://example.com/'
    ),
    ChoosenComment(
        content='Not real stuff',
        url='https://example.com/'
    ),
    ChoosenComment(
        content='Whatever',
        url='https://example.com/'
    ),
    ChoosenComment(
        content='Testeroni testing test',
        url='https://example.com/'
    ),
    ChoosenComment(
        content='Lorem ipsum',
        url='https://example.com/'
    ),
]

def extract_single_random_python_comment(file_content, file_url) -> Optional[ChoosenComment]:
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
            
    if len(cleaned_comments) == 0:
        logging.info('No comments found, returning None...')
        return None
    
    return random.choice(cleaned_comments)
    
def get_all_choosen_comments() -> List[ChoosenComment]:
    
    if CURRENT_ENV == 'test':
        logging.info('Returning test_comments...')
        return test_comments
    
    chosen_comments = []
    
    repos = data_extractor.get_repos_with_supported_languages()
    for repo in repos:
        logging.info(f'Currently extracting from repo: {repo.name}')
        
        repo_comments = []
        files = data_extractor.get_all_files(repo)
        language_specific_files = data_extractor.extract_all_language_files(files, repo.language)
        logging.info(f'Number of language specific files found: {len(language_specific_files)}')
        
        
        for f in language_specific_files:
            
            file_content = github_api.get_raw_data(f.download_url)
            single_comment = extract_single_random_python_comment(file_content, f.html_url)
            if single_comment is not None:
                repo_comments.append(single_comment)
        
            if len(repo_comments) >= MAX_COMMENT_NUMBER_PER_REPO:
                logging.info(f'Max comment number reached for repo: {repo.name}')
                break
        
        chosen_comments += repo_comments
        logging.info(f'Current comment number: {len(chosen_comments)}')
        
        if len(chosen_comments) >= MAX_COMMENT_NUMBER_GLOBAL:
            logging.info(f'Max comment number reached globally, wrapping up...')
            break
    
    return chosen_comments
    
def main(message, context):
    db.insert_choosen_comments(get_all_choosen_comments())
    
if __name__ == "__main__":
    main(None, None)
